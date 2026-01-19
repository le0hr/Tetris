import sys, os
import pygame
import logic as lg
pygame.init()

screen = pygame.display.set_mode((480, 808))   #480, 808
button_surface = pygame.Surface((160, 80))
source_image = pygame.image.load('pic/start_button.png').convert_alpha()
button_image = pygame.transform.scale(source_image, (160, 80))
rect = pygame.Rect(160,364, 160, 80)
button_surface.blit(button_image, (0,0))

screen.blit(button_surface, rect)
def main ():
    button_image = pygame.transform.scale(source_image, (160, 80))
    rect = pygame.Rect(160,364, 160, 80)
    button_surface.blit(button_image, (0,0))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                os.abort()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if rect.collidepoint(event.pos):
                    lg.start(screen)
        if rect.collidepoint(pygame.mouse.get_pos()):
                pass
        pygame.display.update()

if __name__ == "__main__":
    main()