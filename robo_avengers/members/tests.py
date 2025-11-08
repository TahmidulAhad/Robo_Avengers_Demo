from django.test import TestCase
from .models import Member

class MemberModelTest(TestCase):

    def setUp(self):
        Member.objects.create(name="Test Member", email="test@example.com")

    def test_member_creation(self):
        member = Member.objects.get(name="Test Member")
        self.assertEqual(member.email, "test@example.com")