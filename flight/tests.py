from django.test import Client,TestCase
from django.db.models import Max
from .models import Airport,Flight,Passengers
# Create your tests here.
class ModelsTestCase(TestCase):
    def setUp(self):
        a1=Airport.objects.create(code="dss",city="bhagalpur")
        a2=Airport.objects.create(code="ndl",city="Delhi")
        Flight.objects.create(origin=a1,destination=a2,duration=100)
        Flight.objects.create(origin=a1,destination=a1,duration=200)
        Flight.objects.create(origin=a1,destination=a2,duration=-100)

    def test_departure(self):
        a=Airport.objects.get(code="dss")
        self.assertEqual(a.departure.count(),3)

    def test_arrival(self):
        a=Airport.objects.get(code="dss")
        self.assertEqual(a.arrival.count(),1)

    def test_valid_flight(self):
        a1=Airport.objects.get(code="dss")
        a2=Airport.objects.get(code="ndl")
        f=Flight.objects.get(origin=a1,destination=a2,duration=100)
        self.assertTrue(f.is_valid_flight())

    def test_invalid_flight_destination(self):
        a1=Airport.objects.get(code="dss")
        f=Flight.objects.get(origin=a1,destination=a1)
        self.assertFalse(f.is_valid_flight())

    def test_invalid_flight_duration(self):
        a1=Airport.objects.get(code="dss")
        a2=Airport.objects.get(code="ndl")
        f=Flight.objects.get(origin=a1,destination=a2,duration=-100)
        self.assertFalse(f.is_valid_flight())
