"""
WSGI config for Nezapadni project.
"""

import os
import sys
from pathlib import Path
from django.core.wsgi import get_wsgi_application

# BASE_DIR = /app/Nezapadni
BASE_DIR = Path(__file__).resolve().parent.parent

# Добавляем /app/Nezapadni в PYTHONPATH,
# чтобы Django видел apps: accounts, main, courses
if str(BASE_DIR) not in sys.path:
    sys.path.append(str(BASE_DIR))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Nezapadni.Nezapadni.settings")

application = get_wsgi_application()
