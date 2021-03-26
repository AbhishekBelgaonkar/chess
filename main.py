import pygame
from chesss import GEngine
width = 400
height = 400
dimension = 8 #no of sqarues in a row or column
square = height/dimension
images = {}
# call images only once dont load them every frame
def LoadImages():
    pieces = ['wP', 'wR', 'wQ','wK','wN','wB','bP', 'bR', 'bQ','bK','bN','bB']
    for piece in pieces:
        images[piece] = pygame.transform.scale(pygame.image.load("images/" + piece + ".png"), (square, square))
#input
def main():
    screen = pygame.display.set_mode((width, height))
    # the game state is simply a way of referring to a set of values for all the variables in a game program
    gs = GEngine.game()
    print(gs.board)
main()
