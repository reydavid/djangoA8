from django.urls import path
from .import views

app_name="courses"

urlpatterns = [
    path ('',views.index),
    path ('addcourse',views.addCourse),
    path ('removecourse/<id>/',views.removeCourse,name='removeCourse')
]