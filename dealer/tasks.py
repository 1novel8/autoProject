import json

from django.core.mail import send_mail

from autoProject.celery import app


@app.task()
def send_spam(data):
    send_mail('ДОБРОЙ НОЧИ!',
              'Dealer:'+json.dumps(data),
              'noooowell@gmail.com',
              ['18.novel.18@gmail.com'],
              fail_silently=False
              )
