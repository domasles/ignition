import pygame, sys, moderngl

class Window:
    def __init__(self, width, height, title="Game Window"):
        self.width = width
        self.height = height
        self.title = title

        pygame.init()
        pygame.display.set_caption(title)

        pygame.display.gl_set_attribute(pygame.GL_CONTEXT_MAJOR_VERSION, 4)
        pygame.display.gl_set_attribute(pygame.GL_CONTEXT_MINOR_VERSION, 6)
        pygame.display.gl_set_attribute(pygame.GL_CONTEXT_PROFILE_MASK, pygame.GL_CONTEXT_PROFILE_CORE)

        self.screen = pygame.display.set_mode((width, height), pygame.OPENGL | pygame.DOUBLEBUF)
        self.ctx = moderngl.create_context()

        self.clock = pygame.time.Clock()

    def fill(self, color):
        self.ctx.clear(color=color)

    def close(self):
        pygame.quit()
        sys.exit()
