from django.db.models import Avg, Count
from django.shortcuts import render
from .models import Service, Employee


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def services(request):
    return render(request, 'services.html', {'services': Service.objects.all()})


def employees(request):
    people = Employee.objects.order_by('name')
    stats = people.aggregate(total=Count('id'), avg_age=Avg('age'), avg_salary=Avg('salary'))
    return render(request, 'employees.html', {'employees': people, 'stats': stats})
