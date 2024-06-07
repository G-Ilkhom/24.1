from datetime import datetime

from django.core.management.base import BaseCommand

from materials.models import Course, Lesson
from users.models import Payment, User


class Command(BaseCommand):

    def handle(self, *args, **options):
        # Payment.objects.all().delete()
        # User.objects.all().delete()

        user, created = User.objects.get_or_create(email="example@sky.pro")
        course, created = Course.objects.get_or_create(name="Python-разработчик")
        lesson, created = Lesson.objects.get_or_create(
            name="Сериализаторы", course=course
        )

        Payment.objects.create(
            user=user,
            payment_date=datetime.now().date(),
            amount=500,
            payment_method="переводом",
            course=course,
            lesson=lesson,
        )

        self.stdout.write(self.style.SUCCESS(f"Платеж успешно создан"))
