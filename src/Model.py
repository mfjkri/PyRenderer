from typing import Tuple

import numpy
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
        # project_to_screen
        pass

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
