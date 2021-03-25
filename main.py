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
bg_color = (255, 255, 255)
white = (0, 0, 0)
b_king = pygame.image.load('king.png')
b_king_x = 435
b_king_y = 35
b_pawn_y = 130
g_pawn_y = 630
g_pawn1_x = 30
g_pawn2_x = 130
g_pawn3_x = 230
g_pawn4_x = 330
g_pawn5_x = 430
g_pawn6_x = 530
g_pawn7_x = 630
g_pawn8_x = 730
b_pawn1_x = 30
b_pawn2_x = 130
b_pawn3_x = 230
b_pawn4_x = 330
b_pawn5_x = 430
b_pawn6_x = 530
b_pawn7_x = 630
b_pawn8_x = 730
b_pawn1 = pygame.image.load("pawn.png")
b_pawn2 = pygame.image.load("pawn.png")
b_pawn3 = pygame.image.load("pawn.png")
b_pawn4 = pygame.image.load("pawn.png")
b_pawn5 = pygame.image.load("pawn.png")
b_pawn6 = pygame.image.load("pawn.png")
b_pawn7 = pygame.image.load("pawn.png")
b_pawn8 = pygame.image.load("pawn.png")
g_pawn1 = pygame.image.load("g_pawn.png")
g_pawn2 = pygame.image.load("g_pawn.png")
g_pawn3 = pygame.image.load("g_pawn.png")
g_pawn4 = pygame.image.load("g_pawn.png")
g_pawn5 = pygame.image.load("g_pawn.png")
g_pawn6 = pygame.image.load("g_pawn.png")
g_pawn7 = pygame.image.load("g_pawn.png")
g_pawn8 = pygame.image.load("g_pawn.png")

def black():
    screen.blit(b_king, (b_king_x, b_king_y))
    screen.blit(b_pawn1, (b_pawn1_x, b_pawn_y))
    screen.blit(b_pawn2, (b_pawn2_x, b_pawn_y))
    screen.blit(b_pawn3, (b_pawn3_x, b_pawn_y))
    screen.blit(b_pawn4, (b_pawn4_x, b_pawn_y))
    screen.blit(b_pawn5, (b_pawn5_x, b_pawn_y))
    screen.blit(b_pawn6, (b_pawn6_x, b_pawn_y))
    screen.blit(b_pawn7, (b_pawn7_x, b_pawn_y))
    screen.blit(b_pawn8, (b_pawn8_x, b_pawn_y))
def grey():
    screen.blit(g_pawn1, (g_pawn1_x, g_pawn_y))
    screen.blit(g_pawn2, (g_pawn2_x, g_pawn_y))
    screen.blit(g_pawn3, (g_pawn3_x, g_pawn_y))
    screen.blit(g_pawn4, (g_pawn4_x, g_pawn_y))
    screen.blit(g_pawn5, (g_pawn5_x, g_pawn_y))
    screen.blit(g_pawn6, (g_pawn6_x, g_pawn_y))
    screen.blit(g_pawn7, (g_pawn7_x, g_pawn_y))
    screen.blit(g_pawn8, (g_pawn8_x, g_pawn_y))
#standard game loop
while True:
    # input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill(bg_color)
    black()
    grey()
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