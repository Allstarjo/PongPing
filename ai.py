import pygame

class AI:
    def __init__(self, x, y, win_width, speed, win):
        self.x = x
        self.win_width = win_width
        self.WHITE = (255, 255, 255)
        self.y = y
        self.WIN = win
        self.speed = speed
        self.HEIGHT, self.WIDTH = 10, 150

    def move(self, direction):
        if direction == "left" and self.x + self.speed > 0:
            self.x -= self.speed
        elif direction == "right" and self.x < self.win_width - self.WIDTH:
            self.x += self.speed

    def draw(self):
        pygame.draw.rect(self.WIN, self.WHITE, (self.x, 0,
                                                self.WIDTH, self.HEIGHT))
