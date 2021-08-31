from django.contrib import admin
from .models import *

from django.contrib.auth.models import User, Group


admin.site.unregister(User)
admin.site.unregister(Group)


class ContactAdmin(admin.ModelAdmin):
    model = Contact
    list_display = ('name', 'phone', 'email')


class MailAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False if self.model.objects.count() > 0 else super().has_add_permission(request)


class LessonInLine(admin.StackedInline):
    model = Lesson
    list_display = ('name', 'module')


class ModuleAdmin(admin.ModelAdmin):
    ordering = ('course', 'number')
    inlines = [LessonInLine]


class ModuleInLine(admin.StackedInline):
    ordering = ('number',)
    model = Module
    extra = 1


class SkillsInLine(admin.StackedInline):
    model = Skills
    extra = 1


class CuratorAdmin(admin.ModelAdmin):
    pass


class QuestionBusinessAdmin(admin.ModelAdmin):
    pass


class QuestionInLine(admin.StackedInline):
    model = Question


class CourseAdmin(admin.ModelAdmin):
    inlines = [ModuleInLine, SkillsInLine, QuestionInLine]


admin.site.register(QuestionBusiness, QuestionBusinessAdmin)
admin.site.register(Mail, MailAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Module, ModuleAdmin)
admin.site.register(Curator, CuratorAdmin)
admin.site.register(Course, CourseAdmin)