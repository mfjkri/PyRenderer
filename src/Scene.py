import pygame

from src.Model import Model


class Scene:
    def __init__(self, name: str, width: int, height: int,
                 framerate: int = 60):
        self.name = name

        self.width = width
        self.height = height

        self.models = []

        pygame.init()
        self.window = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()
        self.framerate = framerate

    def add_model(self, model: Model) -> int:
        self.models.append(model)
        return len(self.models) - 1

    def render(self):
        while True:
            pygame.display.set_caption(str(self.clock.get_fps()))
            pygame.display.flip()
            self.clock.tick(self.framerate)
