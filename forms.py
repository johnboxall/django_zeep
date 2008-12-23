from django import forms

from django_zeep.models import ZeepEvent


class ZeepEventModelForm(forms.ModelForm):
    class Meta:
        model = ZeepEvent