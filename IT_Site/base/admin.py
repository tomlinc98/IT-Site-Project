from django.contrib import admin

# Register your models here.

from .models import Course, Topic, Module, Announcement, Advert, Event, Comment

admin.site.register(Course)
admin.site.register(Topic)
admin.site.register(Module)
admin.site.register(Announcement)
admin.site.register(Advert)
admin.site.register(Event)
admin.site.register(Comment)
