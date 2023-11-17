import pygame

class Ball:
    def __init__(self, x, y, win):
        self.size = 15
        self.WHITE = (255, 255, 255)
        self.speed = 7
        self.WIN = win
        self.position = [x, y]
        self.direction = pygame.Vector2(1, 1).normalize()

    def move(self):
        self.position[0] += self.speed * self.direction.x
        self.position[1] -= self.speed * self.direction.y

    def draw(self):
        pygame.draw.ellipse(self.WIN, self.WHITE, (int(self.position[0]), int(self.position[1]),
                                                   self.size, self.size))
