from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail
from materials.models import Course, Subscription
from datetime import timezone, datetime, timedelta
from users.models import User


@shared_task
def send_email(course_id):
    try:
        course = Course.objects.get(pk=course_id)
        subscribers = Subscription.objects.get(course=course_id)

        print("Отправка работает")

        send_mail(
            subject=f'Курс {course} обновлен',
            message=f'Курс {course}, на который вы подписаны, обновлен',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[subscribers.user.email]
        )
    except Course.DoesNotExist:
        print(f"Курс с id={course_id} не найден.")
    except Subscription.DoesNotExist:
        print(f"Подписчики на курс с id={course_id} не найдены.")


@shared_task
def check_inactive_users():
    active_users = User.objects.filter(is_active=True)
    now = datetime.now(timezone.utc)
    for user in active_users:
        if user.last_login:
            if now - user.last_login > timedelta(days=30):
                user.is_active = False
                user.save()
                print(f"Пользователь {user} заблокирован")
