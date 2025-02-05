import re
import automon
import selenium

from automon.integrations.seleniumWrapper.user_agents import SeleniumUserAgentBuilder

import selenium.webdriver.remote.webelement

from .config import AutoSiteKeyConfig
from .actions import (
    Actions,
    Click,
    Type,
    OpenUrl,
)

log = automon.log.logging.getLogger(__name__)
log.setLevel(level=automon.log.DEBUG)


class AutoSiteKeyClient(object):
    """A way to configure website behaviors to auto hotkey to anything"""

    _URL: str = None
    _ACTIONS: [Actions or Click or Type or OpenUrl] = []
    _TEST: [Actions or Click or Type] = []

    def __init__(self, **kwargs):
        self.browser = automon.integrations.seleniumWrapper.SeleniumBrowser()
        self.config = AutoSiteKeyConfig(**kwargs)

    def __repr__(self):
        return f'{self.__dict__}'

    def get(self, url: str, delay_on_load: int = None):
        """Open url in browser"""

        if delay_on_load:
            result = self.browser.get(url=url)
            automon.Sleeper.seconds(seconds=delay_on_load)
        else:
            result = self.browser.get(url=url)

        return result

    def is_ready(self, **kwargs) -> bool:
        """Check if client is ready"""

        try:
            if self.config.is_ready() and self.run(**kwargs):
                log.debug(f'AutoSiteKeyClient :: IS READY')
                return True
        except Exception as error:
            raise Exception(f'AutoSiteKeyClient :: IS NOT READY :: ERROR :: {error=}')

        return False

    def play(self, actions: list = None) -> bool:
        """play actions"""

        results = []

        if actions and type(actions) != list:
            actions = [actions]

        log.debug(f'AutoSiteKeyClient :: PLAY :: {actions=}')
        log.info(f'AutoSiteKeyClient :: PLAY :: {len(actions)} ACTIONS')

        if not actions and self._ACTIONS:
            actions = self._ACTIONS
        elif not actions and not self._ACTIONS:
            raise SyntaxError(f'AutoSiteKeyClient :: PLAY :: ERROR :: MISSING ACTIONS :: {actions}')

        for action in actions:

            if type(action) == Actions:
                result = self.play_action(action=action)
                results.append(dict(
                    action=action,
                    result=result,
                ))
                log.debug(f'AutoSiteKeyClient :: PLAY :: {result=}')

            elif type(action) == Click:
                result = self.play_click(action=action)
                results.append(dict(
                    action=action,
                    result=result,
                ))
                log.debug(f'AutoSiteKeyClient :: PLAY :: {result=}')

            elif type(action) == OpenUrl:
                result = self.play_openurl(action=action)

            elif type(action) == Type:
                result = self.play_type(action=action)
                results.append(dict(
                    action=action,
                    result=result,
                ))
                log.debug(f'AutoSiteKeyClient :: PLAY :: {result=}')

        log.debug(f'AutoSiteKeyClient :: PLAY :: {results=}')
        log.info(f'AutoSiteKeyClient :: PLAY :: {len(results)} ACTIONS :: DONE')
        return results

    def play_action(self, action: Actions) -> bool:
        pass

    def play_click(self, action: Click) -> bool:
        """Click `selenium.webdriver.remote.webelement.WebElement`"""

        log.debug(f'AutoSiteKeyClient :: PLAY :: CLICK :: {action=}')

        element = action.element

        # check if selenium Element
        if type(element) == selenium.webdriver.remote.webelement.WebElement:
            result = self.browser.action_click(element=element)
            log.debug(f'AutoSiteKeyClient :: PLAY :: CLICK :: ELEMENT :: {result=}')
            log.info(f'AutoSiteKeyClient :: PLAY :: CLICK :: ELEMENT :: DONE')
            return result or True

        # check if xpath
        if type(element) == str:

            # //*[@id="content-text"]/span
            _regex_xpath_short = r'[/][/][*]'
            # /html/
            _regex_xpath_full = r'/html/'

            _regex_list = [
                _regex_xpath_full,
                _regex_xpath_short,
            ]

            for _regex in _regex_list:

                if re.compile(_regex).match(element):
                    _element = self.browser.find_xpath(value=element)
                    result = self.browser.action_click(element=_element)
                    log.debug(f'AutoSiteKeyClient :: PLAY :: CLICK :: XPATH :: {result=}')
                    log.info(f'AutoSiteKeyClient :: PLAY :: CLICK :: XPATH :: DONE')
                    return result or True

        # check if str
        if type(element) == str:

            _elements = self.browser.find_elements_with_beautifulsoup(match=element)

            # try to find the exact match
            if _elements:

                log.debug(f'AutoSiteKeyClient :: PLAY :: CLICK :: SEARCH :: {len(_elements)} ELEMENTS')

                for _element in _elements:
                    # pop from end of list
                    _element = _elements.pop(-1)

                    _match = re.compile(element).match(_element.text)

                    if _match:
                        try:
                            result = self.browser.action_click(element=_element)
                            log.debug(f'AutoSiteKeyClient :: PLAY :: CLICK :: SEARCH :: {result=}')
                            log.info(f'AutoSiteKeyClient :: PLAY :: CLICK :: SEARCH :: DONE')
                            return result or True
                        except Exception as error:
                            log.error(f'AutoSiteKeyClient :: PLAY :: CLICK :: SEARCH :: {error=}')

        raise Exception(f'AutoSiteKeyClient :: PLAY :: CLICK :: ERROR :: NOT FOUND :: {element=}')

    def play_openurl(self, action: OpenUrl) -> bool:
        """Open url"""

        log.debug(f'AutoSiteKeyClient :: PLAY :: OPEN URL :: {action=}')

        url = action.url
        kwargs = action.kwargs

        result = self.browser.get(url=url, **kwargs)

        log.debug(f'AutoSiteKeyClient :: PLAY :: OPEN URL :: {result=}')
        log.info(f'AutoSiteKeyClient :: PLAY :: OPEN URL :: DONE')

        return result or True

    def play_type(self, action: Type):
        pass

    def run(self, headless: bool = True, enable_logging: bool = True):
        """Run browser"""

        try:
            self.browser.config.webdriver_wrapper = automon.integrations.seleniumWrapper.webdriver_chrome.ChromeWrapper()

            self.browser.config.webdriver_wrapper.enable_antibot_detection()
            self.browser.config.webdriver_wrapper.set_logging_level(level='DEBUG')

            if headless:
                self.browser.config.webdriver_wrapper.in_headless()

            if enable_logging:
                self.browser.config.webdriver_wrapper.enable_logging()

            run = self.browser.run()

            log.debug(f'AutoSiteKeyClient :: RUN :: {run=}')
            log.info(f'AutoSiteKeyClient :: RUN :: DONE')
            return run or True
        except Exception as error:
            raise Exception(f'AutoSiteKeyClient :: RUN :: ERROR :: {error=}')

        return False

    def test(self):
        """Play tests"""

        _TEST = self._TEST

        if _TEST:
            log.debug(f'AutoSiteKeyClient :: TEST :: {_TEST=}')

            result = self.play(_TEST)
            log.debug(f'AutoSiteKeyClient :: TEST :: {result=} :: DONE')
            log.info(f'AutoSiteKeyClient :: TEST :: DONE')
            return result or True

        raise ValueError(f'AutoSiteKeyClient :: TEST :: ERROR :: NO TESTS FOUND :: {_TEST=}')


class Hotkey(AutoSiteKeyClient):
    """Hotkey class intended to be inherited when used for other sites"""

    # _URL: str
    # _ACTIONS: [Actions]
    # _TEST: [Actions]

    def __init__(self):
        super().__init__()

    def __repr__(self):
        return (
            f'{type(self).__name__} :: '
            f'{len(self.ACTIONS)} ACTIONS :: '
            f'{len(self.TEST)} TESTS :: '
            f'{self.URL or "NO URL"}'
        )

    @property
    def ACTIONS(self) -> [Click or Type]:
        """list of Click or Type actions"""
        return self._ACTIONS

    def _hotkey_name(self):
        return f'{type(self).__name__}'

    def _re_search(self, pattern: str, search: str):
        return re.compile(pattern).search(search)

    @property
    def _regex_url(self):
        if self._URL:
            return re.compile(self._URL)

    @property
    def TEST(self):
        return self._TEST

    @property
    def URL(self):
        return self._URL
