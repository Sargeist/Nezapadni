"""
ASGI config for Nezapadni project.
"""

import os
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Nezapadni.settings')

application = get_asgi_application()
