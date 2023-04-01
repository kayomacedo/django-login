from django.contrib import admin
from .models import Question, Answer

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'title', 'created_date')
    list_display_links = ('id', 'title')
    list_filter = ('user', 'created_date')

admin.site.register(Question, QuestionAdmin)

