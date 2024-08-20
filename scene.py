from utils.final import *

import pygame

class Scene(metaclass=NoOverrideMeta):
    def __init__(self, window):
        self.window = window

    @final
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.window.close()

            self.window.fill((0, 0, 0))
            self.draw()

            pygame.display.flip()
            self.window.clock.tick(60)

    def draw(self): ...

class HUD():
    def __init__(self, window):
        self.window = window

    def draw(self): ...
