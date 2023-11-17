import pygame
import sys

class Menu:
    def __init__(self, options, ecran):
        self.options = options
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.red = (255, 0, 0)
        self.couleur_options = [self.white] * len(options)
        self.selectionne = None
        self.screen = ecran
        self.police = pygame.font.Font(None, 36)
        self.menu_bool = True
        self.submenu_b = False
        self.facile = False
        self.normale = False
        self.difficile = False

    def afficher_texte(self, message, x, y, couleur=(255, 255, 255)):
        if self.menu_bool == True:
            texte = self.police.render(message, True, couleur)
            self.screen.blit(texte, (x, y))

    def afficher(self):
        if self.menu_bool == True:
            self.screen.fill((0, 0, 0))
            self.afficher_texte("PONGPING", 600/2 + 25, 50)

            for i, option in enumerate(self.options):
                self.afficher_texte(option, 300 + 50, 250 + i * 50, self.couleur_options[i])
            pygame.display.flip()

    def update(self, event):
        if self.menu_bool == True:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.selectionne is not None:
                    if self.selectionne == len(self.options) - 1:
                        pygame.quit()
                        sys.exit()
                    else:
                        if self.submenu_b:
                            if self.selectionne == 0:
                                self.facile = True
                            elif self.selectionne == 1:
                                self.normale = True
                            elif self.selectionne == 2:
                                self.difficile = True
                        self.screen.fill((0, 0, 0))
                        self.menu_bool = False
            elif event.type == pygame.MOUSEMOTION:
                x, y = event.pos
                for i, option in enumerate(self.options):
                    rect = pygame.Rect(300 + 50, 250 + i * 50, 200, 50)
                    if rect.collidepoint(x, y):
                        self.couleur_options[i] = self.red
                        self.selectionne = i
                    else:
                        self.couleur_options[i] = self.white
            pygame.display.flip()