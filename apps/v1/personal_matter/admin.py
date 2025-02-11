from django.contrib import admin
from .models import PersonData
from modeltranslation.admin import TabbedTranslationAdmin

@admin.register(PersonData)
class PesronDataAdmin(TabbedTranslationAdmin):
    list_display = ('first_name', 'last_name', 'gender', 'nationality', 'hobby', 'height', 'weight',)
    search_fields = ('first_name', 'last_name', 'hobby')
    list_filter = ('gender', 'height', 'weight',)
    fieldsets = (
        ('Main Data', {
            'fields': ('image', 'first_name', 'last_name')
        }),
        ('Personal Information', {
            'fields': ('hobby', 'gender', 'nationality', 'height', 'weight', 'date_of_birth')
        }),
        ('Contact Information', {
            'fields': ('email', 'phone', 'address')
        }),
    )