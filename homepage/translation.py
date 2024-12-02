from modeltranslation.decorators import register
from modeltranslation.translator import TranslationOptions
from .models import *


# Service Translation:
@register(Service)
class ServiceTranslationOptions(TranslationOptions):
    fields = ('title', 'descriptions', )


# Ideas Translation:
@register(Ideas)
class IdeasTranslationOptions(TranslationOptions):
    fields = ('name', 'role', 'content', )


# Process Translation:
@register(ProcessStep)
class ProcessStepTranslationOptions(TranslationOptions):
    fields = ('title', 'descriptions', )