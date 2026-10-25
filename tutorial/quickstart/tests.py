from django.urls import reverse
from rest_framework import status 
from rest_framework.test import APITestCase
from .models import Product


class ProductAPITestCase(APITestCase):

    def setUp(self):
        self.product = Product.objects.create(
            name="Laptop",
            price="79000.87",
            description="Asus Vivobook"
        )
        self.list_url = reverse('product_list')
        self.detail_url = reverse('product_detail',kwargs={'id': self.product.id})

    def test_get_product_list(self):
        response = self.client.get(self.list_url)

        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], 'Phone')

    def test_get_product_detail(self):
        response = self.client.get(self.detail_url)

        self.assertEqual(
            response.status_code,status.HTTP_200_OK
        )
        self.assertEqual(
            response.data['id'], self.product.id
        )
        self.assertEqual(
            response.data['name'], 'Laptop'
        )

    def test_get_non_existent_product(self):
        url = reverse('product_detail', kwargs={'id': 9999})
        response = self.client.get(url)
        self.assertEqual(
            response.status_code,
            status.HTTP_404_NOT_FOUND
        )

    def test_update_product(self):
        data = { "name": "Gaming Laptop",
                "price": "85000.00",
                "description": "High performance laptop"
                }
        response = self.client.put(
            self.detail_url, data, format="json")
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_update_product_invalid_data(self):
        data = { "name": "",
                "price": "invalid",
                "description": "invalid product"
                }
        response = self.client.put(
            self.detail_url, data, format='json'
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )

    def test_delete_product(self):
        response = self.client.delete(self.detail_url)
        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )
        self.assertEqual(Product.objects.count(),0)

    def test_delete_non_existent_product(self):
        url = reverse('product_detail', kwargs={'id': 9999})
        response = self.client.delete(url)
        self.assertEqual(
            response.status_code,
            status.HTTP_404_NOT_FOUND
        )
    

        