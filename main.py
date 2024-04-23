import pygame
from pygame.locals import *
import time

SIZE = 40

class Snake:
    def __init__(self, surface_screen, length):
        self.length = length
        self.surface_screen = surface_screen
        self.block = pygame.image.load("resources/block.jpg").convert()    # to load the image
        self. x = [SIZE] * length
        self.y = [SIZE] * length
        self.direction = 'right'

    def draw(self):
        self.surface_screen.fill((59, 125, 212))
        for i in range(self.length):
            self.surface_screen.blit(self.block, (self.x[i], self.y[i]))  # blit pour afficher l'image et (100, 100)
                                                                # pour les coordonnees de l'image
        pygame.display.flip()  # or display.update()

    def move_left(self):
        self.direction = 'left'

    def move_right(self):
        self.direction = 'right'

    def move_up(self):
        self.direction = 'up'

    def move_down(self):
        self.direction = 'down'

    def snake_move(self):
        for i in range(self.length-1, 0, -1):
            self.x[i] = self.x[i-1]
            self.y[i] = self.y[i - 1]

        if self.direction == 'left':
            self.x[0] -= SIZE
        if self.direction == 'right':
            self.x[0] += SIZE
        if self.direction == 'up':
            self.y[0] -= SIZE
        if self.direction == 'down':
            self.y[0] += SIZE
        self.draw()


class Fruit:
    def __init__(self, surface_screen):
        self.surface_screen = surface_screen
        self.fruit = pygame.image.load("resources/apple.jpg").convert()
        self.x = SIZE * 3
        self.y = SIZE * 3

    def draw(self):
        self.surface_screen.blit(self.fruit, (self.x, self.y))
        pygame.display.flip()


class Game:
    def __init__(self):
        pygame.init()  # Initialiser pygame
        self.surface = pygame.display.set_mode((1000, 680))  # to create a surface
        self.surface.fill((59, 125, 212))  # define the background color(rgb color picker)
        self.snake = Snake(self.surface, 2)
        self.snake.draw()
        self.fruit = Fruit(self.surface)
        self.fruit.draw()

    def play(self):
        self.snake.snake_move()
        self.fruit.draw()

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

            game.play()
            time.sleep(0.3)


if __name__ == "__main__":
    game = Game()
    game.run()
    pygame.display.flip()



