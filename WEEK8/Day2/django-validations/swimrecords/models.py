from django.db import models
from django.core import validators as v

from .validators import (
    validate_relay, 
    validate_stroke,
    validate_record_date,
    )

class SwimRecord(models.Model):
 
    first_name = models.CharField(blank=False)
    last_name = models.CharField(blank=False)
    team_name = models.CharField(blank=False)
    relay = models.BooleanField(default=True,validators=[validate_relay])
    stroke = models.CharField(validators=[validate_stroke])
    distance = models.IntegerField(validators=[v.MinValueValidator(50)])
    record_date = models.DateTimeField(validators=[validate_record_date])
    record_broken_date = models.DateTimeField()
