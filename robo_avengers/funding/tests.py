from django.test import TestCase
from .models import Funding

class FundingModelTest(TestCase):

    def setUp(self):
        Funding.objects.create(name="Test Funding", amount=1000)

    def test_funding_creation(self):
        funding = Funding.objects.get(name="Test Funding")
        self.assertEqual(funding.amount, 1000)

    def test_funding_str(self):
        funding = Funding.objects.get(name="Test Funding")
        self.assertEqual(str(funding), "Test Funding")