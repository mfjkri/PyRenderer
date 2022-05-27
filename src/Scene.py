import math

import pygame
import numpy

from Model import Model
from Camera import Camera


class Scene:
    def __init__(self, name: str, width: int, height: int,
                 framerate: int = 60):
        self.name = name

        self.VWIDTH = width
        self.VHEIGHT = height

        self.models = []

        self.camera = Camera(
            scene_width=width,
            scene_height=height,
            position=[-5, 6, -55]
        )
        self.projection: ProjectionMatrices = ProjectionMatrices(self)

        pygame.init()
        self.window = pygame.display.set_mode((self.VWIDTH, self.VHEIGHT))
        self.clock = pygame.time.Clock()
        self.framerate = framerate

    def add_model(self, model: Model) -> int:
        self.models.append(model)
        return len(self.models) - 1

    def is_face_within_screen(self, face: numpy.ndarray) -> bool:
        return not numpy.any((face == self.VWIDTH) | (face == self.VHEIGHT))

    def render(self):
        while True:
            self.window.fill(pygame.Color('darkslategray'))

            for model in self.models:
                model.draw()

            [exit() for i in pygame.event.get() if i.type == pygame.QUIT]

            pygame.display.flip()
            self.clock.tick(self.framerate)


class ProjectionMatrices:
    def __init__(self, scene: Scene):
        camera = scene.camera

        RIGHT = math.tan(camera.horizontal_fov / 2)
        LEFT = -RIGHT
        TOP = math.tan(camera.vertical_fov / 2)
        BOTTOM = -TOP
        NEAR_PLANE = camera.near_plane
        FAR_PLANE = camera.far_plane

        m00 = 2 / (RIGHT - LEFT)
        m11 = 2 / (TOP - BOTTOM)
        m22 = (FAR_PLANE + NEAR_PLANE) / (FAR_PLANE - NEAR_PLANE)
        m32 = -2 * NEAR_PLANE * FAR_PLANE / (FAR_PLANE - NEAR_PLANE)

        self.projection_matrix = numpy.array([
            [m00, 0, 0, 0],
            [0, m11, 0, 0],
            [0, 0, m22, 1],
            [0, 0, m32, 0]
        ])

        VW, VH = scene.VWIDTH, scene.VHEIGHT
        self.to_screen_matrix = numpy.array([
            [VW, 0, 0, 0],
            [0, -VH, 0, 0],
            [0, 0, 1, 0],
            [VW, VH, 0, 1]
        ])
