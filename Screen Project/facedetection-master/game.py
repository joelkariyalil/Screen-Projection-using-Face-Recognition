import pygame
import random
import time
import math

# Initialize pygame
pygame.init()

# Create window (width, height)
screen = pygame.display.set_mode(((800, 600)))
ScreenHeight = screen.get_height()
ScreenWidth = screen.get_width()

# Background picture
background = pygame.image.load("background.jpg")

# Title and Icon
pygame.display.set_caption("F22-Raptor Simulator")
icon = pygame.image.load("jet1.png")
pygame.display.set_icon(icon)


# Object List (obstacles)
obstacle_list = []


class Obstacle(object):

    def __init__(self):  # removed unused parameters
        self.obstacleImg = 'rock.png'  # pygame.image.load("rock.png")
        self.obstacleX = random.randint(600, 700)
        self.obstacleY = random.randint(0, ScreenHeight - 64)
        self.obstacleX_change = random.uniform(-0.3, -0.2)

    def __repr__(self):
        return f'Obstacle(image={self.obstacleImg!r}, X={self.obstacleX}, Y={self.obstacleY}, change={self.obstacleX_change})'

    def spawn_obstacle(self):
        image = pygame.image.load(self.obstacleImg)
        screen.blit(image, (self.obstacleX, self.obstacleY))


# Keep window running (Infinite-Loop)
running = True

# Timer
timer1_start = time.time()
timer1_current = 0

# Counter while-loop to display objects
count_object_display = 0

# While-Loop (Everything that takes place during the game is inside here)
while running:

    timer1_current = time.time()

    if timer1_current - timer1_start >= 1:
        timer1_start = time.time()  # Timer of start set to current time
        obstacle = Obstacle()  # Create instance of class obstacle
        obstacle_list.append(obstacle)
        print(obstacle)

    # Insert Background
    screen.blit(background, (0, 0))

    # End game / close window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    while count_object_display <= len(obstacle_list)-1:
        obstacle_list[count_object_display].spawn_obstacle()
        count_object_display += 1

        if count_object_display > len(obstacle_list)-1:
            count_object_display = 0


    # Update after each iteration of the while-loop
    pygame.display.update()