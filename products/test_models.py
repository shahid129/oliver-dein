from django.test import TestCase
from .models import Category, Product, Comment


class TestModels(TestCase):
    """
    Test the models
    """

    def test_category(self):
        """
        Test if the model returns a string
        """
        category = Category.objects.create(name='Test Name')
        self.assertEqual(str(category), 'Test Name')

    def test_product(self):
        """
        Test if the product model returns a string
        """
        product = Product.objects.create(
            name='Test Name',
            price='22',
            rating='2.2'
        )
        self.assertEqual(str(product), 'Test Name')
