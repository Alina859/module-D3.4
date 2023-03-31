from django.db.models.signals import post_save
from django.core.mail import send_mail
from django.dispatch import receiver
from django.conf import settings
from django.contrib.auth.models import User
@receiver(post_save, sender=User)
def notify_managers_posts(sender, instance, created, **kwargs):
    if created:
        title = f'NewsPaper. Пользователь {instance.username} зарегистрирован.'
        message = f'Добрый день, {instance.username}!\n' \
                  f'Команда NewsPaper благодарит вас за регистрацию на нашем портале.\n' \
                  f'Теперь вам доступны: личный кабинет и возможности писать комментарии,' \
                  f' или стать автором и написать статью.'
    else:
        title = f'NewsPaper. Данные пользователя {instance.username} изменены.'
        message = f'Добрый день, {instance.username}!\n' \
                  f'Ваши персональные данные были изменены. Подробнее в личном кабинете , на сайте.'
    send_mail(
        subject=title,
        message=message,
        from_email=settings.SERVER_EMAIL,
        recipient_list=[instance.email]
        recipient_list=[instance.email,]
    )