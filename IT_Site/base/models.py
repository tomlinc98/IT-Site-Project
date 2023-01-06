from django.db import models

# Create your models here.


class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Course(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    requirements = models.TextField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)  # last update
    course_img = models.ImageField(
        upload_to="static/course", height_field=None, width_field=None, max_length=100, null=True, blank=True)

    def __str__(self):
        return self.title


class Module(models.Model):
    course = models.ManyToManyField(Course)
    code = models.CharField(max_length=200, unique=True)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    module_img = models.ImageField(
        upload_to="static/module", height_field=None, width_field=None, max_length=100, null=True, blank=True)
    staff_img = models.ImageField(
        upload_to="static/staff", height_field=None, width_field=None, max_length=100, null=True, blank=True)
    staff_name = models.CharField(max_length=200)

    def __str__(self):
        return self.title
