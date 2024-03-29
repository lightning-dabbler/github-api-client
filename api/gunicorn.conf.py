"""gunicorn WSGI server configuration."""
import os
from multiprocessing import cpu_count

bind = f"0.0.0.0:{os.environ.get('X_GUNICORN_PORT',2064)}"
workers = cpu_count() * 2 + 1
loglevel = "info"
max_requests = 10000
timeout = 40
preload_app = True
