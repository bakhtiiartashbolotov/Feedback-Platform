from django.contrib import admin

from django.contrib import admin
from .models import Feedback
from .models import Category

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('question', 'category', 'id')
    list_filter = ['category']
    search_fields = ('question',)

admin.site.register(Category)
