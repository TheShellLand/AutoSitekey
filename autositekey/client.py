from automon import logging
from automon.integrations.seleniumWrapper import SeleniumBrowser
from automon.integrations.seleniumWrapper.webdriver_chrome import ChromeWrapper
from automon.integrations.seleniumWrapper.user_agents import SeleniumUserAgentBuilder

from .config import AutoSiteKeyConfig

log = logging.getLogger(__name__)
log.setLevel(level=logging.DEBUG)


class AutoSiteKeyClient(object):
    """A way to configure website behaviors to auto hotkey to anything"""

    def __init__(self, **kwargs):
        self.browser = SeleniumBrowser()
        self.config = AutoSiteKeyConfig(**kwargs)

    def __repr__(self):
        return f'{self.__dict__}'

    def get(self, url: str):
        return self.browser.get(url=url)

    def is_ready(self) -> bool:
        if self.config.is_ready() and self.run():
            return True
        return False

    def run(self, headless: bool = True):
        self.browser.config.webdriver_wrapper = ChromeWrapper()

        useragent = SeleniumUserAgentBuilder().get_top()
        self.browser.config.webdriver_wrapper.set_user_agent(
            useragent
        )

        if headless:
            self.browser.config.webdriver_wrapper.in_headless()

        return self.browser.run()
