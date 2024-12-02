from modeltranslation.decorators import register
from modeltranslation.translator import TranslationOptions
from .models import *

# CompanyInfo transilation options:
@register(CompanyInfo)
class CompanyInfoTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'mission_statement', )



# Teammember transilation options:
@register(CompanyInfo)
class TeamMemberTranslationOptions(TranslationOptions):
    fields = ('name', 'role',)