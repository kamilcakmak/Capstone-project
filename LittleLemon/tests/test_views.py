from django.test import TestCase
from Restaurant.models import Menu
from Restaurant.views import MenuItemsView
from Restaurant.serializers import MenuSerializer
#from Restaurant.views import MenuItemsView

class MenuViewTest(TestCase):
    def setUp(self):
        Menu.objects.create(title="IceCream", price=80, inventory=100)
        #Menu.objects.create(title="IceCream", price=80, inventory=100)

    def test_getall(self):
        response = self.client.get('/restaurant/menu/', headers={'SERVER_PORT':'8000'})
        print(response.request)
        #print(response.data)
        
        # print(response.data[0])
        # m = MenuSerializer(Menu.objects.all(), many=True)
        # print(m.data)
        # print(MenuSerializer(Menu.objects.get()).data)
        self.assertEqual(response.data, MenuSerializer(Menu.objects.all(), many=True).data)

    def test2(self):
        response = self.client.get('/restaurant/', headers={'SERVER_PORT':'8000'})

    
    