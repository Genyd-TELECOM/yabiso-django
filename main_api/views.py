from django.shortcuts import render
from .models import *
from rest_framework import viewsets
from .serializers import *

# Create your views here.

def id_school_from_user(user_name):
    names = user_name.split(".")

    if len(names) == 1:
        user = User.objects.get(username=names[0])
        return user.school_set.all()[0]

    last_name = names[0].capitalize()
    post_name = names[1].capitalize()

    teacher = Teacher.objects.get(last_name=last_name, post_name=post_name)
    return teacher.school

class ParentViewSet(viewsets.ModelViewSet):
    serializer_class = ParentSerializer
    def get_queryset(self):
        user_name = self.request.user.username
        return Parent.objects.filter(school=id_school_from_user(user_name))


class StudentViewSet(viewsets.ModelViewSet):
    serializer_class = StudentSerializer
    def get_queryset(self):
        user_name = self.request.user.username
        return Student.objects.filter(school=id_school_from_user(user_name))

class SchoolViewSet(viewsets.ModelViewSet):
    serializer_class = SchoolSerializer
    def get_queryset(self):
        user_name = self.request.user.username
        return School.objects.filter(name=id_school_from_user(user_name).name)

class ClassroomViewSet(viewsets.ModelViewSet):
    serializer_class = ClassroomSerializer
    def get_queryset(self):
        user_name = self.request.user.username
        return Classroom.objects.filter(school=id_school_from_user(user_name))

class RegistrationViewSet(viewsets.ModelViewSet):
    serializer_class = RegistrationSerializer
    def get_queryset(self):
        user_name = self.request.user.username
        return Registration.objects.filter(school=id_school_from_user(user_name))

class TeacherViewSet(viewsets.ModelViewSet):
    serializer_class = TeacherSerializer
    def get_queryset(self):
        user_name = self.request.user.username
        return Teacher.objects.filter(school=id_school_from_user(user_name))

class PresenceViewSet(viewsets.ModelViewSet):
    serializer_class = PresenceSerializer
    def get_queryset(self):
        user_name = self.request.user.username
        return Presence.objects.filter(school=id_school_from_user(user_name))