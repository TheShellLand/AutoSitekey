from automon.log import Logging

log = Logging(name='AutoSiteKeyConfig', level=Logging.DEBUG)


class AutoSiteKeyConfig(object):

    def __init__(self, **kwargs):
        self._args = kwargs

    def __repr__(self):
        return f'{self.__dict__}'
