from utils.config import SHADERS_DIR
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from window import Window
    from camera import Camera

import numpy, glm

class Model:
    _instances = []

    def __init__(self, window: "Window", vertices: list, space: str="scene", camera: "Camera"=None, vertex_shader: str=None, fragment_shader: str=None):
        self.window = window
        self.ctx = window.ctx

        self.vertices = vertices

        self.space = space
        self.camera = camera

        if self.space == "scene":
            if self.camera == None:
                raise ValueError("In scene space it's expected to specify a camera")
            
            self.vertex_shader = f"{SHADERS_DIR}/default_scene.vert" if vertex_shader == None else vertex_shader
            self.fragment_shader = f"{SHADERS_DIR}/default_scene.frag" if fragment_shader == None else fragment_shader

        elif self.space == "hud":
            self.vertex_shader = f"{SHADERS_DIR}/default_hud.vert" if vertex_shader == None else vertex_shader
            self.fragment_shader = f"{SHADERS_DIR}/default_hud.frag" if fragment_shader == None else fragment_shader

        self.vbo = self.get_vbo()
        self.shaders = self.load_shaders()
        self.vao = self.get_vao()

        self.model_matrix = self.get_model_matrix()

        self.on_init()

        Model._instances.append(self)

    def on_init(self):
        if self.space == "scene":
            self.shaders["projection_matrix"].write(self.camera.projection_matrix)
            self.shaders["view_matrix"].write(self.camera.view_matrix)
            self.shaders["model_matrix"].write(self.model_matrix)

    def get_vertex_data(self):
        return numpy.array(self.vertices).astype("f4")
    
    def get_vao(self):
        return self.ctx.vertex_array(self.shaders, [(self.vbo, "3f", "in_position")])
    
    def get_vbo(self):
        return self.ctx.buffer(self.get_vertex_data())

    def load_shaders(self):
        with open(self.vertex_shader) as f:
            vertex_shader = f.read()

        with open(self.fragment_shader) as f:
            fragment_shader = f.read()

        return self.ctx.program(vertex_shader, fragment_shader)
    
    def get_model_matrix(self):
        return glm.mat4()
    
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
