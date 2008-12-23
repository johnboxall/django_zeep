from django.conf import settings

import zeep.sms


def send_sms(user_id, message):
    "Send a message using the Zeep API."
    connection = zeep.sms.connect(settings.ZEEP_KEY, settings.ZEEP_SECRET)
    response = connection.send_message(user_id, message)
    return response
