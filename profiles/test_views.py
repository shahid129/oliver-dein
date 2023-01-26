from django.test import TestCase
from django.contrib.auth.models import User
from django.shortcuts import redirect
from .models import UserProfile


class TestViews(TestCase):
    """
    Test for the views
    """

    def setUp(self):
        self.user = User.objects.create_user(
            'shahid', 'shahid@email.com', 'shahidpassword'
        )

    def test_profile_page(self):
        """
        Test if the profile page loads
        """
        self.client.login(username='shahid', password='shahidpassword')
        response = self.client.get('/profile/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/profile.html')
