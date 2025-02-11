from modeltranslation.translator import register, TranslationOptions
from .models import HeaderModel


@register(HeaderModel)
class HeaderModelTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)