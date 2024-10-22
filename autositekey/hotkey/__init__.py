_ALL_CLASSES = [
    CLASS
    for name, CLASS in globals().items()
    if name.endswith('HK')
]
