import automon

log = automon.log.logging.getLogger(__name__)
log.setLevel(level=automon.log.DEBUG)


class Click(object):
    """Object holds what to click. Optional: 'when' conditions"""

    def __init__(self, element):
        self.element = element

    def __repr__(self):
        return f'Click :: {self.element}'


class Type(object):
    """Object holds what to type. Optional: 'when' conditions"""

    def __init__(self, text: str):
        self._text = [text]
        self._when = []

    def __repr__(self):
        return f'Type :: {self._text}'

    def text(self, text: str):
        """text to type in browser"""
        self._text.append(text)
        return self

    def when(self, xpath: str):
        """xpath match for condition to be True"""
        self._when.append(xpath)
        return self


class OpenUrl(object):
    """Object holds what Url to open"""

    def __init__(self, url: str, kwargs=None):
        self.url = url
        self.kwargs = kwargs

    def __repr__(self):
        return f'OpenUrl :: {self.url}'


class Actions(object):
    """Object holds a set actions"""

    def __init__(self, name: str, page_pattern: str = None):
        """
        :param name: give your Actions set a name
        :param page_pattern: regex pattern to match url
        """

        self.name = name
        self.page_pattern = page_pattern
        self.steps = ()

        log.debug(f'Actions :: {self.name} :: created')

    def __repr__(self):
        return f'Actions :: {len(self.steps)}'

    def add_action(self, step: OpenUrl or Click or Type):
        log.debug(f'Actions :: {self.name} :: add_action :: {step}')
        self.steps = self.steps + (step,)
        log.info(f'Actions :: {self.name} :: add_action :: added')
        return self
