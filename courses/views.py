from django.shortcuts import render, redirect
from .models import Course

# Create your views here.

def index(request):
    context = {
        'allCourses': Course.objects.all()
    }
    return render(request, "courses/index.html", context)

def addCourse(request):
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
#       print(request.POST['name'])
        course = Course.objects.create(name=name,description=description)
        print(course)

    return redirect("/")

def removeCourse(request, id):
    Course.objects.get(id=id).delete()
    #course.delete()

    return redirect("/")
