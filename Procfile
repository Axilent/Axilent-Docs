web: python manage.py collectstatic --noinput; gunicorn -b 0.0.0.0:$PORT -w 9 -k gevent --max-requests 250 docs.wsgi:application
