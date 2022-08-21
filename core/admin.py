from django.contrib import admin
from .models import (
    Project,
    ProjectType,
)


admin.site.register([
    Project,
    ProjectType,
])