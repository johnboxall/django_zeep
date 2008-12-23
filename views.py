from django.conf import settings
from django.http import HttpResponse

from django_zeep.forms import ZeepEventModelForm
from django_zeep.helpers import send_sms

def callback(request):
    "Callback from Zeep."    

    if request.method == "GET":
        from django.shortcuts import render_to_response
        return render_to_response('django_zeep/test.html', {'form':ZeepEventModelForm()})
    
    response = settings.ZEEP_DEFAULT_RESPONSE
    if request.method == "POST":
        form = ZeepEventModelForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.find_rule()
            event.save()
            response = event.response            
        
    # print response
    # Hack just send a message back w/ the response
    # SUBSCRIPTION_UPDATE
    send_sms(event.uid, response)
    
    
    return HttpResponse(response, mimetype="text/plain")



