from django import template
from django.conf import settings

register = template.Library()


@register.inclusion_tag('django_zeep/panel.html')
def zeep_panel(style=None, obj=None):
    if obj is None:
        # No id? Just use the current timestamp.
        import time
        id = int(time.time())
    else:
        id = obj.id    
    return dict(id=id, key=settings.ZEEP_KEY, style=style)
