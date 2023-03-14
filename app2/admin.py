from django.contrib import admin
from app2.models import *
# # Register your models here.
admin.site.register([Employee, College, Principal, Department, Student, Subject])