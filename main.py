#  BOMBERMAN

import pygame
import sys

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

x_balle = 20
vitesse_x = 5
y_balle = 20
vitesse_y = 5


while en_cours:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            en_cours = False

    # Remplir l'écran et dessiner la balle
    screen.fill(white)
    pygame.draw.circle(screen, rouge, (x_balle, y_balle), 20) # (origine, couleur, (posX, posY), rayon)

    x_balle += vitesse_x
    y_balle += vitesse_y
    
    if x_balle > 800 - 20 or x_balle <= 20 :
        vitesse_x = -vitesse_x
    elif y_balle > 600 - 20 or y_balle <= 20:
        vitesse_y = -vitesse_y 

    # Rafraîchir l'affichage
    pygame.display.flip()

    # Contrôler la vitesse de la boucle
    clock.tick(60)

# Quitter pygame
pygame.quit()
sys.exit()