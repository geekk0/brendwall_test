import requests
import unittest


class TestProductsAPI(unittest.TestCase):
    def test_get_products(self):
        url = 'http://127.0.0.1:8000/api/products/'
        response = requests.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)

    def test_get_products_invalid_url(self):
        url = 'http://127.0.0.1:8000/api/invalid-url/'
        response = requests.get(url)

        self.assertEqual(response.status_code, 404)

    def test_post_product(self):
        url = 'http://127.0.0.1:8000/api/products/'
        data = {
            'name': 'Test Product',
            'description': 'This is a test product',
            'price': 9.99
        }
        response = requests.post(url, json=data)

        self.assertEqual(response.status_code, 201)
        self.assertIsInstance(response.json(), dict)
        self.assertEqual(response.json()['name'], data['name'])
        self.assertEqual(response.json()['description'], data['description'])
        self.assertEqual(float(response.json()['price']), data['price'])

    def test_post_product_validation(self):
        url = 'http://127.0.0.1:8000/api/products/'
        data = {
            'name': '',  # empty string
            'description': 'This is a test product',
            'price': 9.99
        }
        response = requests.post(url, json=data)

        self.assertEqual(response.status_code, 400)
        self.assertIsInstance(response.json(), dict)
        self.assertIn('name', response.json())

        data = {
            'name': 'Test Product',
            'description': '',  # empty string
            'price': 9.99
        }
        response = requests.post(url, json=data)

        self.assertEqual(response.status_code, 201)
        self.assertIsInstance(response.json(), dict)
        self.assertIn('description', response.json())

        data = {
            'name': 'Test Product',
            'description': 'This is a test product',
            'price': -1.0  # invalid price
        }
        response = requests.post(url, json=data)

        self.assertEqual(response.status_code, 400)
        self.assertIsInstance(response.json(), dict)
        self.assertIn('price', response.json())

        data = {
            'name': 'Test Product',
            'description': 'This is a test product',
            'price': ''  # invalid price
        }
        response = requests.post(url, json=data)

        self.assertEqual(response.status_code, 400)
        self.assertIsInstance(response.json(), dict)
        self.assertIn('price', response.json())


if __name__ == '__main__':
    unittest.main()