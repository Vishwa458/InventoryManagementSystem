from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

# Register your models here.
from .models import *


@admin.register(desktop, laptop, mouse, pendrive, disk)
class ViewAdmin(ImportExportModelAdmin):
    pass
