from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

# Create your models here.

class School(models.Model):
    admin = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"

class Classroom(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    level = models.CharField(max_length=5)
    cycle = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.level} {self.cycle}"

class Person(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    post_name = models.CharField(max_length=25)
    address = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        abstract = True

def add_user_to_group(user_name, group_name):
    user = User.objects.get(username=user_name)
    group = Group.objects.get(name=group_name)
    user.groups.add(group)

def create_user_from_teacher(user_name):
    try:
        User.objects.get(username=user_name)
    except:
        User.objects.create_user(username=user_name, password="12345678")
        add_user_to_group(user_name, "Teacher")


class Teacher(Person):
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    email = models.CharField(max_length=25)
    phone = models.CharField(max_length=15)

    def save(self, *args, **kwargs):
        username = self.last_name.lower() + "." + self.post_name.lower()
        create_user_from_teacher(username)
        super().save(*args, **kwargs)

class Parent(Person):
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    email = models.CharField(max_length=25)
    phone = models.CharField(max_length=15)

class Student(Person):
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE)
    birth_date = models.DateField()

class Registration(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    school_year = models.CharField(max_length=10)

    def __str__(self):
        classroom_infos = self.classroom.level + " " + self.classroom.cycle
        return f"{self.student.last_name} => {classroom_infos}"

class Presence(models.Model):
    school = models.ForeignKey(School,on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)
    is_present = models.BooleanField()

    def __str__(self):
        return f"{self.student.last_name}, {self.date}"