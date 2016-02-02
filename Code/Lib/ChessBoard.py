from Piece import *

class XiangQiBoardException(Exception):
  def __init__(self):
    pass



class XiangQiBoard:
  def __init__(self):
    self.__board = [[-1, -1, -1, -1, -1, -1, -1, -1, -1],

                  [-1, -1, -1, -1, -1, -1, -1, -1, -1],

                  [-1, -1, -1, -1, -1, -1, -1, -1, -1],

                  [-1, -1, -1, -1, -1, -1, -1, -1, -1],

                  [-1, -1, -1, -1, -1, -1, -1, -1, -1],

                  #----------楚河--------汉界----------#

                  [-1, -1, -1, -1, -1, -1, -1, -1, -1],

                  [-1, -1, -1, -1, -1, -1, -1, -1, -1],

                  [-1, -1, -1, -1, -1, -1, -1, -1, -1],

                  [-1, -1, -1, -1, -1, -1, -1, -1, -1],

                  [-1, -1, -1, -1, -1, -1, -1, -1, -1]]
    
    self.__pieces = []
    self.__dead = []

  def getBoard(self):
    return self.__board

  def printSideBoard(self):
    pass

  def isEmptyLoc(self, loc, enemy=False):
    x, y = loc

    if enemy == True:
      x = 8 - x
      y = 9 - y
      
    if self.__board[x][y] != -1:
      return False
    return True

  def isValidLoc(self, loc, enemy=False):
    x, y = loc

    if enemy == True:
      x = 8 - x
      y = 9 - y

    if x > -1 and x < 9 and y > -1 and y < 10:
      return True
    return False

  def addPiece(self, piece):
    loc = piece.getLoc()
    if self.isEmptyLoc(loc):
      self.__pieces.append(piece)

  def movePiece(self, piece, loc):
    cur_x, cur_y = piece.getLoc()
    x, y = loc
    self.__board[x][y] = self.__board[cur_x][cur_y]
    self.__board[cur_x][cur_y] = -1

  def killPiece(self, piece):
    self.__dead.append(piece)






