import pygame

class Ball: 

    def __init__(self):
        self.rayon = 20
        self.color = (255, 0, 0)
        self.position_x = 20    
        self.position_y = 20
        self.velocity_x = 10
        self.velocity_y = 8
        

    def draw_ball(self, screen):
        pygame.draw.circle(screen, self.color, (self.position_x, self.position_y), self.rayon) # (origine, couleur, (posX, posY), rayon)
    
    def moving_ball(self):
        self.position_x += self.velocity_x
        self.position_y += self.velocity_y
        
        if self.position_x > 800 - 20 or self.position_x <= 20 :
            self.velocity_x = -self.velocity_x
        elif self.position_y > 600 - 20 or self.position_y <= 20:
            self.velocity_y = -self.velocity_y 