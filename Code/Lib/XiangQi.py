''' Board Part '''
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

                  #----------------------------------#

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

  def inOwnArea(self, loc):
    ''' Check whether the location is in own area '''
    x, y = loc
    if x > -1 and x < 9 and y > -1 and y < 5:
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















''' Piece Part '''

type_tuple = type(())

class PieceException(Exception):
  def __init__(self):
    pass

class LocationException(PieceException):
  pass

''' Helper Functions '''
def addVector(v1, v2): ## Promised ##
  ''' Return the sum of v1 and v2
      v1 and v2 are 2D vectors
  '''
  return (v1[0] + v2[0], v1[1] + v2[1])

def subVector(v1, v2): ## Promised ##
  ''' Return the difference from v2 to v1 (v1 - v2)
      v1 and v2 are 2D vectors
  '''
  return (v1[0] - v2[0], v1[1] - v2[1])

def negVector(v): ## Promised ##
  ''' Return the negation of v
      v is a 2D vector
  '''
  return (-1 * v[0], -1 * v[1])

def getDirection(v): ## Promised ##
  ''' Return the direction of v
      v is a 2D vector
      e.g (+3, 0) --> (+1, 0)
          (0, -4) --> (0, -1)
  '''
  x, y = v
  if x != 0:
    x /= abs(x)

  if y != 0:
    y /= abs(y)

  return (x,y)



''' Main Functions & Classes '''

class Piece:
  ''' Class Name: Piece

      Class Introduction: 
          Creating a Piece and put it to the given Xiang Qi Board
          Will form a connection with Xiang Qi Board

      Class Member:
          xiangqi_board (private): the Xiang Qi Board of one's own
          enemy_xiangqi_board (private): the Xiang Qi Board of enemy
          loc (private): the current location of this Piece
  '''

  def __init__(self, xiangqi_board,\
                enemy_xiangqi_board=XiangQiBoard(),\
                loc=(0,0)):
    # check the format of location is valid
    if type(loc) != type_tuple or len(loc) != 2:
      raise LocationException()

    # check the type of xiangqi_board is XiangQiBoard
    if type(xiangqi_board) != type(XiangQiBoard()):
      raise XiangQiBoardException()

    # check the type of enemy_xiangqi_board is XiangQiBoard
    if type(enemy_xiangqi_board) != type(XiangQiBoard()):
      raise XiangQiBoardException()

    # check if the locaiton is not occupied
    if not xiangqi_board.isEmptyLoc(loc):
      raise LocationException()

    # check if the location is valid
    if not xiangqi_board.isValidLoc(loc):
      raise LocationException()

    self.__loc = loc
    self.__xiangqi_board = xiangqi_board
    self.__xiangqi_board.addPiece(self)
    self.__enemy_xiangqi_board = enemy_xiangqi_board



  def __str__(self):
    return 'Piece'

  def getLoc(self):
    ''' Return the current location '''
    return self.__loc

  def canGoto(self, loc): # virtual method
    ''' Check if the location is available '''
    pass

  def goto(self, loc):
    ''' Update the current location
        Note: check the target location is available before calling this
            function
    '''
    self.__xiangqi_board.movePiece(self, loc)
    self.__loc = loc

  def possibleAction(self): # virtual method
    ''' Return a list of possible action

        Note: available action and possible action are not identical. available
            action means the action is possible to do for this Piece and is
            available to put this Piece to the target location, while possible
            action only focus on whether the action can be done by this Piece
    '''
    pass

  def availableTargetLoc(self):
    ''' Return a list of available action

        Note: available action and possible action are not identical. available
            action means the action is possible to do for this Piece and is
            available to put this Piece to the target location, while possible
            action only focus on whether the action can be done by this Piece
    '''
    result = []

    for action in self.possibleAction():
      loc = addVector(self.__loc, action)
      # check if the action is valid
      if self.canGoto(loc):
        result.append(action)

    return result


  def die(self):
    self.__xiangqi_board.killPiece(self)





class Chariot(Piece):
  DIRECTION = [(0,1), (0,-1), (1,0), (-1,0)]

  def __str__(self):
    return 'Chariot'

  def canGoto(self, loc):
    # check if the location is valid and empty
    if not self.__xiangqi_board.isValidLoc(loc) or\
       not self.__xiangqi_board.isEmptyLoc(loc):
      return False

    # check if the action is valid for Chariot
    action = subVector(loc, self.__loc)
    if action[0] != 0 and action[1] != 0:
      return False

    # check if there are some pieces between the current location and target
    # location
    direction = getDirection(action)
    cur_loc = self.__loc
    cur_loc = addVector(cur_loc, direction)
    while cur_loc != loc:
      if not self.__xiangqi_board.isEmptyLoc(cur_loc) or\
         not self.__enemy_xiangqi_board.isEmptyLoc(cur_loc, enemy=True):
        return False
      cur_loc = addVector(cur_loc, direction)

    return True



class Horse(Piece):
  ''' Class Name: Horse (Piece)

      Class Introduction: 
          Creating a Horse and put it to the given Xiang Qi Board
          Will form a connection with Xiang Qi Board

      Class Member:
          xiangqi_board (private): the Xiang Qi Board of one's own
          enemy_xiangqi_board (private): the Xiang Qi Board of enemy
          loc (private): the current location of this Piece
          ACTION (public): possible actions list for Horse
  '''
  ACTION = [(1,2), (1,-2), (-1,2), (-1,-2), (2,1), (2,-1), (-2,1), (-2,-1)]

  def __str__(self):
    return 'Horse'

  def canGoto(self, loc):
    # check if the location is valid and empty
    if not self.__xiangqi_board.isValidLoc(loc) or\
       not self.__xiangqi_board.isEmptyLoc(loc):
      return False

    # check if the action is reachable for Horse
    action = subVector(loc, self.__loc)
    if action not in self.ACTION:
      return False

    # check if the Horse is obstructed
    x, y = action
    x = x - x / abs(x)
    y = y - y / abs(y)
    action = (x,y)
    loc = addVector(self.__loc, action)
    if not self.__xiangqi_board.isEmptyLoc(loc) and\
       not self.__enemy_xiangqi_board.isEmptyLoc(loc):
      return False

    return True



class Cannon(Piece):
  def __str__(self):
    return 'Cannon'

  def canGoto(self, loc):
    pass



class Elephant(Piece):
  Action = [(2,2), (2,-2), (-2,2), (-2,-2)]
  def __str__(self):
    return 'Elephant'

  def canGoto(self, loc):
    # check if the location is valid and empty
    if not self.__xiangqi_board.isValidLoc(loc) or\
       not self.__xiangqi_board.isEmptyLoc(loc):
      return False

    # check if the location is in own area
    if not self.__xiangqi_board.inOwnArea(loc):
      return False

    # check if the location is reachable for Elephant
    action = subVector(loc, self.__loc)
    if action not in ACTION:
      return False

    # check if the Elephant is obstructed
    action = getDirection(action)
    if not self.__xiangqi_board.isEmptyLoc(addVector(self.__loc, action)):
      return False

class General(Piece):
  PALACE = [(x,y) for x in range(3,6) for y in range(3,6)]
  ACTION = [(0,1), (-1,0), (0,-1), (1,0)]

  def __init__(self, xiangqi_board,\
                enemy_xiangqi_board=XiangQiBoard(),\
                loc=(0,0)):
    # check if the location is in Palace
    if loc not in PALACE:
      raise LocationException()
    Piece.__init__(self, xiangqi_board, enemy_xiangqi_board, loc)

  def __str__(self):
    return 'General'

  def canGoto(self, loc):
    pass


