import datetime
from django.test import TestCase
from Restaurant.models import Menu, Booking

class MenuTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="IceCream", price=80, inventory=100)
        self.assertEqual(item.__str__(), "IceCream : 80")

class BookingTest(TestCase):
    def test_get_item(self):
        item = Booking.objects.create(name="test", no_of_quests=80, bookingdate=datetime.date(2023, 10, 7))
        self.assertEqual(item.__str__(), "test")
