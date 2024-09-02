from utils.config import SHADERS_DIR
from typing import TYPE_CHECKING
from utils.final import *

if TYPE_CHECKING:
    from window import Window

class HUD(metaclass=NoOverrideMeta):
    @final
    def __init__(self, window: "Window"):
        self.window = window
        self.vertex_shader = f"{SHADERS_DIR}/default_hud.vert"
        self.fragment_shader = f"{SHADERS_DIR}/default_hud.frag"

        self.on_init()

    def on_init(self): ...

    def draw(self): ...
