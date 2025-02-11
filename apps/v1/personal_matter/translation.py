from modeltranslation.translator import register, TranslationOptions
from .models import PersonData


@register(PersonData)
class PersonDataTranslationOptions(TranslationOptions):
    fields = (
        'first_name',
        'last_name',
        'hobby',
        'nationality',
        'skin_color',
    )
