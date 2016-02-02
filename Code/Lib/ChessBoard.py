from Piece import *

class XiangQiBoardException(Exception):
  def __init__(self):
    pass



class XiangQiBoard:
  ''' Class Name: XiangQiBoard

      Class Introduction:
          Creating a Xiang Qi board for playing Xiang Qi game

      Class Member:
          board (private): a 9-by-10 2D list, use integer as its entry
          pieces (private): a list of attended pieces, the index of a piece
              is the nickname of this piece which will be used in the board
          dead (private): a list of died pieces
  '''

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
    ''' Return the board '''
    return self.__board

  def printSideBoard(self):
    ''' Print out the board which only have own pieces '''
    pass

  def isEmptyLoc(self, loc, enemy=False):
    ''' Check whether the given location is not occupied by other piece
        If 'enemy' is set to True, then the location will be reversed first 
    '''
    x, y = loc

    if enemy == True:
      x = 8 - x
      y = 9 - y

    if self.__board[x][y] != -1:
      return False
    return True

  def isValidLoc(self, loc, enemy=False):
    ''' Check whether the given location is in the board range or not
        If 'enemy' is set to True, then the location will be reversed first
    '''
    x, y = loc

    if enemy == True:
      x = 8 - x
      y = 9 - y

    if x > -1 and x < 9 and y > -1 and y < 10:
      return True
    return False

  def addPiece(self, piece):
    ''' Adding a piece to this board 
        Note: this function only add piece to the board, check if this action
            is permitted and valid before calling this function
    '''
    x, y = piece.getLoc()
    self.__board[x][y] = len(self.__pieces)
    self.__pieces.append(piece)

  def movePiece(self, piece, loc):
    ''' Moving a piece to a give location of this board
        Note: this function only move piece to the given location, check if
            this action is permitted and valid before calling this function
    '''
    cur_x, cur_y = piece.getLoc()
    x, y = loc
    self.__board[x][y] = self.__board[cur_x][cur_y]
    self.__board[cur_x][cur_y] = -1

  def killPiece(self, piece):
    ''' Append a piece to the dead list '''
    self.__dead.append(piece)






