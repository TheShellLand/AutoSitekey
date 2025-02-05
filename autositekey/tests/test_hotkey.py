import unittest

from autositekey import AutoSiteKeyClient

test = AutoSiteKeyClient()


class MyTestCase(unittest.TestCase):
    def test(self):

        test.run(headless=True)


if __name__ == '__main__':
    unittest.main()
    test.browser.quit()
