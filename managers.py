from django.db import models


class ZeepEventManager(models.Manager):
    def rule_for_event(self, event):
        "Retrieve the rule that applies to this event."
        # Eventually this could be some crazy search through the rules
        # but for now we'll just look for a rule with a matching event type
        rule = self.filter(event=event.event)[0]
        return rule