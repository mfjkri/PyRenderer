from typing import Tuple


class Model():
    def __init__(self, path: str = None, vertices: list = None, faces: list = None):
        if path:
            vertices, faces = self.load_from_file(path)
        else:
            assert (not vertices and not faces) or (
                vertices or faces), "BOTH VERTICES AND FACES MUST BE PROVIDED"

        self.vertices = vertices
        self.faces = faces

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
