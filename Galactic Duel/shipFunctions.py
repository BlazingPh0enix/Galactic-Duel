import pygame
from variables import vel, border, height, width, bullet_vel, yellow_hit, red_hit

def yellow_movement(keys_pressed, yellow):

    if (keys_pressed[pygame.K_a] and yellow.x - vel > 0):
        yellow.x -= vel

    if (keys_pressed[pygame.K_d] and yellow.x + vel + yellow.width < border.x):
        yellow.x += vel

    if (keys_pressed[pygame.K_w] and yellow.y - vel > 0):
        yellow.y -= vel

    if (keys_pressed[pygame.K_s] and yellow.y + vel + yellow.height < height):
        yellow.y += vel

def red_movement(keys_pressed, red):

    if (keys_pressed[pygame.K_LEFT] and red.x - vel > border.x):
        red.x -= vel

    if (keys_pressed[pygame.K_RIGHT] and red.x + vel + red.width < width):
        red.x += vel

    if (keys_pressed[pygame.K_UP] and red.y - vel > 0):
        red.y -= vel

    if (keys_pressed[pygame.K_DOWN] and red.y + vel + red.height < height):
        red.y += vel

def handle_bullets(yellow_bullets, red_bullets, yellow, red):

    for bullet in yellow_bullets:
        bullet.x += bullet_vel
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(red_hit))
            yellow_bullets.remove(bullet)

        elif bullet.x > width:
            yellow_bullets.remove(bullet)

    for bullet in red_bullets:
        bullet.x -= bullet_vel
        if yellow.colliderect(bullet):
            pygame.event.post(pygame.event.Event(yellow_hit))
            red_bullets.remove(bullet)

        elif bullet.x < 0:
            red_bullets.remove(bullet)