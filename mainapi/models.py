from turtle import title
from django.db import models
from django.utils import timezone as tz


class Todo(models.Model):
    title = models.CharField(max_length=100)
    begins = models.TimeField(default=tz.now)
    ends = models.TimeField(default=tz.now)
    done = models.BooleanField(default=False)

    def __str__(self):
        if self.done:
            return "{}-Completed".format(self.title, self.done)
        else:
            return "{}-Not Completed".format(self.title, self.done)
            
        
    

    class Meta: 
        verbose_name = "a todo"
        verbose_name_plural = "Todolist"


