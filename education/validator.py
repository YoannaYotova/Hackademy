import requests
from django.core.exceptions import ValidationError


def validate_url(url):
    r = requests.get(url)
    if not r.status_code < 400:
        raise ValidationError('URL does not exist')
