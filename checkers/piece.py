
from .constants import RED, WHITE, GREY, SQUARE_SIZE, CROWN
import pygame

class Piece:

    #Class Variables:
    PADDING = 15
    OUTLINE = 2

    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.king = False 
        self.x = 0
        self.y = 0
        self.calc_pos()

        #determining the direction the pieces are moving based on the color and coordinates of the board
        #not doing direction here anymore
        # if self.color == RED:
        #     self.direction = -1
        # else:
        #     self.direction = 1


        

        #calculate position, drawing from the center of the circle
    def calc_pos(self):
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2

    def make_king(self):
        self.king = True


    def draw(self, win):
        radius = SQUARE_SIZE//2 - self.PADDING
        pygame.draw.circle(win, GREY, (self.x, self.y), radius + self.OUTLINE)
        pygame.draw.circle(win, self.color, (self.x, self.y), radius)
        if self.king:
            win.blit(CROWN, (self.x - CROWN.get_width()//2, self.y - CROWN.get_height()//2) )

    def move (self, newrow, newcol):
        self.row = newrow
        self.col = newcol
        self.calc_pos()

        #useful for debugging
    def __repr__(self):
        return str(self.color)