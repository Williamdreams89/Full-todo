from datetime import datetime
from django.db import models
from django.utils import timezone as tz


class Todo(models.Model):
    title = models.CharField(max_length=100)
    begins = models.DateTimeField(default=tz.now)
    ends = models.DateTimeField(default=tz.now)
    done = models.BooleanField(default=False)
    start_date = models.DateField(default=datetime.now)
    end_date = models.DateField(default=datetime.now)
    def __str__(self):
        if self.done:
            return "{}-Completed".format(self.title, self.done)
        else:
            return "{}-Not Completed".format(self.title, self.done)
            
    
    

    class Meta: 
        verbose_name = "a todo"
        verbose_name_plural = "Todolist"


