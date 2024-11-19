from django.urls import re_path

from .gpt_consumers import ChatGPTConsumer

websocket_urlpatterns = [
    re_path(r"^ws/orientation/search/$", ChatGPTConsumer.as_asgi()),
    # path('ws/search', ChatGPTConsumer.as_asgi()),
]