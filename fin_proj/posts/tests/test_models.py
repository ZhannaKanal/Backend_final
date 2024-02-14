from django.test import TestCase
from django.test import TestCase
from posts.models import Price, InfoTravel
from django.urls import reverse, resolve
class PriceModelTestcase(TestCase):
    @classmethod
    def setUpTestData(cls):
        Price.objects.create(kala= "Shymkent")
    def test_string_method(self):
        price = Price.objects.get(id=1)
        expected_string = f"{price.kala}"
        self.assertEqual(str(price), expected_string)
        
    def test_get_absolute_url(self):
        price = Price.objects.get(id=1)
        self.assertEqual(20000, price.price)
    
class InfoTravelModelTestcase(TestCase):
    @classmethod
    def setUpTestData(cls):
        InfoTravel.objects.create(name = "Aksu")
    def test_string_method(self):
        profile = InfoTravel.objects.get(id=1)
        expected_object_name = f"{profile.name}"
        self.assertEqual(str(profile), expected_object_name)
        
    def test_climate_max_length(self):
        profile = InfoTravel.objects.get(id=1)
        max_length = profile._meta.get_field('climate').max_length
        self.assertEqual(max_length, 255)

    def test_flora_max_length(self):
        profile = InfoTravel.objects.get(id=1)
        max_length = profile._meta.get_field('flora').max_length
        self.assertEqual(max_length, 255)

#from posts.views import send_message
