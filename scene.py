from utils.final import *

import pygame

class Scene(metaclass=NoOverrideMeta):
    def __init__(self, window):
        self.window = window

    @final
    def run(self):
        self.window.check_events()

        self.window.fill((0, 0, 0))
        self.draw()

        pygame.display.flip()
        self.window.clock.tick(60)

    def draw(self): ...

class HUD():
    def __init__(self, window):
        self.window = window

    def draw(self): ...
