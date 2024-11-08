#  BOMBERMAN

import pygame
import sys

# Initialiser pygame
pygame.init()

# Définir les dimensions de la fenêtre
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Aller-Retour d'une Balle")

# Couleurs
rouge = (255, 0, 0)
white = (255, 255, 255)

en_cours = True
clock = pygame.time.Clock()

while en_cours:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            en_cours = False

    # Remplir l'écran et dessiner la balle
    screen.fill(white)
    pygame.draw.circle(screen, rouge, (100, 200), 20)

    # Rafraîchir l'affichage
    pygame.display.flip()

    # Contrôler la vitesse de la boucle
    clock.tick(60)

# Quitter pygame
pygame.quit()
sys.exit()