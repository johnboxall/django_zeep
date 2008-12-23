from django.contrib import admin
from django.forms.models import fields_for_model

from django_zeep.models import *


class ZeepEventAdmin(admin.ModelAdmin):
    list_display = fields_for_model(ZeepEvent).keys()
#    search_fields = ['website', 'page']

class ZeepRuleAdmin(admin.ModelAdmin):
    list_display = fields_for_model(ZeepRule).keys()
#    search_fields = ['website']

