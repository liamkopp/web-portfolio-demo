from django.contrib import admin

# Register your models here.
from portfolio.models import Project, Type

admin.site.register(Project)
admin.site.register(Type)