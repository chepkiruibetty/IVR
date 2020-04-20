from django.urls import path
from .views import Calls, CallResponseForLanguage

urlpatterns = [
    path('calls/', Calls.as_view(), name='calls'),
    path('call/response/', CallResponseForLanguage.as_view(), name='language_response'),
]
