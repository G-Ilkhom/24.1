from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from materials.models import Course, Lesson, Subscription
from users.models import User


# class CourseTestCase(APITestCase):
#
#     def setUp(self):
#         self.user = User.objects.create(
#             email="test@sky.pro",
#             password="123",
#             is_superuser=True,
#             is_staff=True,
#             is_active=True,
#         )
#         self.course = Course.objects.create(
#             name="DRFTests", description="DRF Tests description", owner=self.user
#         )
#         self.lesson = Lesson.objects.create(
#             name="Tests",
#             description="Tests description",
#             course=self.course,
#             owner=self.user,
#         )
#         self.client = APIClient()
#         self.client.force_authenticate(user=self.user)
#
#     def test_course_retrieve(self):
#         url = reverse("materials:course-detail", args=(self.course.pk,))
#         response = self.client.get(url)
#         data = response.json()
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(data.get("name"), self.course.name)
#         self.assertIsNotNone(data.get("lessons"))
#
#     def test_course_create(self):
#         url = reverse("materials:course-list")
#         data = {"name": "Django", "description": "Django Test"}
#         response = self.client.post(url, data)
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         self.assertEqual(Course.objects.all().count(), 2)
#
#     def test_course_update(self):
#         url = reverse("materials:course-detail", args=(self.course.pk,))
#         data = {"name": "Docker"}
#         response = self.client.patch(url, data)
#         data = response.json()
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(data.get("name"), "Docker")
#
#     def test_course_delete(self):
#         url = reverse("materials:course-detail", args=(self.course.pk,))
#         response = self.client.delete(url)
#         self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
#         self.assertEqual(Course.objects.all().count(), 0)
#
#     def test_course_list(self):
#         url = reverse("materials:course-list")
#         response = self.client.get(url)
#         data = response.json()
#
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#
#         result = {
#             "count": 1,
#             "next": None,
#             "previous": None,
#             "results": [
#                 {
#                     "id": self.course.pk,
#                     "name": self.course.name,
#                     "lessons": [
#                         {
#                             "id": self.lesson.pk,
#                             "url_video": None,
#                             "name": self.lesson.name,
#                             "description": self.lesson.description,
#                             "preview": None,
#                             "course": self.course.pk,
#                             "owner": self.lesson.owner.pk,
#                         }
#                     ],
#                     "description": self.course.description,
#                     "count_lessons": 1,
#                     "owner": self.course.owner.pk,
#                 }
#             ],
#         }
#
#         self.assertEqual(data, result)


class LessonTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(
            email="test@sky.pro",
            password="123",
            is_superuser=True,
            is_staff=True,
            is_active=True,
        )
        self.course = Course.objects.create(
            name="DRFTests", description="DRF Tests description", owner=self.user
        )
        self.lesson = Lesson.objects.create(
            name="Tests",
            description="Tests description",
            course=self.course,
            owner=self.user,
        )
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_lesson_retrieve(self):
        url = reverse("materials:lesson_retrieve", args=(self.lesson.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("name"), self.lesson.name)

    def test_lesson_create(self):
        url = reverse("materials:lesson_create")
        data = {"name": "DRF", "course": self.course.id, "url_video": "https://www.youtube.com/docker/"}
        response = self.client.post(url, data)
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Lesson.objects.all().count(), 2)

    def test_lesson_update(self):
        url = reverse("materials:lesson_update", args=(self.lesson.pk,))
        data = {"name": "Docker"}
        response = self.client.patch(url, data)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("name"), "Docker")

    def test_lesson_delete(self):
        Lesson.objects.create(
            name="New Lesson",
            description="New Lesson description",
            course=self.course,
            owner=self.user,
        )
        url = reverse("materials:lesson_delete", args=(self.lesson.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Lesson.objects.all().count(), 1)

    def test_lesson_list(self):
        url = reverse("materials:lesson_list")
        response = self.client.get(url)
        data = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        result = {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [
                {
                    "id": self.lesson.pk,
                    "name": self.lesson.name,
                    "description": self.lesson.description,
                    "preview": None,
                    "course": self.lesson.course.pk,
                    "owner": self.lesson.owner.pk,
                    "url_video": None
                }
            ],
        }

        self.assertEqual(data, result)


class SubscriptionTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(
            email="test@sky.pro",
            password="123",
            is_superuser=True,
            is_staff=True,
            is_active=True,
        )
        self.course = Course.objects.create(
            name="DRFTests", description="DRF Tests description"
        )
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_subscription_activate(self):
        data = {"user_id": self.user.id, "course_id": self.course.id}
        response = self.client.post("/course/subscription/", data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), {"message": "Подписка добавлена"})

    def test_subscription_deactivate(self):
        Subscription.objects.create(user=self.user, course=self.course)
        data = {"user_id": self.user.id, "course_id": self.course.id}
        response = self.client.post("/course/subscription/", data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), {"message": "Подписка удалена"})
