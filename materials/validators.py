from rest_framework.serializers import ValidationError


def youtube_url_validator(value):
    if "https://www.youtube.com/" not in value.lower():
        raise ValidationError("Использована запрещенная ссылка")
