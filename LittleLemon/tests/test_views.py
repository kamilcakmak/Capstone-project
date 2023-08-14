import datetime
from django.test import TestCase
from Restaurant.models import Menu, Booking
from Restaurant.serializers import MenuSerializer, BookingSerializer

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

class BookingViewTest(TestCase):
    def setUp(self):
        Booking.objects.create(name="test", no_of_quests=80, bookingdate=datetime.date(2023, 10, 7))

    def test_getall(self):
        response = self.client.get('/restaurant/booking/', headers={'SERVER_PORT':'8000'})
        self.assertEqual(response.data, BookingSerializer(Booking.objects.all(), many=True).data)

    
    