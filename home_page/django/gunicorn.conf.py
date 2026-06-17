bind = '0.0.0.0:8000'
workers = 1
worker_class = 'sync'
threads = 1
timeout = 0
accesslog = '/logs/gunicorn/access.log'
errorlog = '/logs/gunicorn/error.log'
wsgi_app = 'mysite.wsgi:application'
