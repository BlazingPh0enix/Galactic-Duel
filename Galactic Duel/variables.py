import pygame
import os
pygame.font.init()
pygame.mixer.init()

width, height = 900, 500
fps = 60

bullet_vel = 8
max_bullets = 5
vel = 5

ship_width, ship_height = 55, 42

bullet_hit_sound = pygame.mixer.Sound(os.path.join('Assets', 'Grenade+1.mp3'))
bullet_fire_sound = pygame.mixer.Sound(os.path.join('Assets', 'Gun+Silencer.mp3'))
yellow_hit = pygame.USEREVENT + 1
red_hit = pygame.USEREVENT + 2

border = pygame.Rect(width//2 - 5, 0, 10, height)
window = pygame.display.set_mode((width, height))

RED = (255, 0, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)

winner_font = pygame.font.Font('Assets\\Grand9K Pixel.ttf', 85)
health_font = pygame.font.Font('Assets\\Grand9K Pixel.ttf', 30)

space = pygame.transform.scale(pygame.image.load(os.path.join
                                                 ('Assets','space.png')), (width, height))

yellow_spaceship = pygame.image.load(os.path.join('Assets', 'spaceship_yellow.png'))
yellow_spaceship = pygame.transform.rotate(pygame.transform.scale
                                           (yellow_spaceship, (ship_width, ship_height)), 90)

red_spaceship = pygame.image.load(os.path.join('Assets', 'spaceship_red.png'))
red_spaceship = pygame.transform.rotate(pygame.transform.scale
                                        (red_spaceship, (ship_width, ship_height)), 270)