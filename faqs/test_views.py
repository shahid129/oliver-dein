from django.test import TestCase
from django.contrib.auth.models import User
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

    def test_delete_faqs_page(self):
        """
        Test to check if delete page redirects
        """
        self.client.login(username='admin', password='adminpassword')
        response = self.client.get(f'/faqs/delete_faqs/{self.faq.id}/')
        self.assertEqual(response.status_code, 302)

    # ----------------- End of url test

    def test_add_faqs(self):
        """
        Test if the view creates a new faqs
        """
        self.client.login(username='admin', password='adminpassword')
        # check if the form is valid
        response = self.client.post(
            '/faqs/add_faqs/', {
                'category': 'OT',
                'questions': 'Sample Question',
                'answers': 'Sample Answers'
            }, follow=True  # the client will follow the redirect
        )
        self.assertEqual(response.status_code, 200)

        message = list(response.context.get('messages'))[0]
        self.assertEqual(message.tags, "success")
        self.assertTrue("FAQs added successfully." in message.message)

    def test_edit_faqs(self):
        """
        Test if the edit view lets you edit the faqs
        """
        self.client.login(username='admin', password='adminpassword')
        # check if the form is valid
        response = self.client.post(
            f'/faqs/edit_faqs/{self.faq.id}/', {
                'category': 'OT',
                'questions': 'Sample Question',
                'answers': 'Sample Answers'
            }, follow=True  # the client will follow the redirect
        )
        self.assertEqual(response.status_code, 200)

        message = list(response.context.get('messages'))[0]
        self.assertEqual(message.tags, "success")
        self.assertTrue("FAQs updated successfully." in message.message)

    def test_delete_faqs(self):
        """
        Test if the edit view lets you edit the faqs
        """
        self.client.login(username='admin', password='adminpassword')
        response = self.client.post(
            f'/faqs/delete_faqs/{self.faq.id}/'
        )
        self.assertEqual(response.status_code, 302)

    # Superuser functionality
    def test_only_superuser_can_add(self):
        """
        Test if the edit view lets you edit the faqs
        """
        self.client.login(username='shahid', password='shahidpassword')
        response = self.client.post(
            f'/faqs/add_faqs/', follow=True
        )
        self.assertEqual(response.status_code, 200)

        message = list(response.context.get('messages'))[0]
        self.assertEqual(message.tags, "error")
        self.assertTrue(
            'Sorry! You are not authorised to do that' in message.message)

    def test_only_superuser_can_edit(self):
        """
        Test if the edit view lets you edit the faqs
        """
        self.client.login(username='shahid', password='shahidpassword')
        response = self.client.post(
            f'/faqs/edit_faqs/{self.faq.id}/', follow=True
        )
        self.assertEqual(response.status_code, 200)

        message = list(response.context.get('messages'))[0]
        self.assertEqual(message.tags, "error")
        self.assertTrue(
            'Sorry! You are not authorised to do that' in message.message)

    def test_only_superuser_can_delete(self):
        """
        Test if the edit view lets you edit the faqs
        """
        self.client.login(username='shahid', password='shahidpassword')
        response = self.client.post(
            f'/faqs/delete_faqs/{self.faq.id}/', follow=True
        )
        self.assertEqual(response.status_code, 200)

        message = list(response.context.get('messages'))[0]
        self.assertEqual(message.tags, "error")
        self.assertTrue(
            'Sorry! You are not authorised to do that' in message.message)
