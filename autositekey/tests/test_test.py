import unittest

from autositekey.client import AutoSiteKeyClient
from autositekey import *


class MyTestCase(unittest.TestCase):

    def test(self):
        TEST = Hotkey()
        TEST._TEST = Click('Phone number, username, or email')

        TEST.run(headless=True)

        TEST.get('https://www.instagram.com/', delay_on_load=3)

        self.assertTrue(TEST.test())

        pass


if __name__ == '__main__':
    unittest.main()
