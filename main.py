import sys
sys.path.append("src")

import os

from Scene import Scene
from Model import Model

WIDTH, HEIGHT = 1600, 900


def main() -> None:
    scene: Scene = Scene(
        "test",
        width=WIDTH,
        height=HEIGHT
    )

    teapot_model = Model(
        scene=scene,
        path=os.path.join("models", "teapot.obj")
    )
    teapot_model.translate([-20, 10, 100])
    scene.add_model(teapot_model)

    scene.render()


if __name__ == "__main__":
    main()
