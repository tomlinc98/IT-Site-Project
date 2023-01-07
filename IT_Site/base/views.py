from django.shortcuts import render
from django.db.models import Q
from .models import Course, Topic, Module

# Create your views here.


def home(request):
    pk = [1, 2, 3]
    courses = Course.objects.filter(id__in=pk)
    context = {f'course{i}': course for i,
               course in enumerate(courses, start=1)}
    return render(request, 'base/home.html', context)


def about(request):
    return render(request, 'base/about.html')


def all_courses(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''

    # Search params - course topic, title, description
    courses = Course.objects.filter(
        Q(topic__name__icontains=q) |
        Q(title__icontains=q) |
        Q(description__icontains=q)
    )

    topics = Topic.objects.all()
    course_count = courses.count()

    context = {'courses': courses, 'topics': topics,
               'course_count': course_count}
    return render(request, 'base/all_courses.html', context)


def course(request, pk):
    course = Course.objects.get(id=pk)
    modules = course.module_set.all()
    context = {
        'course': course,
        'modules': modules,
    }
    return render(request, 'base/course.html', context)


def module(request, pk):
    module = Module.objects.get(id=pk)
    context = {
        'module': module}
    return render(request, 'base/module.html', context)


def faq(request):
    return render(request, 'base/faq.html')
