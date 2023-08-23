from automon.log import Logging
from automon.integrations.seleniumWrapper import SeleniumBrowser

from .config import AutoSiteKeyConfig

log = Logging(name='AutoSiteKeyClient', level=Logging.DEBUG)


class AutoSiteKeyClient(object):
    """A way to configure website behaviors to auto hotkey to anything"""

    def __init__(self, **kwargs):
        self.browser = SeleniumBrowser()
        self._config = AutoSiteKeyConfig(**kwargs)

    @property
    def config(self):
        return self._config

    def run(self, headless: bool = True):
        if headless:
            self.browser.config.set_webdriver.Chrome().in_headless()

        self.browser.config.set_webdriver.Chrome().run()
        return self
