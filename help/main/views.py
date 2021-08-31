from django.core.mail import send_mail, EmailMultiAlternatives
from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string, get_template
from django.utils.html import strip_tags

from .models import Curator, Course, Module, Contact, QuestionBusiness, Mail
from .forms import ContactForm, MailForm


def index(request):
    speakers = Curator.objects.all()
    courses = Course.objects.all()
    return render(request, 'index.html', {'speakers': speakers, 'courses': courses})


def courses(request):
    form = MailForm(request.POST)
    courses = Course.objects.all()
    speakers = Curator.objects.all()
    mail_message = Mail.objects.all()
    email = ''
    # Отправляем письмо если форма подверждена
    html_message = render_to_string('mail.html', {'context': mail_message})
    plain_message = strip_tags(html_message)

    # Отправляем письмо если форма подверждена
    if form.is_valid():
        email = form.cleaned_data.get('mail')
    send_mail(
        'Вам подарочек!',
        plain_message,
        'artemon.m174@gmail.com',
        [email],
        html_message=html_message,
        fail_silently=True
    )

    return render(request, 'second.html', {'courses': courses, 'speakers': speakers, 'form': form})


def course(request, slug):
    course = get_object_or_404(Course, slug__iexact=slug)
    module = Module.objects.all()
    form = ContactForm(request.POST)
    client = Contact()
    if form.is_valid():
        client.name = form.cleaned_data.get('name')
        client.email = form.cleaned_data.get('mail')
        client.phone = form.cleaned_data.get('phone')
        client.save()
    return render(request, 'third.html', {'course': course, 'module': module, 'form': form})


def business(request):
    form = ContactForm(request.POST)
    client = Contact()
    questions = QuestionBusiness.objects.all()
    if form.is_valid():
        client.name = form.cleaned_data.get('name')
        client.email = form.cleaned_data.get('mail')
        client.phone = form.cleaned_data.get('phone')
        client.save()

    return render(request, 'fourth.html', {'form': form, 'questions': questions})
