from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import Person

@admin.register(Person)
class PersonAdmin(ImportExportModelAdmin):
    list_display = ('id','name', 'login_id', 'location')