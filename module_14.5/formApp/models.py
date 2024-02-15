from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

def comma_separated_validator(value):
    values = value.split(',')
    for val in values:
        if not val.strip():
            raise ValidationError(_('Empty values are not allowed.'))

class Employee(models.Model):
    empId = models.BigAutoField(primary_key=True)
    name = models.TextField()
    status = models.BooleanField()
    address = models.CharField(
        validators=[comma_separated_validator],
        max_length=255
    )
    dateOfBirth = models.DateField()
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    salary = models.DecimalField(max_digits=5, decimal_places=2)
    duration = models.DurationField()
    email = models.EmailField()
    resume = models.FileField(upload_to='files/')
    result = models.FloatField()
    image = models.ImageField()
    age = models.IntegerField()
    otherData = models.JSONField()
    otherUrl = models.URLField()
    uid = models.UUIDField()
