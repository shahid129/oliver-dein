from django.test import TestCase
from .forms import ProductForm, CommentForm


class TestForm(TestCase):
    """
    Test the form
    """

    def test_product_form(self):
        """
        Test if all the fields are displayed in the form
        """
        form = ProductForm()
        self.assertEqual(form.Meta.fields, '__all__')

    def test_item_is_required_product_form(self):
        """
        Check if following fields field are required
        """
        form = ProductForm({
            'name': '',
            'description': '',
            'price': '',
        })
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors.keys())
        self.assertIn('description', form.errors.keys())
        self.assertIn('price', form.errors.keys())
        self.assertEqual(
            form.errors['name'][0], 'This field is required.')
        self.assertEqual(
            form.errors['description'][0], 'This field is required.')
        self.assertEqual(
            form.errors['price'][0], 'This field is required.')

    def test_item_is_required_product_form(self):
        """
        Check if following fields field are required
        """
        form = CommentForm({
            'name': '',
            'body': '',
        })
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors.keys())
        self.assertIn('body', form.errors.keys())
        self.assertEqual(
            form.errors['name'][0], 'This field is required.')
        self.assertEqual(
            form.errors['body'][0], 'This field is required.')
