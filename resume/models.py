from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.
class Bio(models.Model):
    name = models.CharField(max_length=100)
    bio = RichTextUploadingField()
    one_liner = models.CharField(max_length=100)
    summary = RichTextUploadingField()
    skills = RichTextUploadingField()

    def __str__(self):
        return self.name


class Experience(models.Model):
    company = models.CharField(max_length=255)
    position = models.CharField(max_length=300)
    description = RichTextUploadingField()
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    still_work_here = models.BooleanField(default=False)
    is_seasonal = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.position} at {self.company}'


class Education(models.Model):
    institution = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    course = models.CharField(max_length=300)
    award = models.CharField(max_length=10)
    description = RichTextUploadingField()
    start_date = models.DateField()
    end_date = models.DateField()
    still_in_progress = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.award} {self.course} from {self.institution}'


class Project(models.Model):
    name = models.CharField(max_length=500)
    url = models.URLField()
    repository = models.CharField(max_length=500)
    description = RichTextUploadingField()
    image = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.name


class Skill(models.Model):
    name = models.CharField(max_length=255)
    description = RichTextUploadingField()

    def __str__(self):
        return self.name


class Language(models.Model):
    name = models.CharField(max_length=255)
    start_date = models.DateField()

    def __str__(self):
        return self.name
