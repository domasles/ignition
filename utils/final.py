class NoOverrideMeta(type):
    def __init__(cls, name, bases, clsdict):
        super().__init__(name, bases, clsdict)
        
        for base in bases:
            for attr, value in base.__dict__.items():
                if attr in clsdict and getattr(value, "_no_override", False):
                    raise TypeError(f"Cannot override final method {attr}")

def final(func):
    func._no_override = True
    return func
