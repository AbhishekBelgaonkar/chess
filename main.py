import pygame
import GEngine
width = 400
height = width
dimension = 8 #no of sqarues in a row or column
square = height//dimension
images = {}
pygame.display.set_caption("Chess")
icon = pygame.image.load("images/bP.png")
pygame.display.set_icon(icon)
# call images only once dont load them every frame
def LoadImages():
    pieces = ['wp', 'wR', 'wQ','wK','wN','wB','bp', 'bR', 'bQ','bK','bN','bB']
    for piece in pieces:
        images[piece] = pygame.transform.scale(pygame.image.load("images/" + piece + ".png"), (square, square))
#input
def main():
    screen = pygame.display.set_mode((width, height))
    # the game state is simply a way of referring to a set of values for all the variables in a game program
    screen.fill(pygame.Color("white"))
    clock = pygame.time.Clock()
    gs = GEngine.game()
    LoadImages()
    running = True
    while (running):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        clock.tick(30)
        pygame.display.flip()
        DrawGameState(screen, gs)
def DrawGameState(screen, gs):
    drawBoard(screen) # draws squares
    drawPieces(screen, gs.board) # draws pieces on squares
def drawBoard(screen):
    colours = [pygame.Color("white"), pygame.Color("grey")]
    for r in range(dimension):
        for c in range(dimension):
            colour = colours[((r+c)%2)] # if row and column sum is odd the dark sqaure and if even the grey square
            pygame.draw.rect(screen, colour, pygame.Rect(c*square, r*square, square, square))
def drawPieces(screen, board):
    for r in range(dimension):
        for c in range(dimension):
            piece = board[r][c]
            if piece != "--":#not empty square
                screen.blit(images[piece], pygame.Rect(c*square, r*square, square, square))
# makes sure that program only runs if this file is run
if __name__ == "__main__":
    main()
    

