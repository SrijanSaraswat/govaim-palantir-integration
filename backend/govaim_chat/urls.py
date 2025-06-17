from django.urls import path
from .views import chat_handler

urlpatterns = [
    path('', chat_handler, name='chat_handler'),
]
