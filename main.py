import pygame
from pygame.locals import *


def draw_block():
    surface.fill((59, 125, 212))
    surface.blit(block, (block_x, block_y))  # blit pour afficher l'image et (100, 100) pour les coordonnees de l'image
    pygame.display.flip()  # or display.update() 


if __name__ == "__main__":
    pygame.init()    # Initialiser pygame

    surface = pygame.display.set_mode((1000, 500))   # to create a surface
    surface.fill((59, 125, 212))                     # define the background color

    block = pygame.image.load("resources/block.jpg").convert()    # to load the image
    block_x = 500
    block_y = 250
    surface.blit(block, (block_x, block_y))
    pygame.display.flip()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
    
                if event.key == K_UP:
                    block_y -= 10
                    draw_block()
                if event.key == K_DOWN:
                    block_y += 10
                    draw_block()
                if event.key == K_LEFT:
                    block_x -= 10
                    draw_block()
                if event.key == K_RIGHT:
                    block_x += 10
                    draw_block()
            elif event.type == QUIT:
                running = False

