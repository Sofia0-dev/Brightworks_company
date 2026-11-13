from django.db import models


class Service(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    age = models.PositiveIntegerField()
    department = models.CharField(max_length=50)
    job_title = models.CharField(max_length=100)
    salary = models.PositiveIntegerField()
    hire_date = models.DateField()

    def __str__(self):
        return self.name
