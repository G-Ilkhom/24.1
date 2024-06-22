from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail
from materials.models import Course, Subscription
from datetime import timezone
from users.models import User


@shared_task
def send_email(course_id):
    course = Course.objects.get(pk=course_id)
    subscribers = Subscription.objects.get(course=course_id)
    print("Отправка работает")

    send_mail(
        subject=f'Курс {course} обновлен',
        message=f'Курс {course},на который вы подписаны обновлён',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[subscribers.user.email, 'anonymoustoken@mail.ru']
    )


@shared_task
def check_inactive_users():
    one_month = timezone.now() - timezone.timedelta(days=30)
    inactive_users = User.objects.filter(last_login__lt=one_month)
    for user in inactive_users:
        user.is_active = False
        user.save()