from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from window import Window

import glm

class Camera:
    def __init__(self, window: "Window", position: tuple=(0, 0, 0), FOV: int=50, clip_plane: tuple=(0.01, 1000)):
        self.window = window
        self.aspect_ratio = window.width / window.height

        self.position = glm.vec3(position)
        self.up = glm.vec3(0, 1, 0)

        self.FOV = FOV
        self.clip_plane = clip_plane

        self.projection_matrix = self.get_projection_matrix()
        self.view_matrix = self.get_view_matrix()

    def get_projection_matrix(self):
        return glm.perspective(glm.radians(self.FOV), self.aspect_ratio, self.clip_plane[0], self.clip_plane[1])
    
    def get_view_matrix(self):
        return glm.lookAt(self.position, glm.vec3(0), self.up)
