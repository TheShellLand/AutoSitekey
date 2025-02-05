import unittest

from autositekey import AutoSiteKeyClient

test = AutoSiteKeyClient()


class MyTestCase(unittest.TestCase):
    def test(self):
        if test.is_ready():
            test.run(headless=True)


if __name__ == '__main__':
    unittest.main()
    test.browser.quit()
