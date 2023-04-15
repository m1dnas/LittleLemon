from django.test import TestCase, Client
from django.urls import reverse
from restaurant.models import Menu
import json

class MenuViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.menu1 = Menu.objects.create(title='Banana', price=100)
        self.menu2 = Menu.objects.create(title='Apple', price=120)
    
    def test_getall(self):
        response = self.client.get(reverse('menu-list'))
        menus = Menu.objects.all()
        serialized_data = json.dumps([{'name': menu.name, 'description': menu.description} for menu in menus])
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, serialized_data.encode('utf-8'))
