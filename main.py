#chess
import pygame
import sys
pygame.init()
clock = pygame.time.Clock()
screen_width = 800
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("CHESS")
icon = pygame.image.load('chess1.png')
pygame.display.set_icon(icon)
bg_color = (0, 0, 0)
white = (255, 255, 255)
#standard game loop
while True:
    # input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill(bg_color)
    # vertical lines
    pygame.draw.aaline(screen, white, (100, 0), (100, screen_height))
    pygame.draw.aaline(screen, white, (200, 0), (200, screen_height))
    pygame.draw.aaline(screen, white, (300, 0), (300, screen_height))
    pygame.draw.aaline(screen, white, (400, 0), (400, screen_height))
    pygame.draw.aaline(screen, white, (500, 0), (500, screen_height))
    pygame.draw.aaline(screen, white, (600, 0), (600, screen_height))
    pygame.draw.aaline(screen, white, (700, 0), (700, screen_height))
    # h0rizontal lines
    pygame.draw.aaline(screen, white, (0, 100), (screen_width, 100))
    pygame.draw.aaline(screen, white, (0, 200), (screen_width, 200))
    pygame.draw.aaline(screen, white, (0, 300), (screen_width, 300))
    pygame.draw.aaline(screen, white, (0, 400), (screen_width, 400))
    pygame.draw.aaline(screen, white, (0, 500), (screen_width, 500))
    pygame.draw.aaline(screen, white, (0, 600), (screen_width, 600))
    pygame.draw.aaline(screen, white, (0, 700), (screen_width, 700))
    pygame.display.flip()
    clock.tick(60)