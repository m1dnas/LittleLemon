from django.test import TestCase, Client
from django.urls import reverse
from .models import Menu
from .serializers import MenuSerializer
import json

class MenuTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title='Banana', price=100, inventory=1)
        self.assertEqual(str(item), 'Banana : 100')

class MenuViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.menu1 = Menu.objects.create(title='Banana', price=100, inventory=1)
        self.menu2 = Menu.objects.create(title='Apple', price=120, inventory=1)
    
    def test_getall(self):
        expected_data = MenuSerializer([self.menu1, self.menu2], many=True).data

        response = self.client.get('menu')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, expected_data)

        serialized_data = MenuSerializer([self.menu1, self.menu2], many=True).data
        self.assertEqual(serialized_data, expected_data)
