### SIMPLEST CASE HOW TO SEND EMAIL WITH CELERY
IN USE:
- django
- celery
- redis

INSTRUCTIONS
- start project
- create app
- go to celery [docs](https://docs.celeryq.dev/en/stable/django/first-steps-with-django.html), do what they say
- - create celery.py
- - update _\_\_init\_\_.py_

- set celery consts at _settings.py_\
CELERY_BROKER_URL = 'localhost'\
CELERY_ACCEPT_CONTENT = ['json']\
CELERY_TASK_SERIALIZER = 'json'

- set email consts at _settings.py_ ([source](https://dev-ed.ru/blog/django-email-gmail-mailru-yandex/))\
EMAIL_HOST = 'smtp.yandex.ru'\
EMAIL_PORT = 465\
EMAIL_USE_TLS = False\
EMAIL_USE_SSL = True\
EMAIL_HOST_USER = 'sender.email@yandex.ru'
EMAIL_HOST_PASSWORD = 'sender_email_password'

- create _tasks.py_ in the app dir
- create tasks in _tasks.py_ (import @shared_task)
- create a view
- create urls
- import tasks to _views.py_ and use them
