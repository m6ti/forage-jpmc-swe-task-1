import unittest

from client3 import getDataPoint, getRatio


class TestStockFunctions(unittest.TestCase):

    def test_getDataPoint(self):
        # Arrange: Simulated test case with bid price less than ask price
        quote = {
            'stock': 'AAPL',
            'top_bid': {'price': 120.48},
            'top_ask': {'price': 120.74}
        }
        expected_tuple = ('AAPL', 120.48, 120.74, (120.48 + 120.74) / 2)

        # Act: Call the function with the quote
        result = getDataPoint(quote)

        # Assert: Check if the result matches the expected tuple
        self.assertEqual(result, expected_tuple)

    def test_calculatePriceBidGreaterThanAsk(self):
        # Arrange: Simulated test case with bid price greater than ask price
        quote = {
            'stock': 'GOOG',
            'top_bid': {'price': 1500.01},
            'top_ask': {'price': 1499.99}
        }
        expected_tuple = ('GOOG', 1500.01, 1499.99, (1500.01 + 1499.99) / 2)

        # Act: Call the function with the quote
        result = getDataPoint(quote)

        # Assert: Check if the result matches the expected tuple
        self.assertEqual(result, expected_tuple)

    def test_getRatio(self):
        # Arrange: Two valid prices where price_b is not zero
        price_a = 120.74
        price_b = 120.48

        # Act: Call the function
        result = getRatio(price_a, price_b)

        # Assert: Check if the result is correct
        self.assertEqual(result, price_a / price_b)

    def test_getRatio_priceBZero(self):
        # Arrange: Price B is zero, which should return None
        price_a = 120.74
        price_b = 0

        # Act: Call the function
        result = getRatio(price_a, price_b)

        # Assert: Check if the result is None
        self.assertIsNone(result)

    def test_getRatio_priceAZero(self):
        # Arrange: Price A is zero, and Price B is non-zero
        price_a = 0
        price_b = 120.48

        # Act: Call the function
        result = getRatio(price_a, price_b)

        # Assert: Check if the result is zero
        self.assertEqual(result, 0)


if __name__ == '__main__':
    unittest.main()