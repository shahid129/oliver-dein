from django.test import TestCase
from django.contrib.auth.models import User
from django.shortcuts import redirect
from .models import Faqs


class TestViews(TestCase):
    """
    Test for the views
    """
    # ----------------- Test all the urls
    def setUp(self):
        self.superuser = User.objects.create_superuser(
            'admin', 'admin@email.com', 'adminpassword'
        )
        
        self.user = User.objects.create_user(
            'shahid', 'shahid@email.com', 'shahidpassword'
        )

        self.faq = Faqs.objects.create(
            category='OR',
            questions='sample question',
            answers='sample answers'
        )

    def test_faqs_page(self):
        """
        Test faqs page
        """
        response = self.client.get('/faqs/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'faqs/faqs.html')

    def test_add_faqs_page(self):
        """
        Test if the add_faqs page loads
        """
        self.client.login(username='admin', password='adminpassword')
        response = self.client.get('/faqs/add_faqs/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'faqs/add_faqs.html')

    def test_edit_faqs_page(self):
        """
        Test if the edit page loads
        """
        self.client.login(username='admin', password='adminpassword')
        response = self.client.get(f'/faqs/edit_faqs/{self.faq.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'faqs/edit_faqs.html')
