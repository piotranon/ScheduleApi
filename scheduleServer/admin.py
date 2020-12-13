from django.contrib import admin
from .models import Lecturer,Lecture,FieldOfStudy,Building,Specialization,Groups

admin.site.register([Lecturer,Lecture,FieldOfStudy,Building,Specialization,Groups])