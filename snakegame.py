import pygame
import time
import random

pygame.init()

w = (255, 255, 255)
b = (0, 0, 0)
g = (0, 155, 0)
r = (255, 0, 0)
clk = pygame.time.Clock()
wid = 600
ht = 600
font = pygame.font.SysFont(None, 25)
pygame.display.set_caption('SNAKE')
screen = pygame.display.set_mode((wid, ht))
block_size = 12
fps = 28


def snake(block_size, add_block):
    for x in add_block:
        pygame.draw.rect(screen, g, [x[0], x[1], block_size, block_size])


def display_msg(msg, color):
    font = pygame.font.SysFont(None, 25)
    screen_text = font.render(msg, True, color)
    screen.blit(screen_text, [wid / 5, ht / 5])


def startgame():
    game_exit = False
    game_over = False
    addblock = []
    snakelength = 1

    c_x = wid / 2
    c_y = ht / 2

    c_changed_x = 0
    c_changed_y = 0

    random_fruit_x = round(random.randrange(0, wid - block_size) / 10) * 10
    random_fruit_y = round(random.randrange(0, ht - block_size) / 10) * 10

    while not game_exit:
        while game_over == True:
            screen.fill(w)

            '''file1='g_over.mp3'
            pygame.mixer.music.load(file1)
            pygame.mixer.music.play(-1)'''

            display_msg("Your game is over , press c to continue or q to quit", r)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        pygame.mixer.music.stop()
                        startgame()
                    if event.key == pygame.K_q:
                        game_exit = True
                        game_over = False

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    c_changed_x = -block_size
                    c_changed_y = 0

                if event.key == pygame.K_RIGHT:
                    c_changed_x = block_size
                    c_changed_y = 0

                if event.key == pygame.K_UP:
                    c_changed_x = 0
                    c_changed_y = -block_size

                if event.key == pygame.K_DOWN:
                    c_changed_x = 0
                    c_changed_y = block_size

        if c_x >= wid or c_x < 0 or c_y >= ht or c_y < 0:
            game_over = True
        c_x = c_x + c_changed_x
        c_y = c_y + c_changed_y

        screen.fill(w)

        fruit_size = 30
        pygame.draw.rect(screen, r, [random_fruit_x, random_fruit_y, fruit_size, fruit_size])

        snakehead = []
        snakehead.append(c_x)
        snakehead.append(c_y)
        addblock.append(snakehead)

        if len(addblock) > snakelength:
            del addblock[0]

        for pieces in addblock[:-1]:
            if pieces == snakehead:
                game_over = True
        snake(block_size, addblock)
        pygame.display.update()

        if c_x >= random_fruit_x and c_x <= random_fruit_x + fruit_size:
            if c_y >= random_fruit_y and c_y <= random_fruit_y + fruit_size:
                random_fruit_x = round(random.randrange(0, wid - block_size) / 12) * 12
                random_fruit_y = round(random.randrange(0, ht - block_size) / 12) * 12
                snakelength += 1
        screen_text = font.render("score : " + str((snakelength * 10) - 10), True, b)
        screen.blit(screen_text, [wid - 180, 20])
        pygame.display.update()

        clk.tick(fps)
    pygame.quit()
    quit()


pygame.event.clear()
bg = pygame.image.load("sn.jpg")
bg = pygame.transform.scale(bg, (600, 600))
file = 'tetris.mp3'

pygame.mixer.init()
pygame.mixer.music.load(file)
pygame.mixer.music.play(-1)

screen.blit(bg, (0, 0))
font = pygame.font.SysFont(None, 45)
screen_text = font.render("Press Any Key", True, r)
screen.blit(screen_text, [wid / 5, ht / 5])
pygame.display.update()

while True:
    event = pygame.event.wait()

    if event.type == pygame.KEYDOWN:
        pygame.mixer.music.stop()
        startgame()