from django.db import models
from django.contrib.auth.models import User



class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.CharField(max_length=100)
    

    def __str__(self):
        return str(self.task)
