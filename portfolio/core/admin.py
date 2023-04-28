from django.contrib import admin
from core.models import Project

# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
    pass

admin.site.register(Project, ProjectAdmin)

