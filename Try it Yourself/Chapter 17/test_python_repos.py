import unittest
from python_repos import link


class NamesTestCase(unittest.TestCase):
    def test_status_code(self):
        temp = link('https://api.github.com/search/repositories?q=language:python&sort=stars')
        self.assertEqual(temp, 200)


if __name__ == '__main__':
    unittest.main()