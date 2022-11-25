import json

from django.core.mail import send_mail

from autoProject.celery import app


@app.task()
def send_spam(data):
    send_mail('ДОБРОЙ НОЧИ!',
              'Dealer:'+json.dumps(data),
              'noooowell@gmail.com',
              ['pavel-kul1707@mail.ru'],
              fail_silently=False)
