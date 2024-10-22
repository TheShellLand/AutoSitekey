import unittest

from autositekey.client import AutoSiteKeyClient


class MyTestCase(unittest.TestCase):
    def test(self):
        test = AutoSiteKeyClient()
        if test.is_ready():
            self.assertTrue(test.get('https://1.1.1.1'))


if __name__ == '__main__':
    unittest.main()
