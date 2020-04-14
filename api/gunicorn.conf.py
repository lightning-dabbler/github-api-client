"""gunicorn WSGI server configuration."""
from multiprocessing import cpu_count

bind = "0.0.0.0:2064"
workers = cpu_count() * 2 + 1
loglevel = 'info'
max_requests = 10000
timeout = 40
