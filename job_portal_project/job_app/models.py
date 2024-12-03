from django.db import models

# Create your models here.


class Category(models.Model):
    category = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)

    def __str__(self):
        return self.category


class Roles(models.Model):
    Category = models.ForeignKey(Category, on_delete=models.CASCADE)
    job_role = models.CharField(max_length=250)
    slug =models.SlugField(max_length=250)

    def __str__(self):
        return self.job_role

class Jobs(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    role = models.ForeignKey(Roles, on_delete=models.CASCADE)
    company = models.CharField(max_length=250)
    location = models.CharField(max_length=250)
    qualification= models.CharField(max_length=250)
    technical_skills =models.TextField()
    softskills = models.TextField()
    experience_category = models.CharField(max_length=150)
    experience = models.CharField(max_length=250, blank=True, null=True)
    last_date = models.DateField()
    salary = models.CharField(max_length=250)
    email  = models.EmailField()
    tags = models.TextField()
    date_added = models.DateTimeField( auto_now_add=True)

    def __str__(self):
        return f'{self.role} - {self.company}-{self.location}'
