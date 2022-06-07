import pygame
import random
from pygame.locals import *


xSize = 800
ySize = xSize
bgColor = (66, 163, 207)
gridColor = (255,255,255)
xCenters = [xSize*1/6, xSize*1/2, xSize*5/6]
yCenters = [ySize*1/6, ySize*1/2, ySize*5/6]
xGrid = [0, xSize/3, xSize*2/3, xSize]
yGrid = [0, ySize/3, ySize*2/3, ySize]
positions = ["A","A","A","A","A","A","A","A","A"]

class board: #draw the board
    def __init__(self):
#        self.surfGrid = pygame.Surface((400, 400))
        pass

    def draw(self):
        self.screen = pygame.display.set_mode((xSize, ySize))
        self.screen.fill(bgColor)
        for i in range(0, xSize):
            self.screen.set_at((int(xGrid[1]), i), gridColor)
            self.screen.set_at((int(xGrid[2]), i), gridColor)
        for i in range(0, ySize):
            self.screen.set_at((i, int(yGrid[1])), gridColor)
            self.screen.set_at((i, int(yGrid[2])), gridColor)

        

class tictac:
    def __init__(self): 
        self.pieces = ["X", "O"]
        self.turn = self.pieces[0]
#        self.create = pygame.draw()
        self.backBoard = board()
        self.screen = pygame.display.set_mode((xSize, ySize))
        self.xTurn = True
        self.placement = []
        self.count = 0
        self.previousMoves=[0,0,0,0,0,0,0,0,0];

    def drawX(self, placement):
        pygame.draw.line(self.screen, gridColor, ((placement[0]-int(xGrid[1]*1/3)), placement[1]-int(xGrid[1]*1/3)), ((placement[0]+int(xGrid[1]*1/3)), placement[1]+int(xGrid[1]*1/3)), width=3) #Draw left-to-right line
        pygame.draw.line(self.screen, gridColor, ((placement[0]-int(xGrid[1]*1/3)), placement[1]+int(xGrid[1]*1/3)), ((placement[0]+int(xGrid[1]*1/3)), placement[1]-int(xGrid[1]*1/3)), width=3)

    def drawO(self, placement):
        pygame.draw.circle(self.screen, gridColor, (placement[0], placement[1]), xCenters[0]*2/3, 3)

    def drawStored(self):
        for i in range(len(self.previousMoves)):
            if positions[i] == "X":
                self.drawX(self.previousMoves[i])

            elif positions[i] == "O":
                self.drawO(self.previousMoves[i])


    def clickInSpace(self,xMouse,yMouse): #decision for where the mouse has clicked
        self.count = -1
        for j in range(len(yCenters)): #check to see where on the grid the mouse coords lie
            for i in range(len(xCenters)):
                self.count += 1
                if xMouse > xGrid[int(i)] and xMouse < xGrid[int(i+1)]:
                    if yMouse > xGrid[j] and yMouse < xGrid[j+1]:
                        self.placement = [int(xCenters[i]),int(yCenters[j])]                        
                        return



    def playTurns(self, xMouse, yMouse): #logic for whose turn it is
        if self.xTurn == True:
            self.clickInSpace(xMouse,yMouse)
            if positions[self.count] == "A":#can only put something here if nothing has been placed here
                self.drawX(self.placement)  #draw X in the position determined by clickInSpace
                self.previousMoves[self.count] = self.placement
                self.xTurn = not self.xTurn #switches turn to O
                positions[self.count] = self.turn #makes it known that an X was already placed here
                self.turn = self.pieces[1]

        elif self.xTurn == False:
            self.clickInSpace(xMouse,yMouse)
            if positions[self.count] == "A":
                self.drawO(self.placement)
                self.previousMoves[self.count] = self.placement
                self.xTurn = not self.xTurn
                positions[self.count] = self.turn
                self.turn = self.pieces[0]
#        print(positions)
                


class mainGame:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.board = board()
        self.board.draw() #draw board
        pygame.display.flip()
        self.tictac = tictac()
        self.running = True
        self.pause = False
        self.xMouse = 0
        self.yMouse = 0


    def play(self):

        self.board.draw()
        self.tictac.playTurns(self.xMouse,self.yMouse)
        self.tictac.drawStored()
        pygame.display.update()#update display
        

    def run(self):
        while self.running: #Game running loop, keeps it loaded unitl I hit escape
            for event in pygame.event.get():
                if event.type == MOUSEBUTTONDOWN: #do something if mouse gets clicked 
                    self.xMouse,self.yMouse = pygame.mouse.get_pos()
                    self.play()
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE: #hit escape and quit
                        self.running = False
                elif event.type == QUIT:
                    self.running = False
                    

if __name__ == "__main__":
    game = mainGame()
    game.run()