from django.test import TestCase
from .models import Faqs


class TestViews(TestCase):
    """
    Test for the views
    """
    def test_faqs(self):
        response = self.client.get('/faqs/')
        self.assertEqual(response.status_code, 200)
        self. assertTemplateUsed(response, 'faqs/faqs.html')