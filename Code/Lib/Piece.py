from XiangQiBoard import XiangQiBoardException
from XiangQiBoard import XiangQiBoard

type_tuple = type(())

class PieceException(Exception):
  def __init__(self):
    pass

class LocationException(PieceException):
  pass

''' Helper Functions '''
def addVector(v1, v2):
  return (v1[0] + v2[0], v1[1] + v2[1])

def subVector(v1, v2):
  return (v1[0] - v2[0], v1[1] - v2[1])

def negVector(v):
  return (-1 * v[0], -1 * v[1])

def getDirection(v):
  x, y = v
  if x != 0:
    x /= abs(x)

  if y != 0:
    y /= abs(y)

  return (x,y)



''' Main Functions '''

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

    for action in self.availableAction():
      loc = addVector(self.__loc, action)
      # check if the action is valid
      if self.canGoto(loc):
        result.append(action)

    return result


  def die(self):
    self.__xiangqi_board.killPiece(self)




class Horse(Piece):
  ACTION = [(1,2), (1,-2), (-1,2), (-1,-2), (2,1), (2,-1), (-2,1), (-2,-1)]

  def __str__(self):
    return 'Horse'

  def canGoto(self, loc):
    # check if the location is valid and empty
    if not self.__xiangqi_board.isValidLoc(loc) or\
       not self.__xiangqi_board.isEmptyLoc(loc):
      return False

    # check if the action is valid for Horse
    action = subVector(loc, self.__loc)
    if action is not in self.ACTION:
      return False

    # check if the Horse is obstructed
    x, y = action
    x = x - x / abs(x)
    y = y - y / abs(y)
    action = (x,y)
    if not self.__xiangqi_board.isEmptyLoc(addVector(self.__loc, action)):
      return False

    return True



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


  def possibleAction(self):
    cur_x, cur_y = self.__loc
    result = []

    for (x, y) in self.ACTION:
      new_loc = (cur_x + x, cur_y + y)
      while self.__xiangqi_board.isEmptyLoc(new_loc)\
        and self.__xiangqi_board.isValidLoc(new_loc):
        result.append(new_loc)
        if not self.__enemy_xiangqi_board.isEmptyLoc(new_loc, enemy=True):
          break
        new_loc = (new_loc[0] + x, new_loc[1] + y)

    return result


class General:
  ACTION = [(0,1), (-1,1), (-1,0), (-1,-1), (0,-1), (1,-1), (1,0), (1,1)]
  def __str__(self):
    return 'General'

  def 










