from autositekey import Hotkey, Click, Type


class GenericHK(Hotkey):
    _url = 'about:blank'
    _test = {
        Click('/html/body'),
    }

    _actions = [
        Click('/html/body'),
        Click('/html/body').xpath('/html/body').when('/html/body'),
        Type('hello').when('/html/body'),
    ]
