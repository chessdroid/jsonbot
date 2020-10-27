from django.db import models
from django.utils.html import format_html


class Account(models.Model):
    username = models.CharField(max_length=50, unique=True, blank=True, null=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    language_code = models.CharField(max_length=10)
    is_bot = models.BooleanField(null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def clean(self):
        if not (self.last_name or self.is_student):
            raise ValidationError('one of the names must not be empty')