from django.contrib import admin

# Register your models here.

from .models import Course, Topic, Module

admin.site.register(Course)
admin.site.register(Topic)
admin.site.register(Module)
