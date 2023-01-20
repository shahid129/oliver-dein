from django.test import TestCase
# from django.contrib.auth.models import User
from django.shortcuts import redirect
from .models import Contact
from .forms import ContactForm


class TestViews(TestCase):
    """
    Test for the views
    """

    def test_contact_page(self):
        """
        Test contact page
        """
        response = self.client.get('/contact/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact/contact.html')
