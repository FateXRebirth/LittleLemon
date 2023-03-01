from django.test import TestCase
from restaurant.models import Menu

class MenuViewTest(TestCase):
    def setUp(self):
        Menu.objects.create(Title="IceCream", Price=80, Inventory=100)
        Menu.objects.create(Title="Cake", Price=120, Inventory=50)
    
    def test_getall(self):
        items = Menu.objects.all()
        self.assertEqual(items[0], Menu.objects.get(Title="IceCream"))
        self.assertEqual(items[1], Menu.objects.get(Title="Cake"))