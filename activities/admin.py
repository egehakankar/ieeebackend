from django.contrib import admin
from .models import Social, Technical

# Register your models here.
@admin.register(Social, Technical)
class SocialAdmin(admin.ModelAdmin):
    search_fields = [
        'title',
    ]
    list_filter = [
        'title'
    ]
    list_display = ['id', 'title', 'branch', 'littleSummary']
    
class TechnicalAdmin(admin.ModelAdmin):
    search_fields = [
        'title',
    ]
    list_filter = [
        'title'
    ]
    list_display = ['id', 'title', 'branch', 'littleSummary']
