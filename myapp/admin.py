from django.contrib import admin
from .models import Service, Employee


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    search_fields = ('name',)


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'age', 'department', 'job_title', 'salary', 'hire_date')
    list_filter = ('department',)
    search_fields = ('name', 'email')
