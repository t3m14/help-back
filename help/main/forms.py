from django import forms
from .models import Contact


class ContactForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'feedback__input input',

        'placeholder': ' Имя',
    }))
    mail = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'feedback__input input',

        'placeholder': 'e-mail',
    }))
    phone = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'feedback__input input',

        'placeholder': '8 912 345 67 89',
    }))


class MailForm(forms.Form):
    mail = forms.CharField(max_length=100,
                           widget=forms.EmailInput
                           (attrs={'class': 'mail__input',
                                   'class': 'input',
                                   'placeholder': 'e-mail',
                                   }
                            )
                           )
