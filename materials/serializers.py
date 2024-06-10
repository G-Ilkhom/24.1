from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from materials.models import Course, Lesson


class LessonSerializer(ModelSerializer):

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
