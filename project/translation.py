from modeltranslation.decorators import register
from modeltranslation.translator import TranslationOptions
from .models import Project, Category


# Project translation:
@register(Project)
class ProjectTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'client', 'location')


# Category translation:
@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'description',)