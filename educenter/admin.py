from django.contrib import admin

from .models import (
        About, Blog, Course, Event, 
        FunFact, Interest, Notice, Research, 
        Requirement, School, Scholarship, Teacher
    )

# Register your models here.
admin.site.register([
        About, Blog, Course,  Event, 
        FunFact, Interest, Notice, Research, 
        Requirement, School, Scholarship, Teacher
    ])