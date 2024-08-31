import numpy

class Model:
    def __init__(self, window, vertices, vertex_shader, fragment_shader):
        self.window = window
        self.ctx = window.ctx

        self.vertices = vertices

        self.vertex_shader = vertex_shader
        self.fragment_shader = fragment_shader

        self.vbo = self.get_vbo()
        self.shaders = self.load_shaders()
        self.vao = self.get_vao()

        self.render()

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
