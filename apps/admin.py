from django.contrib import admin
from .models import Subject, Student, Books


# Register your models here.

class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'number_credits')


class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'last_name')


admin.site.register(Subject, SubjectAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Books)
