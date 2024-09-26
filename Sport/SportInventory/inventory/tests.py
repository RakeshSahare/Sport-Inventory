from django.test import TestCase
from rest_framework.test import APIClient
from .models import Equipments
# Create your tests here.

class EquipmentsTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.equipment = Equipments.objects.create(
            name="Bat",
            brand="Nike",
            quantity=0,
            price=50.00
        )

    def test_create_equipments(self):
        data = {
            "name": "Football",
            "brand": "Adidas",
            "quantity": 10,
            "price": 250.00
        }
        response = self.client.post("/equipment/create/", data, format="json")
        self.assertEqual(response.status_code, 200)

    def test_update_quantity(self):
        data = {"quantity": 0}
        response = self.client.patch(f"/equipment/{self.equipment.id}/update_quantity/", data, format="json")
        self.assertEqual(response.status_code, 200)

    def test_get_unavailable_items(self):
        response = self.client.get("/equipment/unavailable/")
        self.assertEqual(response.status_code, 200)