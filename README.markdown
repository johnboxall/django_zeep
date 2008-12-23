About
=====

Django application stub for using [zeep mobile](http://zeepmobile.com/).
This app ships with some models that will make hooking up zeep a little faster - it's pretty bare bones right now.

Installation
------------

* Download `zeep.sms`:

``sudo easy_install zeep.sms``

* Download `django_zeep`:

``git clone git@github.com:johnboxall/django_zeep.git ``

* Set your Zeep API Key / Secret and a default response in `settings.py`:

<code>
ZEEP_KEY = 'find-me-on-the-zeep-website'

ZEEP_SECRET = 'find-me-on-the-zeep-website'

ZEEP_DEFAULT_RESPONSE = 'default-response-if-no-rule-is-matched'

</code>