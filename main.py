import pygame
import random
import math


pygame.mixer.init()
Screen_width = 800
Screen_height = 600
pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 255)

# adding music


# introductory font
manual = pygame.font.Font('freesansbold.ttf', 45)

show_text = True


def showintro():
    if show_text == True:
        text1 = manual.render("TO START PRESS UPARROW KEY  ", True, RED, BLACK)
        text1_rect = text1.get_rect()
        text1_rect.center = (400, 200)
        Screen.blit(text1, text1_rect)


sc = pygame.font.Font('freesansbold.ttf', 32)


def show_score():
    score = sc.render("deaths ", True, GREEN, BLUE)
    score_rect = score.get_rect()
    score_rect.center = (650, 100)
    Screen.blit(score, score_rect)


call_death = pygame.font.Font('freesansbold.ttf', 32)
no_of_deaths = 0
car_hit = False


def show_deaths():
    deaths = call_death.render(str(no_of_deaths), True, RED, BLACK)
    deaths_rect = deaths.get_rect()
    deaths_rect.center = (630, 150)
    Screen.blit(deaths, deaths_rect)

call_over = pygame.font.Font('freesansbold.ttf',40)


def show_gameover():
    game_over = call_over.render("GAME OVER ", True,RED,BLACK)
    game_over_rect = game_over.get_rect()
    game_over_rect.center = (300,300)
    Screen.blit(game_over,game_over_rect)


Screen = pygame.display.set_mode((Screen_width, Screen_height))
pygame.display.set_caption("racing  era")

m_background = pygame.image.load("pics/mainback.png")

m_x = 0
m_y = 0


def show_ground():
    Screen.blit(m_background, (m_x, m_y))


roadx = 150
roady = -900

c_roady = 0

road = pygame.image.load("pics/image - Copy.png")
# road_rect = road.get_rect(center =(roadx,roady))

car = pygame.image.load("pics/corvettee.png")
car_x = 200
car_y = 536
change_in_car_X = 0
change_in_car_y = 0


def show_car(x, y):
    Screen.blit(car, (car_x, car_y))


oppcar1 = pygame.image.load("pics/oppcar1.png")
oppcar1_x = random.randint(241, 450)
oppcar1_y = -800


def show_oppcar1(x, y):
    Screen.blit(oppcar1, (oppcar1_x, oppcar1_y))


oppcar2 = pygame.image.load("pics/oppcar1.png")
oppcar2_x = random.randint(185, 240)
oppcar2_y = -700


def show_oppcar2(x, y):
    Screen.blit(oppcar2, (oppcar2_x, oppcar2_y))


oppcar3_x = random.randint(185, 430)
oppcar3_y = -650

oppcar3 = pygame.image.load("pics/oppcar1.png")


def show_oppcar3(x, y):
    Screen.blit(oppcar3, (oppcar3_x, oppcar3_y))


def carcollide(w, x, y, z):
    global oppcar1_y
    global oppcar2_y
    global oppcar3_y
    global car_y
    global car_hit
    global no_of_deaths
    distance = math.sqrt((car_x - oppcar1_x) ** 2 + (car_y - oppcar1_y) ** 2)

    if distance <= 40:
        car_y = 536
        car_hit = True
        no_of_deaths += 1
        oppcar1_y = -800
        oppcar3_y = -650
        oppcar2_y = -800




def carcollide1(w, x, y, z):
    global oppcar2_y
    global oppcar3_y
    global oppcar1_y
    global car_y
    global car_hit
    global no_of_deaths
    distancex = math.sqrt((car_x - oppcar2_x) ** 2 + (car_y - oppcar2_y) ** 2)

    if distancex <= 40:
        car_y = 536
        car_hit = True
        no_of_deaths += 1
        oppcar1_y = -800
        oppcar3_y = -650
        oppcar2_y = -800


def carcollide2(w, x, y, z):
    global oppcar3_y
    global car_y
    global car_hit
    global no_of_deaths
    global  oppcar1_y
    global oppcar2_y
    distancex = math.sqrt((car_x - oppcar3_x) ** 2 + (car_y - oppcar3_y) ** 2)

    if distancex <= 40:
        car_y = 536
        car_hit = True
        no_of_deaths += 1
        oppcar1_y = -800
        oppcar3_y = -650
        oppcar2_y = -800


carcollide(oppcar1_y, oppcar1_x, car_x, car_y)

running = True

while running:
    show_ground()
    Screen.blit(road, (roadx, roady))
    showintro()
    show_score()
    show_deaths()

    roady -= c_roady
    if roady >= 0:
        roady = -900
    if car_y == 536:
        c_roady = 0

    keys = (pygame.key.get_pressed())
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if keys[pygame.K_UP]:
            c_roady = -0.6
            change_in_car_y = 0.7
            show_text = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                change_in_car_X = 2

            if event.key == pygame.K_LEFT:
                change_in_car_X = -2

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                change_in_car_X = 0
            if event.key == pygame.K_LEFT:
                change_in_car_X = 0
    if car_x <= 150:
        car_x = 150
    if car_x >= 450:
        car_x = 450

    if car_y <= 450:
        show_oppcar1(oppcar1_x, oppcar1_y)
        show_oppcar2(oppcar2_x, oppcar2_y)
        show_oppcar3(oppcar3_x, oppcar3_y)

    if car_y <= 450:
        change_in_car_y = 0
        c_roady = -0.6


    car_x = car_x + change_in_car_X
    car_y -= change_in_car_y

    carcollide(oppcar1_x, car_x, oppcar1_y, car_y)
    carcollide1(oppcar2_x, car_x, oppcar2_y, car_y)
    carcollide2(oppcar3_x, car_x, oppcar3_y, car_y)

    show_car(car_x, car_y)

    if oppcar2_y >= 600:
        oppcar2_y = -800

    if oppcar3_y >= 600:
        oppcar3_y = -650

    if oppcar1_y >= 600:
        oppcar1_y = -800
        show_oppcar1(oppcar1_x, oppcar1_y)

    if car_y <= 450:
        oppcar1_y += 2
        oppcar2_y += 2
        oppcar3_y += 2

    if no_of_deaths == 3:
        show_gameover()
        



    pygame.display.update()
pygame.quit()
