from typing import Tuple

import numpy
import pygame
import Transform


class Model():
    def __init__(self, scene, path: str = None, vertices: list = None, faces: list = None):
        if path:
            vertices, faces = self.load_from_file(path)
        else:
            assert (not vertices and not faces) or (
                vertices or faces), "BOTH VERTICES AND FACES MUST BE PROVIDED"

        self.scene = scene
        self.vertices: numpy.ndarray = numpy.array(
            [numpy.array(v) for v in vertices])
        self.faces: numpy.ndarray = numpy.array(
            [numpy.array(face) for face in faces])

    def load_from_file(self, path: str) -> Tuple:
        vertices, faces = [], []

        with open(path, "r") as file:
            for line in [line.rstrip() for line in file.readlines()]:
                if line.startswith("v "):
                    vertices.append(
                        [float(i) for i in line.split()[1:]] +
                        [1]
                    )
                elif line.startswith('f'):
                    faces.append(
                        [
                            int(face_.split('/')[0]) - 1
                            for face_ in line.split()[1:]
                        ]
                    )

        return vertices, faces

    def draw(self):
        self.project_to_screen()

    def project_to_screen(self):
        vertices = self.vertices @ self.scene.camera.camera_matrix()
        vertices = vertices @ self.scene.projection.projection_matrix
        vertices /= vertices[:, -1].reshape(-1, 1)
        vertices[(vertices > 2) | (vertices < -2)] = 0
        vertices = vertices @ self.scene.projection.to_screen_matrix
        vertices = vertices[:, :2]

        for face in self.faces:
            polygon = vertices[face]
            if self.scene.is_face_within_screen(polygon):
                pygame.draw.polygon(
                    self.scene.window,
                    pygame.Color('blue'),
                    polygon,
                    1
                )

    def translate(self, pos):
        self.vertices = self.vertices @ Transform.translate(pos)

    def scale(self, scale_to):
        self.vertices = self.vertices @ Transform.scale(scale_to)

    def rotate_x(self, angle):
        self.vertices = self.vertices @ Transform.rotate_x(angle)

    def rotate_y(self, angle):
        self.vertices = self.vertices @ Transform.rotate_y(angle)

    def rotate_z(self, angle):
        self.vertices = self.vertices @ Transform.rotate_z(angle)
