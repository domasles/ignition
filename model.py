from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from window import Window

import numpy

class Model:
    _instances = []

    def __init__(self, window: "Window", vertices: list, vertex_shader: str, fragment_shader: str):
        self.window = window
        self.ctx = window.ctx

        self.vertices = vertices
        
        self.vertex_shader = vertex_shader
        self.fragment_shader = fragment_shader

        self.vbo = self.get_vbo()
        self.shaders = self.load_shaders()
        self.vao = self.get_vao()

        Model._instances.append(self)

    def get_vertex_data(self):
        return numpy.array(self.vertices).astype("f4")
    
    def get_vao(self):
        return self.ctx.vertex_array(self.shaders, [(self.vbo, "3f", "in_pos")])
    
    def get_vbo(self):
        return self.ctx.buffer(self.get_vertex_data())

    def load_shaders(self):
        with open(self.vertex_shader) as f:
            vertex_shader = f.read()

        with open(self.fragment_shader) as f:
            fragment_shader = f.read()

        return self.ctx.program(vertex_shader, fragment_shader)
    
    def render(self):
        self.vao.render()

    def destroy(self):
        self.vbo.release()
        self.shaders.release()
        self.vao.release()

    @classmethod
    def destroy_all(cls):
        for instance in cls._instances:
            instance.destroy()

        cls._instances.clear()
