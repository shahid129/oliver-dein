from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Product


class ProductDetailTestViews(TestCase):
    """
    Test for the views
    """

    def setUp(self):
        self.product = Product.objects.create(
            name='Test Item',
            slug='test-item',
            price=30.00,
            rating=3.3,
        )

        self.superuser = User.objects.create_superuser(
            'admin', 'admin@email.com', 'adminpassword'
        )

        self.user = User.objects.create_user(
            'shahid', 'shahid@email.com', 'shahidpassword'
        )

    def test_products_page(self):
        """
        Test if products page loads
        """
        response = self.client.get('/products/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')

    def test_product_detail(self):
        """
        Test if product detail page loads
        """
        response = self.client.get(reverse(
            'product_detail', args=[self.product.slug])
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/product_detail.html')

    def test_add_product(self):
        """
        Test if add product page loads
        """

        self.client.login(username='admin', password='adminpassword')
        response = self.client.get('/products/add_product/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/add_products.html')

    def test_edit_product(self):
        """
        Test if edit product page loads
        """

        self.client.login(username='admin', password='adminpassword')
        response = self.client.get(reverse(
            'edit_product', args=[self.product.slug])
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/edit_products.html')

    def test_delete_product(self):
        """
        Test if delete product page loads
        """

        self.client.login(username='admin', password='adminpassword')
        response = self.client.get(reverse(
            'delete_product', args=[self.product.slug])
        )
        self.assertEqual(response.status_code, 302)

    # Superuser functionalities
    def test_only_superuser_can_add(self):
        """
        Test if the edit view lets you add the products
        Only admin can add products
        """
        self.client.login(username='shahid', password='shahidpassword')
        response = self.client.post(
            f'/products/add_product/', follow=True
        )
        self.assertEqual(response.status_code, 200)

        message = list(response.context.get('messages'))[0]
        self.assertEqual(message.tags, "error")
        self.assertTrue(
            'Sorry! Only store owners are allowed here.' in message.message
        )

    def test_only_superuser_can_edit(self):
        """
        Test if the edit view lets you edit the products
        Only admin can edit products
        """
        self.client.login(username='shahid', password='shahidpassword')
        response = self.client.get(reverse(
            'edit_product', args=[self.product.slug]), follow=True)

        self.assertEqual(response.status_code, 200)

        message = list(response.context.get('messages'))[0]
        self.assertEqual(message.tags, "error")
        self.assertTrue(
            'Sorry! Only store owners are allowed here.' in message.message
        )

    def test_only_superuser_delete_edit(self):
        """
        Test if the delete view lets you delete the products
        Only admin can delete products
        """
        self.client.login(username='shahid', password='shahidpassword')
        response = self.client.get(reverse(
            'delete_product', args=[self.product.slug]), follow=True)

        self.assertEqual(response.status_code, 200)

        message = list(response.context.get('messages'))[0]
        self.assertEqual(message.tags, "error")
        self.assertTrue(
            'Sorry! Only store owners are allowed here.' in message.message
        )
