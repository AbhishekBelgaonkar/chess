#chess
import pygame
import sys
pygame.init()
clock = pygame.time.Clock()
screen_width = 800
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("CHESS")
bg_color = (0, 0, 0)
white = (255, 255, 255)
while True:
    # input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill(bg_color)
    pygame.display.flip()
    clock.tick(60)