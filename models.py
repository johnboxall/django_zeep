import re

from django.db import models

from django_zeep.managers import ZeepEventManager


FORMAT_RE = re.compile('[(]\w+[)]')

class ZeepBase(models.Model):
    "Zeep base."
    short_code = models.CharField(max_length=32, blank=True)
    event = models.CharField(max_length=32, blank=True,
        help_text="MO / SUBSCRIPTION_UPDATE")
    sms_prefix = models.CharField(max_length=32, blank=True)
    uid = models.CharField(max_length=32, blank=True)
    min = models.CharField(max_length=32, blank=True)
    body = models.CharField(max_length=160, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True
        
class ZeepEvent(ZeepBase):
    "Zeep event."
    rule = models.ForeignKey('django_zeep.ZeepRule', blank=True, null=True)
    response = models.CharField(max_length=160, blank=True)
    
    def find_rule(self, commit=False):
        "Find the best rule for this event."
        rule = ZeepRule.objects.rule_for_event(self)
        event = rule.apply_to_event(self)
        if commit:
            event.save()
        return event

class ZeepRule(ZeepBase):
    "Rule based on zeep event."
    objects = ZeepEventManager()
    format = models.CharField(max_length=160, blank=True, 
        help_text="(short_code) (event) (sms_prefix) (uid) (min) (body)")

    def __unicode__(self):
        return "%s" % self.format

    def apply_to_event(self, event):
        "Dynamic input based on what they sent"
        def swap(mo):
            "Expecting someting like `(uid)` transforms to `event.uid`"
            field = mo.group().strip('()')
            return getattr(event, field)
        event.response = FORMAT_RE.sub(swap, self.format)
        event.rule = self
        return event
    
        # response = self

    

# <QueryDict: {u'short_code': [u'test:88147'], u'event': [u'SUBSCRIPTION_UPDATE'], u'sms_prefix': [u'mobify'], u'uid': [u'106'], u'min': [u'test:933']}>


#<QueryDict: {u'body': [u''], u'sms_prefix': [u'mobify'], u'uid': [u'106'], u'min': [u'test:933'], u'short_code': [u'test:88147'], u'event': [u'MO']}>
