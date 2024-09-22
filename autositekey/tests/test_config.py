import unittest

from autositekey import AutoSiteKeyClient


class MyTestCase(unittest.TestCase):
    def test(self):
        test = AutoSiteKeyClient()
        if test.run(headless=False):
            pass


if __name__ == '__main__':
    unittest.main()
