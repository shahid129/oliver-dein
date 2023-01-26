from django.test import TestCase
from .models import Contact, Address


class TestModels(TestCase):
    """
    Test for models
    """

    def test_if_contact_model_returns_a_string(self):
        """
        Test to see if it returns a string
        """
        contact = Contact.objects.create(
            topic='OR',
            name='shahid',
            email='shahid@mail.com',
            phone='123',
            message='Test Message'
        )
        self.assertEqual(str(contact), 'Message from shahid')

    def test_if_address_model_returns_a_string(self):
        """
        Test to see if it returns a string
        """
        address = Address.objects.create(
            address='Test Address',
            phone='123',
            email='shahid@mail.com',
        )
        self.assertEqual(str(address), 'Test Address')
