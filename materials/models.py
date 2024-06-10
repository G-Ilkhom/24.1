from django.db import models

User = "users.User"


class Course(models.Model):
    name = models.CharField(
        max_length=100, verbose_name="Название курса", help_text="Укажите курс"
    )
    preview = models.ImageField(
        upload_to="course/preview", verbose_name="превью", blank=True, null=True
    )
    description = models.TextField(
        blank=True, null=True, help_text="Укажите описание курса"
    )
    owner = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Владелец",
        help_text="Укажите владельца",
    )

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"


class Lesson(models.Model):
    name = models.CharField(
        max_length=100, verbose_name="Название урока", help_text="Укажите урок"
    )
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, verbose_name="курс", related_name="lessons"
    )
    description = models.TextField(
        blank=True, null=True, help_text="Укажите описание урока"
    )
    preview = models.ImageField(
        upload_to="lesson/preview", verbose_name="превью", blank=True, null=True
    )
    url_video = models.URLField(verbose_name="ссылка на видео", blank=True, null=True)
    owner = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Владелец",
        help_text="Укажите владельца",
    )

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"
