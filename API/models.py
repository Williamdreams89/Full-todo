from datetime import datetime
from pyexpat import model
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone as tz
from datetime import date, time
# Create your models here.


class Todolist(models.Model):
    task_manager = models.ForeignKey(User, on_delete=models.CASCADE, related_name="todolist")
    title = models.CharField(max_length=100)
    start_time = models.TimeField(auto_now=True)
    end_time = models.TimeField()
    done = models.BooleanField(default=False)
    created = models.DateField(default=date.today)


    def __str__(self):
        return "{}-({})".format(self.title, self.task_manager)
    
