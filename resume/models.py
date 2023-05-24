from django.db import models

# Create your models here.

class Bio(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    one_liner = models.CharField(max_length=100)
    summary = models.TextField()
    skills = models.TextField()

    def __str__(self):
        return self.name


class Experience(models.Model):
    company = models.CharField(max_length=255)
    position = models.CharField(max_length=300)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    
    def __str__(self):
        return f'{self.position} at {self.name}'


class Project(models.Model):
    name = models.CharField(max_length=500)
    url = models.URLField()
    description = models.TextField()
    image = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.name

