import pygame
import time
import random

WIDTH = 800
HEIGHT = 600


BLOCK_SIZE = 20


SPEED = 12

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (213, 50, 80)  # Kolor jedzenia
GREEN = (0, 255, 0)  # Kolor węża
BLUE = (50, 153, 213)  # Kolor wyniku


pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Klasyczny Snake w Pygame')


clock = pygame.time.Clock()

font_score = pygame.font.SysFont("bahnschrift", 25)
font_gameover = pygame.font.SysFont("bahnschrift", 40)



def display_score(score):

    value = font_score.render("Wynik: " + str(score), True, BLUE)
    screen.blit(value, [10, 10])


def draw_snake(snake_body):

    for segment in snake_body:

        pygame.draw.rect(screen, GREEN, [segment[0], segment[1], BLOCK_SIZE, BLOCK_SIZE])


def get_random_food_pos():

    x = round(random.randrange(0, WIDTH - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
    y = round(random.randrange(0, HEIGHT - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
    return x, y


def message(msg, color, y_offset=0):

    mesg = font_gameover.render(msg, True, color)
    text_rect = mesg.get_rect(center=(WIDTH / 2, HEIGHT / 2 + y_offset))
    screen.blit(mesg, text_rect)



def game_loop():
    game_over = False
    game_close = False


    x1 = WIDTH / 2
    y1 = HEIGHT / 2


    x1_change = 0
    y1_change = 0


    snake_body = []
    snake_length = 1


    food_x, food_y = get_random_food_pos()

    while not game_over:


        while game_close:
            screen.fill(BLACK)
            message("Przegrałeś!", RED, -30)
            message("Naciśnij C-Gra od nowa, Q-Wyjście", WHITE, 30)
            display_score(snake_length - 1)
            pygame.display.update()

            for event in pygame.event.get():

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True


            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_LEFT and x1_change == 0:
                    x1_change = -BLOCK_SIZE
                    y1_change = 0
                elif event.key == pygame.K_RIGHT and x1_change == 0:
                    x1_change = BLOCK_SIZE
                    y1_change = 0
                elif event.key == pygame.K_UP and y1_change == 0:
                    y1_change = -BLOCK_SIZE
                    x1_change = 0
                elif event.key == pygame.K_DOWN and y1_change == 0:
                    y1_change = BLOCK_SIZE
                    x1_change = 0


        if x1 >= WIDTH or x1 < 0 or y1 >= HEIGHT or y1 < 0:
            game_close = True


        x1 += x1_change
        y1 += y1_change
        screen.fill(BLACK)

        pygame.draw.rect(screen, RED, [food_x, food_y, BLOCK_SIZE, BLOCK_SIZE])


        snake_head = [x1, y1]

        snake_body.append(snake_head)


        if len(snake_body) > snake_length:
            del snake_body[0]


        for segment in snake_body[:-1]:
            if segment == snake_head:
                game_close = True

        draw_snake(snake_body)
        display_score(snake_length - 1)

        pygame.display.update()


        if x1 == food_x and y1 == food_y:
            food_x, food_y = get_random_food_pos()
            snake_length += 1



        clock.tick(SPEED)

    pygame.quit()
    quit()



if __name__ == "__main__":
    game_loop()