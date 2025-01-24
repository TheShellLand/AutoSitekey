import unittest

from autositekey.client import AutoSiteKeyClient
from autositekey import *


class MyTestCase(unittest.TestCase):

    def test(self):

        TEST = Hotkey()

        TEST.run(headless=True)

        TEST.get('https://mapgenie.io/tarkov/maps/customs')

        TEST._TEST = Click(
            '//*[@id="left-sidebar"]/div[2]/div[3]/a[2]'
        )

        TEST.test()

        pass


if __name__ == '__main__':
    unittest.main()
