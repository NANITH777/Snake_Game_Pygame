import pygame
from pygame.locals import *
import time
import random

SIZE = 40
BACKGROUND_COLOR = (40, 30, 232)
delay = 0.2


class Snake:
    def __init__(self, surface_screen, length):
        self.length = length
        self.surface_screen = surface_screen
        self.block = pygame.image.load("resources/block.jpg").convert()    # to load the image
        self. x = [SIZE] * length
        self.y = [SIZE] * length
        self.direction = 'right'

    def draw(self):
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
        pygame.display.set_caption("Snake Game")

        pygame.mixer.init()
        self.game_music()
        self.surface = pygame.display.set_mode((1000, 640))  # to create a surface
        self.surface.fill((59, 125, 212))  # define the background color(rgb color picker)
        self.snake = Snake(self.surface, 1)
        self.snake.draw()
        self.fruit = Fruit(self.surface)
        self.fruit.draw()

    def snake_background(self):
        bg = pygame.image.load("resources/background.jpg")
        self.surface.blit(bg, (0, 0))

    def instructions_music(self):
        pygame.mixer.music.load("resources/instru_music.mp3")
        pygame.mixer.music.play()
        pygame.mixer.music.set_endevent(pygame.USEREVENT + 1)

    def show_instructions(self):
        self.surface.fill(BACKGROUND_COLOR)
        self.instructions_music()
        font = pygame.font.SysFont('arial black', 30)
        instructions = [
            "Welcome to SNAKE GAME!",
            "",
            "Use arrow keys to move the snake.",
            "Press SPACE to pause/resume the game.",
            "Press ESCAPE to quit the game.",
            "",
            "Press ENTER to start the game."
        ]

        y_position = 100
        for line in instructions:
            text_surface = font.render(line, True, (255, 255, 255))
            self.surface.blit(text_surface, (250, y_position))
            y_position += 50

        pygame.display.flip()

        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_RETURN:
                        waiting = False
                        pygame.mixer.music.stop()

                elif event.type == pygame.USEREVENT + 1:
                    self.instructions_music()
                elif event.type == QUIT:
                    pygame.quit()
                    exit(0)

    def play(self):
        self.snake_background()
        self.snake.snake_move()
        self.fruit.draw()
        self.display_score_level()
        pygame.display.flip()

        if self.collision(self.snake.x[0], self.snake.y[0], self.fruit.x, self.fruit.y):
            self.play_sound("ding2")
            self.snake.increase_snake()
            self.fruit.move()

        for i in range(3, self.snake.length):
            if self.collision(self.snake.x[0], self.snake.y[0], self.snake.x[i], self.snake.y[i]):
                self.play_sound("crash")
                self.play_sound("game_over")
                self.game_music()
                raise "Game Over"

        if not (0 <= self.snake.x[0] <= 1000 and 0 <= self.snake.y[0] <= 640):
            self.play_sound("crash")
            self.play_sound("game_over")
            self.game_music()
            raise "Hit The borders"

    def game_music(self):
        pygame.mixer.music.load("resources/game_music.mp3")
        pygame.mixer.music.play()
        pygame.mixer.music.set_endevent(pygame.USEREVENT + 1)  # Set event when music ends

    def play_sound(self, sound):
        sound = pygame.mixer.Sound(f"resources/{sound}.mp3")
        pygame.mixer.Sound.play(sound)

    def game_over(self):
        self.snake_background()
        font = pygame.font.SysFont('arial', 30)
        text1 = font.render(f"Game is over!!! your score is : {self.snake.length} level is : "
                            f"{self.snake.length // 5 + 1}", True, (250, 250, 250))
        self.surface.blit(text1, (230, 300))
        text2 = font.render(f"To play again press Enter. To exit press Escape", True, (250, 250, 250))
        self.surface.blit(text2, (220, 360))
        pygame.display.flip()
        pygame.mixer.music.pause()

    def reset(self):
        self.snake = Snake(self.surface, 1)
        self.fruit = Fruit(self.surface)

    def collision(self, x1, y1, x2, y2):
        if x2 <= x1 < x2 + SIZE and y2 <= y1 < y2 + SIZE:
                return True
        return False

    def display_score_level(self):
        font = pygame.font.SysFont('arial', 30)
        level = self.snake.length // 5 + 1

        score = font.render(f"score: {self.snake.length}", True, (250, 250, 250))
        level_text = font.render(f"Level: {level}", True, (250, 250, 250))

        self.surface.blit(score, (850, 10))
        self.surface.blit(level_text, (850, 50))

    def run(self):
        running = True
        over = False
        paused = False
        delay = 0.2

        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False

                    if event.key == K_RETURN:
                        over = False
                        pygame.mixer.music.unpause()

                    if event.key == K_SPACE:
                        paused = not paused

                    if not over and not paused:
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

                elif event.type == pygame.USEREVENT + 1:
                    self.game_music()  # Restart the music

            try:
                if not over and not paused:
                    game.play()
            except Exception as e:
                self.game_over()
                over = True
                self.reset()
                delay = 0.2

            # Check if snake length is a multiple of 5 and reduce the delay
            if self.snake.length % 5 == 0 and self.snake.length != 0:
                delay = max(0.05, delay - 0.01)  # Reduce the delay, but don't go below 0.05 seconds

            time.sleep(delay)


if __name__ == "__main__":
    game = Game()
    game.show_instructions()
    game.run()
    pygame.display.flip()



