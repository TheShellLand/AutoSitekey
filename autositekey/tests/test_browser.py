import unittest

from autositekey.client import AutoSiteKeyClient


class MyTestCase(unittest.TestCase):
    def test_something(self):
        c = AutoSiteKeyClient()
        c.run(headless=False)
        self.assertTrue(c)


if __name__ == '__main__':
    unittest.main()
