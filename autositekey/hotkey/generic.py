from autositekey import Hotkey, Click, Type


class GenericHK(Hotkey):
    _URL = r'https://.*'

    _TEST = {
        Click('/html/body'),
    }

    _ACTIONS = [
        Click('/html/body'),
        Click('/html/body').xpath('/html/body').when('/html/body'),
        Type('hello').when('/html/body'),
    ]
