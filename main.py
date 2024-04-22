import pygame
from pygame.locals import *


class Snake:
    def __init__(self, surface_screen):
        self.surface_screen = surface_screen
        self.block = pygame.image.load("resources/block.jpg").convert()    # to load the image
        self. x = 500
        self.y = 250

    def draw(self):
        self.surface_screen.fill((59, 125, 212))
        self.surface_screen.blit(self.block, (self.x, self.y))  # blit pour afficher l'image et (100, 100)
                                                                # pour les coordonnees de l'image
        pygame.display.flip()  # or display.update()

    def move_left(self):
        self.x -= 10
        self.draw()

    def move_right(self):
        self.x += 10
        self.draw()

    def move_up(self):
        self.y -= 10
        self.draw()

    def move_down(self):
        self.y += 10
        self.draw()


class Game:
    def __init__(self):
        pygame.init()  # Initialiser pygame
        self.surface = pygame.display.set_mode((1000, 500))  # to create a surface
        self.surface.fill((59, 125, 212))  # define the background color(rgb color picker)
        self.snake = Snake(self.surface)
        self.snake.draw()

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False

                    if event.key == K_UP:
                        self.snake.move_up()
                    if event.key == K_DOWN:
                        self.snake.move_down()
                    if event.key == K_LEFT:
                        self.snake.move_left()
                    if event.key == K_RIGHT:
                        self.snake.move_right()
                elif event.type == QUIT:
                    running = False


if __name__ == "__main__":
    game = Game()
    game.run()
    pygame.display.flip()



