import pygame
import os
from variables import window, space, health_font, border, width, height, yellow_spaceship, red_spaceship, winner_font, RED, YELLOW, WHITE

def draw_window(red, yellow, red_bullet, yellow_bullet, red_health, yellow_health):

    window.blit(space, (0, 0))
    pygame.draw.rect(window, (0, 0, 0), border)

    red_health_text = health_font.render('Health: ' + str(red_health), 1, WHITE)
    yellow_health_text = health_font.render('Health:'+ str(yellow_health), 1, WHITE)
    window.blit(red_health_text, (width - red_health_text.get_width() - 10, 10))
    window.blit(yellow_health_text, (10, 10))

    window.blit(yellow_spaceship, (yellow.x, yellow.y))
    window.blit(red_spaceship, (red.x, red.y))

    for bullet in red_bullet:
        pygame.draw.rect(window, RED, bullet)

    for bullet in yellow_bullet:
        pygame.draw.rect(window, YELLOW, bullet)

    pygame.display.update()

def draw_winner(display_text):
    draw_text = winner_font.render(display_text, 1, WHITE)
    window.blit(draw_text, (width/2 - draw_text.get_width()/2, height/2 - draw_text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(10000)