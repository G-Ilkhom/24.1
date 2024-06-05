from django.core.management.base import BaseCommand
from users.models import User, Payment
from materials.models import Course, Lesson
from datetime import datetime


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.first()
        course = Course.objects.first()
        lesson = Lesson.objects.first()

        payment_data = {
            'user': user,
            'payment_date': datetime.now().date(),
            'amount': 250.00,
            'payment_method': 'переводом'
        }

        if course:
            payment_data['course'] = course
        if lesson:
            payment_data['lesson'] = lesson

        payment = Payment.objects.create(**payment_data)
        self.stdout.write(self.style.SUCCESS(f'Платеж успешно создан: {payment.id}'))
