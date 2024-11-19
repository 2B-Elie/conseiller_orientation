from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import orientation.routing

from django.core.asgi import get_asgi_application

ASGI_APPLICATION = get_asgi_application()


application = ProtocolTypeRouter(
    {
        # (http->django views is added by default)
        "websocket": AuthMiddlewareStack(URLRouter(orientation.routing.websocket_urlpatterns)),
    }
)
