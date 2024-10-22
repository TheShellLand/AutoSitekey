from automon import logging

log = logging.getLogger(__name__)
log.setLevel(level=logging.DEBUG)


class AutoSiteKeyConfig(object):

    def __init__(self, **kwargs):
        self._args = kwargs

    def __repr__(self):
        return f'{self.__dict__}'

    def is_ready(self) -> bool:
        return True
