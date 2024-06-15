from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from materials.models import Course, Lesson, Subscription
from materials.validators import youtube_url_validator


class LessonSerializer(ModelSerializer):
    url_video = serializers.URLField(validators=[youtube_url_validator])

    class Meta:
        model = Lesson
        fields = "__all__"


class CourseSerializer(ModelSerializer):
    count_lessons = SerializerMethodField(read_only=True)
    lessons = LessonSerializer(many=True, read_only=True)

    def get_count_lessons(self, obj):
        return obj.lessons.count()

    class Meta:
        model = Course
        fields = ["id", "name", "lessons", "description", "count_lessons", "owner"]


class SubscriptionSerializer(serializers.ModelSerializer):
    is_subscribed = serializers.SerializerMethodField()

    class Meta:
        model = Subscription
        fields = ["user", "course", "is_subscribed"]

    def get_is_subscribed(self, obj):
        user = self.context["request"].user
        return Subscription.objects.filter(user=user, course=obj.course).exists()
