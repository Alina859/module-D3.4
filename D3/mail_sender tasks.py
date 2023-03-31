from celery import shared_task
from news.models import Category, Post
from .config import newsletter_sender

import datetime


@shared_task
def mailing():
    list_recipients = []
    date_from = datetime.datetime.now() - datetime.timedelta(days=7)
    for category in Category.objects.all():
        list_recipients.clear()
        for user in category.subscribed_users.all():
            list_recipients.append(user.email)
        posts = Post.objects.filter(category=category, date_time_in__gte=date_from)
        newsletter_sender(list_recipients, category.name, posts)