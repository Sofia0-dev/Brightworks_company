from django.test import TestCase
from django.urls import reverse
from .models import Service, Employee


class PageTests(TestCase):
    def test_pages_load(self):
        for name in ['home', 'about', 'services', 'employees']:
            response = self.client.get(reverse(name))
            self.assertEqual(response.status_code, 200, name)

    def test_seed_data(self):
        self.assertEqual(Employee.objects.count(), 30)
        self.assertEqual(Service.objects.count(), 6)
        self.assertEqual(Employee.objects.values('email').distinct().count(), 30)
        for e in Employee.objects.all():
            self.assertTrue(21 <= e.age <= 60)
            self.assertIn('@', e.email)

    def test_employee_page_shows_data(self):
        first = Employee.objects.order_by('name').first()
        self.assertContains(self.client.get(reverse('employees')), first.email)
