from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Parent)
admin.site.register(Student)
admin.site.register(School)
admin.site.register(Classroom)
admin.site.register(Registration)
admin.site.register(Teacher)
admin.site.register(Presence)