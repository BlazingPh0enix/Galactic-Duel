import pygame
import os
from gameWindow import draw_window, draw_winner
from shipFunctions import yellow_movement, red_movement, handle_bullets
from variables import bullet_vel, red_hit, width, yellow_hit, ship_width, ship_height, fps, max_bullets, bullet_fire_sound, bullet_hit_sound

pygame.display.set_caption("Galactic Duel")

def main():

    red = pygame.Rect(700, 300, ship_width, ship_height)
    yellow = pygame.Rect(100, 300, ship_width, ship_height)

    yellow_bullets = []
    red_bullets = []

    yellow_health = 10
    red_health = 10

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(fps)
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_LCTRL and len(yellow_bullets) < max_bullets:
                    bullet = pygame.Rect(yellow.x + yellow.width, yellow.y + yellow.height//2 - 2, 10, 5)
                    yellow_bullets.append(bullet)
                    bullet_fire_sound.play()
                
                if event.key == pygame.K_RCTRL and len(red_bullets) < max_bullets:
                    bullet = pygame.Rect(red.x, red.y + red.height//2 - 2, 10, 5)
                    red_bullets.append(bullet)
                    bullet_fire_sound.play()

            if event.type == yellow_hit:
                yellow_health -= 1
                bullet_hit_sound.play()
            
            if event.type == red_hit:
                red_health -= 1
                bullet_hit_sound.play()

        winner_text = ''

        if yellow_health <= 0:
            winner_text = 'Red Wins!'

        if red_health <= 0:
            winner_text = 'Yellow Wins!'

        if winner_text != '':
            draw_winner(winner_text)
            break

        keys_pressed = pygame.key.get_pressed()

        yellow_movement(keys_pressed, yellow)

        red_movement(keys_pressed, red)

        handle_bullets(yellow_bullets, red_bullets, yellow, red)

        draw_window(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health) 

    main()

if __name__ == "__main__":
    main()