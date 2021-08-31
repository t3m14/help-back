from django.db import models
from django.urls import reverse


class Curator(models.Model):
    image = models.ImageField(verbose_name="Фото", upload_to="curators")
    name = models.CharField(max_length=25, verbose_name='Имя')
    post = models.CharField(max_length=20, verbose_name="Должность")

    class Meta:
        verbose_name = 'Куратор'
        verbose_name_plural = 'Кураторы'




class Course(models.Model):
    name = models.CharField(max_length=50, verbose_name="Название курса", default='Название курса', unique=True)
    slider_description = models.TextField(max_length=200, verbose_name="Описание курса для слайдера")
    description = models.TextField(max_length=255, verbose_name="Описание курса на его странице")
    speaker_photo = models.ImageField(verbose_name="Фото спикера курса", upload_to="speakers")
    speaker_name = models.CharField(max_length=25, verbose_name="Имя спикера курса")
    speaker_description = models.CharField(max_length=255, verbose_name="Описание спикера", default='Описание спикера')

    slug = models.SlugField(verbose_name="Имя ссылки для курса", max_length=255, unique=True, db_index=True, null=False, help_text="Желательно сделать ссылку похожей на название")

    def get_questions(self):
        question = Question()
        return self.question_set.all()

    def get_modules(self):
        module = Module()
        return self.module_set.all()

    def get_skills(self):
        skills = Skills()
        return self.skills_set.all()

    def get_absolute_url(self):
        return reverse('course', kwargs={'course_slug': self.slug})

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


class Skills(models.Model):
    speaker_skills = models.ForeignKey(Course, help_text="Выберите навыки спикера", on_delete=models.CASCADE)
    skill = models.CharField(max_length=150, verbose_name="Навык спикера")

    def __str__(self):
        return self.skill

    class Meta:
        verbose_name = 'Навык спикера курса'
        verbose_name_plural = 'Навыки спикера курса'


class Module(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    caption = models.CharField(max_length=30, verbose_name='Название модуля курса')
    number = models.PositiveSmallIntegerField(verbose_name="Порядковый номер модуля", default=1)


    class Meta:
        ordering = ('number',)

    def get_lessons(self):
        lesson = Lesson()
        return self.lesson_set.all()

    def __str__(self):

        return str( str(self.number) + '. - ' + self.caption + " - " + self.course.name)

    class Meta:
        verbose_name = 'Модуль'
        verbose_name_plural = 'Модули'


class Lesson(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название урока")
    module = models.ForeignKey(Module, help_text="Выберете модуль", on_delete=models.CASCADE, verbose_name="Модуль")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"


class Contact(models.Model):
    name = models.CharField(max_length=50, verbose_name="Имя")
    email = models.EmailField(max_length=100, verbose_name="Почта")
    phone = models.CharField(max_length=12, verbose_name="Телефон")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Контакты для обратной связи"
        verbose_name_plural = "Контакты для обратной связи"


class Mail(models.Model):
    desc = models.TextField(verbose_name="Инструкции для письма")

    def __str__(self):
        return self.desc

    class Meta:
        verbose_name = "Описание инструкций для письма"
        verbose_name_plural = "Описание инструкций для письма"


class Question(models.Model):
    module = models.ForeignKey(Course, on_delete=models.CASCADE)
    question = models.CharField(max_length=50, verbose_name="Вопрос")
    answer = models.CharField(max_length=255, verbose_name="Ответ")

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'


class QuestionBusiness(models.Model):
    question = models.CharField(max_length=50, verbose_name="Вопрос")
    answer = models.CharField(max_length=255, verbose_name="Ответ")

    def __str__(self):
        return self.question


    class Meta:
        verbose_name = 'Вопрос для упаковки бизнеса'
        verbose_name_plural = 'Вопросы для упаковки бизнеса'

