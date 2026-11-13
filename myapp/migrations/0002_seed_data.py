import datetime
import random

from django.db import migrations

FIRST = ['Amina', 'Brian', 'Chloe', 'Daniel', 'Esther', 'Farid', 'Grace', 'Hassan',
         'Irene', 'James', 'Khadija', 'Liam', 'Maya', 'Noah', 'Olivia', 'Peter',
         'Qadir', 'Rahma', 'Samuel', 'Tasha', 'Umar', 'Violet', 'Wanjiru', 'Yusuf']
LAST = ['Abdi', 'Banda', 'Carter', 'Dlamini', 'Evans', 'Farah', 'Gitau', 'Hussein',
        'Ismail', 'Juma', 'Kamau', 'Lopez', 'Mwangi', 'Nguyen', 'Otieno', 'Patel']
JOBS = {
    'Finance': ['Accountant', 'Financial Analyst', 'Payroll Officer'],
    'HR': ['HR Officer', 'Recruiter', 'Training Coordinator'],
    'IT': ['Software Developer', 'Data Analyst', 'Systems Administrator'],
    'Marketing': ['Marketing Executive', 'Content Creator', 'Brand Manager'],
    'Operations': ['Operations Officer', 'Logistics Coordinator', 'Project Manager'],
    'Sales': ['Sales Representative', 'Account Manager', 'Sales Analyst'],
}
SERVICES = [
    ('Web Development', '1200.00', 'Custom websites built with Django and Bootstrap.'),
    ('Data Analysis', '800.00', 'Cleaning, analysing and reporting on your business data.'),
    ('Dashboard Design', '650.00', 'Interactive dashboards that make your numbers easy to read.'),
    ('IT Support', '150.00', 'Fast help with hardware, software and network problems.'),
    ('Staff Training', '400.00', 'Hands-on workshops for Excel, SQL and Python.'),
    ('Consulting', '300.00', 'One-on-one sessions to plan your next digital project.'),
]


def seed(apps, schema_editor):
    Employee = apps.get_model('myapp', 'Employee')
    Service = apps.get_model('myapp', 'Service')
    rng = random.Random(42)

    names = set()
    while len(names) < 30:
        names.add((rng.choice(FIRST), rng.choice(LAST)))

    people = []
    for first, last in sorted(names):
        dept = rng.choice(sorted(JOBS))
        people.append(Employee(
            name=f'{first} {last}',
            email=f'{first.lower()}.{last.lower()}@example.com',
            age=rng.randint(21, 60),
            department=dept,
            job_title=rng.choice(JOBS[dept]),
            salary=rng.randrange(40000, 120001, 500),
            hire_date=datetime.date(2015, 1, 1) + datetime.timedelta(days=rng.randrange(0, 3900)),
        ))
    Employee.objects.bulk_create(people)

    Service.objects.bulk_create(
        [Service(name=n, price=p, description=d) for n, p, d in SERVICES]
    )


def unseed(apps, schema_editor):
    apps.get_model('myapp', 'Employee').objects.all().delete()
    apps.get_model('myapp', 'Service').objects.all().delete()


class Migration(migrations.Migration):
    dependencies = [('myapp', '0001_initial')]
    operations = [migrations.RunPython(seed, unseed)]
