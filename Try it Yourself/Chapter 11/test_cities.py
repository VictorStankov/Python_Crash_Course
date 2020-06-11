import unittest
import city_functions


class CityCountryTest(unittest.TestCase):
    def test_city_country(self):
        a = city_functions.city_country('sofia', 'bulgaria')
        self.assertEqual(a, "Sofia, Bulgaria")

    def test_city_country_pop(self):
        b = city_functions.city_country('sofia', 'bulgaria', 2000000)
        self.assertEqual(b, "Sofia, Bulgaria - population 2000000")


if __name__ == '__main__':
    unittest.main()
