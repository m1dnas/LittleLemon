from django.test import TestCase
from restaurant.models import Menu

class MenuTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title='Banana', price=100)
        self.assertEqual(str(item), 'Banana : 100')
