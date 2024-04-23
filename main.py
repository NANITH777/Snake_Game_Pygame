import pygame
from pygame.locals import *
import time
import random

SIZE = 40
BACKGROUND_COLOR = (59, 125, 212)

class Snake:
    def __init__(self, surface_screen, length):
        self.length = length
        self.surface_screen = surface_screen
        self.block = pygame.image.load("resources/block.jpg").convert()    # to load the image
        self. x = [SIZE] * length
        self.y = [SIZE] * length
        self.direction = 'right'

    def draw(self):
        self.surface_screen.fill(BACKGROUND_COLOR)
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

    def increase_snake(self):
        self.length += 1
        self.x.append(-1)
        self.y.append(-1)


class Fruit:
    def __init__(self, surface_screen):
        self.surface_screen = surface_screen
        self.fruit = pygame.image.load("resources/apple.jpg").convert()
        self.x = SIZE * 3
        self.y = SIZE * 3

    def draw(self):
        self.surface_screen.blit(self.fruit, (self.x, self.y))
        pygame.display.flip()

    def move(self):
        self.x = random.randint(1, 24) * SIZE
        self.y = random.randint(1, 15) * SIZE


class Game:
    def __init__(self):
        pygame.init()  # Initialiser pygame
        self.surface = pygame.display.set_mode((1000, 640))  # to create a surface
        self.surface.fill((59, 125, 212))  # define the background color(rgb color picker)
        self.snake = Snake(self.surface, 1)
        self.snake.draw()
        self.fruit = Fruit(self.surface)
        self.fruit.draw()

    def play(self):
        self.snake.snake_move()
        self.fruit.draw()
        self.display_score()
        pygame.display.flip()

        if self.collision(self.snake.x[0], self.snake.y[0], self.fruit.x, self.fruit.y):
            self.snake.increase_snake()
            self.fruit.move()

        for i in range(3, self.snake.length):
            if self.collision(self.snake.x[0], self.snake.y[0], self.snake.x[i], self.snake.y[i]):
                raise "Game Over"

    def game_over(self):
        self.surface.fill(BACKGROUND_COLOR)
        font = pygame.font.SysFont('arial', 30)
        text1 = font.render(f"Game is over!!! your score is : {self.snake.length}", True, (250, 250, 250))
        self.surface.blit(text1, (300, 300))
        text2 = font.render(f"To play again press Enter. To exit press Escape", True, (250, 250, 250))
        self.surface.blit(text2, (220, 360))
        pygame.display.flip()

    def reset(self):
        self.snake = Snake(self.surface, 1)
        self.fruit = Fruit(self.surface)

    def collision(self, x1, y1, x2, y2):
        if x2 <= x1 < x2 + SIZE and y2 <= y1 < y2 + SIZE:
                return True
        return False

    def display_score(self):
        font = pygame.font.SysFont('arial', 30)
        score = font.render(f"score: {self.snake.length}", True, (250, 250, 250))
        self.surface.blit(score, (850, 10))

    def run(self):
        running = True
        pause = False

        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                    if event.key == K_RETURN:
                        pause = False

                    if not pause:
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

            try:
                if not pause:
                    game.play()
            except Exception as e:
                self.game_over()
                pause = True
                self.reset()

            time.sleep(0.3)


if __name__ == "__main__":
    game = Game()
    game.run()
    pygame.display.flip()



