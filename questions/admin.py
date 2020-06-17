from django.contrib import admin

from .models import Question, QestionCategory


admin.site.register(Question)
admin.site.register(QestionCategory)
