from django.db import models
import datetime
# Create your models here.


class appointment(models.Model):
    pkey = models.CharField(max_length=15)
    dkey = models.CharField(max_length=15)
    content = models.TextField()
    stime = models.TimeField(default=datetime.datetime.now,editable=True)
    date = models.DateField(default=datetime.datetime.now,editable=True)
    etime = models.TimeField(default=datetime.datetime.now,editable=True)
    passed = models.BooleanField(default=False)