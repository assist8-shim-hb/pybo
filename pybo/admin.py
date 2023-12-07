from django.contrib import admin
from .models import Question
from djangoql.admin import DjangoQLSearchMixin


class QuestionAdmin(DjangoQLSearchMixin, admin.ModelAdmin):
    search_fields = ['subject']


# Register your models here.
admin.site.register(Question, QuestionAdmin)
