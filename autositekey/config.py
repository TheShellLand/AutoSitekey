from automon import logging

from autositekey.hotkey import _ALL_CLASSES

log = logging.getLogger(__name__)
log.setLevel(level=logging.DEBUG)


class AutoSiteKeyConfig(object):

    def __init__(self, **kwargs):
        self._args = kwargs

    def __repr__(self):
        return f'{self.__dict__}'

    def test(self):
        return _ALL_CLASSES
