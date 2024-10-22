import unittest

from autositekey import AutoSiteKeyClient


class MyTestCase(unittest.TestCase):
    def test(self):
        test = AutoSiteKeyClient()

        if test.is_ready():
            test.run(headless=False)


if __name__ == '__main__':
    unittest.main()
