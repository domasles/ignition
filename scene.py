from utils.final import *

import pygame

class Scene(metaclass=NoOverrideMeta):
    @final
    def __init__(self, window):
        self.window = window
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
