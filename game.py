import pygame
import sys
from player import Player
from ball import Ball
from ai import AI
from menu import Menu


class Game:
    def __init__(self):
        self.WIDTH, self.HEIGHT = 800, 600
        self.WIN = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("PongPing")
        self.FPS = 60
        self.time = pygame.time.Clock()
        self.running = True
        self.player = Player(self.WIN, self.HEIGHT)
        self.ball = Ball(self.WIDTH // 2, self.HEIGHT // 2, self.WIN)
        self.NEW_BALL = Ball(self.WIDTH // 2, self.HEIGHT // 2, self.WIN)
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.ai = AI(300, 0, self.WIDTH, 10, self.WIN)
        self.score1 = 0
        self.score2 = 9
        self.game_start = False
        self.main_menu = ["Jouer", "Quitter"]
        self.submenu = ["FACILE", "NORMALE", "DIFFICLE", "QUITTER"]
        self.menu = Menu(self.main_menu, self.WIN)
        self.sub_menu = Menu(self.submenu, self.WIN)
        self.sub_menu.menu_bool = False
        self.police = pygame.font.Font(None, 36)
        self.timer_end = pygame.time.Clock()
        self.timer_active = False
        self.duree = 5000
        self.temps_ecoule = 0
    def bounce(self):
        if (self.ball.position[1] >= self.HEIGHT - self.ball.size and self.player.position[0]
                <= self.ball.position[0] <= self.player.position[0] + self.player.WIDTH):
            self.ball.speed *= 1.1
            self.ball.direction.y = - self.ball.direction.y
        if self.ball.position[0] <= 0 or self.ball.position[0] >= self.WIDTH - self.ball.size:
            self.ball.direction.x = - self.ball.direction.x

    def bounce_ai(self):
        if (0 <= self.ball.position[1] <= 0 + self.ai.HEIGHT and self.ai.x
                <= self.ball.position[0] <= self.ai.x + self.ai.WIDTH):
            self.ball.direction.y = - self.ball.direction.y

    def ai_predict(self):
        if self.ball.direction.y >= 0 and self.ball.position[1] > 0:
            if not self.ai.x <= self.ball.position[0] <= self.ai.x + self.ai.WIDTH:
                if self.ball.position[0] > self.ai.x + self.ai.WIDTH:
                    self.ai.move("right")
                elif self.ball.position[0] < self.ai.x:
                    self.ai.move("left")

    def afficher_texte(self, message, x, y, couleur=(255, 255, 255)):
        texte = self.police.render(str(message), True, couleur)
        self.WIN.blit(texte, (x, y))
    def score(self):
        if self.ball.position[1] < 0:
            self.score1 += 1
        elif self.ball.position[1] > self.HEIGHT:
            self.score2 += 1


    def affiche_score(self):
        self.afficher_texte(self.score2, 750, 250)
        self.afficher_texte(self.score1, 750, 350)

    def middle_line(self):
        x_ligne = self.HEIGHT // 2
        pygame.draw.line(self.WIN, self.WHITE, (0, x_ligne), (self.WIDTH, x_ligne), 2)
    def handle_move(self):
        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_a] and self.player.position[0] + self.player.speed > 0:
            self.player.position[0] -= self.player.speed
        elif pressed[pygame.K_d] and (self.player.position[0] + self.player.WIDTH) + self.player.speed <= self.WIDTH:
            self.player.position[0] += self.player.speed
        elif pressed[pygame.K_LEFT] and self.player.position[0] + self.player.speed > 0:
            self.player.position[0] -= self.player.speed
        elif pressed[pygame.K_RIGHT] and self.player.position[0] + self.player.WIDTH + self.player.speed <= self.WIDTH:
            self.player.position[0] += self.player.speed

    def ball_update(self):
        if self.ball.position[1] < (self.HEIGHT - self.HEIGHT) or self.ball.position[1] > self.HEIGHT:
            self.ball = self.NEW_BALL
        else:
            self.ball.draw()
            self.NEW_BALL = Ball(self.WIDTH // 2, self.HEIGHT // 2, self.WIN)
    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                self.menu.update(event)
                if self.menu.menu_bool == False:
                    self.sub_menu.menu_bool = True
                    self.sub_menu.submenu_b = True
                    if self.sub_menu.facile or self.sub_menu.normale or self.sub_menu.difficile:
                        self.sub_menu.menu_bool = False
                        if self.score1 < 10 and self.score2 < 10:
                            self.game_start = True
                self.sub_menu.update(event)

            if self.game_start:
                if self.sub_menu.facile:
                    self.ai.speed = 7
                elif self.sub_menu.normale:
                    self.ai.speed = 10
                elif self.sub_menu.difficile:
                    self.ai.speed = 15
                self.WIN.fill(self.BLACK)
                self.ball.move()
                self.ai_predict()
                self.handle_move()
                self.bounce()
                self.bounce_ai()
                self.middle_line()
                self.affiche_score()
                self.score()
                self.player.draw()
                self.ai.draw()
                self.ball_update()

            if self.menu.menu_bool:
                self.menu.afficher()
            if self.sub_menu.menu_bool:
                self.sub_menu.afficher()

            if self.score1 >= 10 or self.score2 >= 10:
                self.timer_active = True
                self.game_start = False
                if self.score2 >= 10:
                    self.WIN.fill(self.BLACK)
                    self.afficher_texte("AI vainquer", 350, 300)
                elif self.score1 >= 10:
                    self.WIN.fill(self.BLACK)
                    self.afficher_texte("Jouer vainquer", 350, 300)

            if self.timer_active:
                self.temps_ecoule = pygame.time.get_ticks() - 0
                if self.temps_ecoule >= self.duree:
                    pygame.quit()
                    sys.exit()

            pygame.display.flip()
            self.time.tick(self.FPS)
        pygame.quit()
        sys.exit()


