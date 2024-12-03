from django.db import models
from django.contrib.auth.models import User
from job_app.models import Category






class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    age = models.PositiveIntegerField()
    education = models.CharField(max_length=250)
    techical_skills = models.CharField(max_length=250)
    softskills = models.CharField(max_length=255)


    def __str__(self):
        return f'{self.user.first_name}  {self.user.last_name}'




