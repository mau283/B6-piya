from email import message

from django.conf import settings
from django.core.mail import send_mail
from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from jobs_board_main.models import *
from jobs_board_main.signals import new_subscriber


@receiver(new_subscriber, sender = Subscription)
def handle_new_subscription(sender, **kwargs):
    print("fdyufhhjfhfhjjhhjfj")
    subscriber = kwargs['subscriber']
    job = kwargs['job'] 

    msg = f"""User {subscriber.email} has just subscribed to the job {job.title}"""

    print(msg)
    
    send_mail(f"{job.title}",
                message = msg, from_email="abc@gmail.com", recipient_list= ["knlchavan26@gmail.com",], fail_silently = False)

