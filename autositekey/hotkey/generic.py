from autositekey import Hotkey, Click, Type


class GenericHK(Hotkey):
    URL = 'about:blank'

    TEST = {
        Click('/html/body'),
    }

    ACTIONS = [
        Click('/html/body'),
        Click('/html/body').xpath('/html/body').when('/html/body'),
        Type('hello').when('/html/body'),
    ]
