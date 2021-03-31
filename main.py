import pygame
import GEngine
width = 400
height = width
dimension = 8 #no of sqarues in a row or column
square = height//dimension
images = {}
pygame.display.set_caption("Chess")
icon = pygame.image.load("images/bp.png")
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
    screen.fill(pygame.Color("white")) # set the background colour to white 
    clock = pygame.time.Clock() # used to limit the maximum fps
    gs = GEngine.game() # allows us access to the game class
    LoadImages() # this is a function call for load images and is initialized just once before the main game loop so that we dont waste resources loading all the images again and again
    running = True 
    sqaureselected = () # no sqaure is selected initially
    playerclicks = [] # keeps track of player clicks
    while (running): # main game loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                location = pygame.mouse.get_pos() # x,y location for the mouse
                row = location[0]//square
                col = location[1]//square
                if sqaureselected == (row, col): # checks if same square is selected twice
                    sqaureselected = () # deselects the sqaure
                    playerclicks = [] # resets player clicks
                else:
                    sqaureselected = (row,col)
                    playerclicks.append(sqaureselected) # adds 1st and 2nd clicks to the list
                if len(playerclicks) == 2:
                    move = GEngine.move(playerclicks[0], playerclicks[1], gs.board)
                    print(move.getchessnotation())
                    gs.makemove(move)
                    sqaureselected = ()
                    playerclicks = []
        DrawGameState(screen, gs) # function call for the gamestate, which includes all the chess pieces
        clock.tick(30)
        pygame.display.flip() # updates the game display
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
            if piece != "--": # not empty square
                screen.blit(images[piece], pygame.Rect(c*square, r*square, square, square))
# makes sure that program only runs if this file is run
if __name__ == "__main__":
    main()
    

