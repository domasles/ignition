from typing import TYPE_CHECKING
from utils.final import *

if TYPE_CHECKING:
    from window import Window

class HUD(metaclass=NoOverrideMeta):
    @final
    def __init__(self, window: "Window"):
        self.window = window
        self.on_init()

    def on_init(self): ...

    def draw(self): ...
