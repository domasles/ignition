from utils.final import *

class HUD(metaclass=NoOverrideMeta):
    @final
    def __init__(self, window):
        self.window = window
        self.on_init()

    def on_init(self): ...

    def draw(self): ...
