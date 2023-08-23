from automon import Logging

log = Logging(name='Hotkey', level=Logging.DEBUG)


class Click(object):
    """Object holds what to click. Optional: 'when' conditions"""

    def __init__(self, xpath: str):
        self._xpath = [xpath]
        self._when = []

    def when(self, xpath: str):
        """xpath to click in browser"""
        self._when.append(xpath)
        return self

    def xpath(self, xpath: str):
        """xpath match for condition to be True"""
        self._xpath.append(xpath)
        return self


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


class Hotkey(object):
    """Hotkey class intended to be inherited when used for other sites"""

    _actions: [Click or Type]
    _url: str
    _test: dict

    def __repr__(self):
        return f'{self.hotkey_name}'

    @property
    def hotkey_name(self):
        return f'{type(self).__name__}'

    @property
    def actions(self) -> [Click or Type]:
        """list of Click or Type actions"""
        return self._actions

    @property
    def url(self):
        return self._url

    def logging(
            self,
            name: str = None,
            level: int = Logging.DEBUG,
            **kwargs
    ) -> Logging:
        return Logging(name=name or self.hotkey_name, level=level, **kwargs)
