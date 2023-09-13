import os


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "judonazim.settings")
import django
django.setup()


from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter, get_default_application
from channels.security.websocket import AllowedHostsOriginValidator
from django.core.asgi import get_asgi_application

#from chats.routing import websocket_urlpatterns


# Initialize Django ASGI application early to ensure the AppRegistry
# is populated before importing code that may import ORM models.
django_asgi_app = get_asgi_application()

import chats.routing
import notifications.routing

application = ProtocolTypeRouter(
    {
        "http": django_asgi_app,
        "websocket": AllowedHostsOriginValidator(
            AuthMiddlewareStack(URLRouter([
            *chats.routing.websocket_urlpatterns,
            *notifications.routing.websocket_urlpatterns,

             ])
            )
        ),
    }
)
