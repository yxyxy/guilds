import os
import sys
from django.core.wsgi import get_wsgi_application

sys.path.append('/guilds')

try:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'auth_service.app.settings')
    application = get_wsgi_application()
except Exception as e:
    print(f"Error initializing Django application: {e}")
    raise