import unittest

from autositekey.client import AutoSiteKeyClient

test = AutoSiteKeyClient()


class MyTestCase(unittest.TestCase):
    def test(self):
        if test.is_ready(headless=True):
            self.assertTrue(test.get('https://1.1.1.1'))


if __name__ == '__main__':
    unittest.main()
    test.browser.quit()
