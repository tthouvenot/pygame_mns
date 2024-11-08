#  BOMBERMAN

import pygame
import sys
from balle import Ball

# Initialiser pygame
pygame.init()

# Définir les dimensions de la fenêtre
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Bomberman")

# Couleurs
rouge = (255, 0, 0)
white = (255, 255, 255)

en_cours = True
clock = pygame.time.Clock()

ball = Ball()


while en_cours:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            en_cours = False

    # Remplir l'écran et dessiner la balle
    screen.fill(white)
    ball.draw_ball(screen)

    ball.moving_ball()

    # Rafraîchir l'affichage
    pygame.display.flip()

    # Contrôler la vitesse de la boucle
    clock.tick(60)

# Quitter pygame
pygame.quit()
sys.exit()