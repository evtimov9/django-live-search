import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
import live_search_app.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'live_search_project.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": URLRouter(live_search_app.routing.websocket_urlpatterns),
})
