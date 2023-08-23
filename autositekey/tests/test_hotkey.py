import unittest

from autositekey import AutoSiteKeyClient


class MyTestCase(unittest.TestCase):
    def test_something(self):
        test = AutoSiteKeyClient()
        test.run(headless=False)
        pass


if __name__ == '__main__':
    unittest.main()
