from rest_framework import generics
from django.http import HttpResponse


# Create your views here.
class Calls(generics.CreateAPIView):
    def post(self, request, *args, **kwargs):
        isActive = request.POST.get("isActive")
        if isActive == '1':
            content = """<?xml version="1.0" encoding="utf-8"?> <Response> <GetDigits timeout="10" finishOnKey="#" 
            callbackUrl=""> <Say>Welcome to Furaha Bank. Your bank of choice. Please press one followed by hash for 
            English. Please press two followed by hash for Kiswahili</Say> </GetDigits> <Say>We did not get any 
            response. Good bye</Say> </Response> """
            response = HttpResponse(content, content_type="application/xml; charset=utf-8")
            response['Content-Length'] = len(content)

            return response

        return HttpResponse("Ok")
