from django.contrib import admin
from modeltranslation.admin import TabbedTranslationAdmin
from django.shortcuts import redirect
from .models import HeaderModel, FooterModel, Wise_quotes


@admin.register(HeaderModel)
class HeaderAdmin(TabbedTranslationAdmin):
    list_display = ['title', 'description',]


    def changelist_view(self, request, extra_context=None):
        obj = HeaderModel.objects.first()
        if obj:
            return redirect('admin:%s_%s_change' % (self.model._meta.app_label, self.model._meta.model_name), obj.pk)
        return super().changelist_view(request, extra_context)


@admin.register(FooterModel)
class FooterAdmin(admin.ModelAdmin):
    list_display = ['address']


    def changelist_view(self, request, extra_context=None):
        obj = FooterModel.objects.first()
        if obj:
            return redirect('admin:%s_%s_change' % (self.model._meta.app_label, self.model._meta.model_name), obj.pk)
        return super().changelist_view(request, extra_context)


@admin.register(Wise_quotes)
class WiseQuoteAdmin(admin.ModelAdmin):
    list_display = ['quote', 'author']


