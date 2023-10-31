import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dgp.settings')
django.setup()

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from project.routing import websocket_urlpatterns
from channels.security.websocket import AllowedHostsOriginValidator
from channels.auth import AuthMiddlewareStack

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AllowedHostsOriginValidator(
            AuthMiddlewareStack(URLRouter(websocket_urlpatterns))
        ),
})