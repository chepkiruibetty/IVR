from django.urls import path
from .views import Calls

urlpatterns = [
    path('calls/', Calls.as_view(), name='calls'),
]
