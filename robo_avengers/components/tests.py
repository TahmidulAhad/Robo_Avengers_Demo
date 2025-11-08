from django.test import TestCase
from .models import Component

class ComponentModelTest(TestCase):

    def setUp(self):
        Component.objects.create(name="Test Component", description="A component for testing.")

    def test_component_creation(self):
        component = Component.objects.get(name="Test Component")
        self.assertEqual(component.description, "A component for testing.")

    def test_component_str(self):
        component = Component.objects.get(name="Test Component")
        self.assertEqual(str(component), "Test Component")