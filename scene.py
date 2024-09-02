from utils.config import SHADERS_DIR
from typing import TYPE_CHECKING
from utils.final import *

if TYPE_CHECKING:
    from window import Window

import pygame

class Scene(metaclass=NoOverrideMeta):
    @final
    def __init__(self, window: "Window"):
        self.window = window
        self.vertex_shader = f"{SHADERS_DIR}/default_scene.vert"
        self.fragment_shader = f"{SHADERS_DIR}/default_scene.frag"

        self.on_init()

    def on_init(self): ...

    def draw(self): ...

    @final
    def run(self):
        self.window.check_events()

        self.window.fill((0, 0, 0))
        self.draw()

        pygame.display.flip()
        self.window.clock.tick(60)
