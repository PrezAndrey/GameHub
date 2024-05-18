import pygame as p
from pygame.locals import *

#______________________________FUNCTIONS____________________________
def load_image(src, size, x, y):
    image = p.image.load(src).convert()
    image = p.transform.scale(image, size)
    rect = image.get_rect(center=(x, y))
    transparent = image.get_at((0, 0))
    #image.set_colorkey(transparent)
    
    return image, rect
    
    

#______________________________VARIABLES____________________________
screen_size = 800, 600
game_is_running = True

# WINDOW
p.init()
window = p.display.set_mode(screen_size)
p.display.set_caption("Game Hub")

# IMAGES
test = load_image("s.png", (150, 150), screen_size[0] // 2, screen_size[1] // 2)

# GAME LOOP

while game_is_running:
    for event in p.event.get():
        if event.type == QUIT:
            game_is_running = False
            p.quit()
    window.fill((255, 255, 255))
    window.blit(test[0], test[1])
    p.display.update()

