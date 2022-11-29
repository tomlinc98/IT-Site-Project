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
    updated = models.DateTimeField(auto_now=True) # last post update

    def __str__(self):
        return self.title

class Module(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    code = models.CharField(max_length=200, unique=True)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    staff_img = models.ImageField(upload_to="static/staff", height_field=None, width_field=None, max_length=100)
    staff_name = models.CharField(max_length=200)

    def __str__(self):
        return self.title

