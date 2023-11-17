import pygame


class Player:
    def __init__(self, win, win_height):
        self.WIDTH, self.HEIGHT = 150, 10
        self.speed = 0
        self.WHITE = (255, 255, 255)
        self.position = [400, 500]
        self.WIN = win
        self.win_height = win_height

    def draw(self):
        pygame.draw.rect(self.WIN, self.WHITE, (self.position[0], self.win_height - self.HEIGHT,
                                                self.WIDTH, self.HEIGHT))
