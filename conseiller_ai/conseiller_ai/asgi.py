import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import orientation.routing  # Assure-toi que 'orientation.routing' est correct

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'conseiller_ai.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),  # Gère les requêtes HTTP
    "websocket": AuthMiddlewareStack(URLRouter(orientation.routing.websocket_urlpatterns)),  # Gère les WebSockets
})
    