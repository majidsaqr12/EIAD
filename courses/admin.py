from django.contrib import admin
from .models import Category, Course, Registration
from import_export.admin import ImportExportModelAdmin

@admin.register(Category)
class CategoryAdmin(ImportExportModelAdmin):
    pass

@admin.register(Course)
class CourseAdmin(ImportExportModelAdmin):
    pass

@admin.register(Registration)
class RegistrationAdmin(ImportExportModelAdmin):
    pass

admin.site.site_header = "EIAD administration"
