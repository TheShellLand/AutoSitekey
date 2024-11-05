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
        try:
            if self.config.is_ready() and self.run():
                return True
        except Exception as error:
            log.error(error)
        return False

    def run(self, headless: bool = True):
        try:
            self.browser.config.webdriver_wrapper = ChromeWrapper()

            useragent = SeleniumUserAgentBuilder().get_top()
            self.browser.config.webdriver_wrapper.set_user_agent(
                useragent
            )

            if headless:
                self.browser.config.webdriver_wrapper.in_headless()

            return self.browser.run()
        except Exception as error:
            raise Exception(error)


class Click(object):
    """Object holds what to click. Optional: 'when' conditions"""

    def __init__(self, element):
        self._element = element

    @property
    def element(self):
        return self._element

    def click(self):
        try:
            return self.element.click()
        except Exception as error:
            raise Exception(f'click :: error :: {error}')


class Type(object):
    """Object holds what to type. Optional: 'when' conditions"""

    def __init__(self, text: str):
        self._text = [text]
        self._when = []

    def text(self, text: str):
        """text to type in browser"""
        self._text.append(text)
        return self

    def when(self, xpath: str):
        """xpath match for condition to be True"""
        self._when.append(xpath)
        return self


class Hotkey(AutoSiteKeyClient):
    """Hotkey class intended to be inherited when used for other sites"""

    _URL: str
    _ACTIONS: [Click or Type]
    _TEST: dict

    def __init__(self):
        super().__init__()

    def __repr__(self):
        return f'{self.hotkey_name}'

    def hotkey_name(self):
        return f'{type(self).__name__}'

    @property
    def actions(self) -> [Click or Type]:
        """list of Click or Type actions"""
        return self._ACTIONS

    @property
    def url(self):
        return self._URL
