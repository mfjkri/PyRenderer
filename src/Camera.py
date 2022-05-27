import math

import numpy


class Camera:
    def __init__(self, scene_width: int, scene_height: int, position: numpy.ndarray):
        # Positional vector
        self.position = numpy.array([*position, 1.0])

        # Directional vectors
        self.forward = numpy.array([0, 0, 1, 1])
        self.up = numpy.array([0, 1, 0, 1])
        self.right = numpy.array([1, 0, 0, 1])

        # Field of Views
        self.horizontal_fov = math.pi / 3
        self.vertical_fov = self.horizontal_fov * (scene_height / scene_width)

        # Clipping Planes
        self.near_plane = 0.1
        self.far_plane = 100

    def translate_matrix(self):
        x, y, z, w = self.position

        return numpy.array([
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 1, 0],
            [-x, -y, -z, 1]
        ])

    def rotate_matrix(self):
        rx, ry, rz, w = self.right
        fx, fy, fz, w = self.forward
        ux, uy, uz, w = self.up

        return numpy.array([
            [rx, ux, fx, 0],
            [ry, uy, fy, 0],
            [rz, uz, fz, 0],
            [0, 0, 0, 1]
        ])

    def camera_matrix(self):
        return self.translate_matrix() @ self.rotate_matrix()
