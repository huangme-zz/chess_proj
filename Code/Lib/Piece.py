from XiangQiBoard import XiangQiBoardException
from XiangQiBoard import XiangQiBoard

type_tuple = type(())

class PieceException(Exception):
  def __init__(self):
    pass

class LocationException(PieceException):
  pass




class Piece:
  def __init__(self, xiangqi_board,\
                enemy_xiangqi_board=XiangQiBoard(),\
                loc=(0,0)):

    if type(loc) != type_tuple or len(loc) != 2:
      raise LocationException()

    if type(xiangqi_board) != type(XiangQiBoard()):
      raise XiangQiBoardException()

    if type(enemy_xiangqi_board) != type(XiangQiBoard()):
      raise XiangQiBoardException()

    if not xiangqi_board.isValidLoc(loc):
      raise LocationException()

    self.__loc = loc
    self.__xiangqi_board = xiangqi_board
    self.__xiangqi_board.addPiece(self)
    self.__enemy_xiangqi_board = enemy_xiangqi_board

  def __str__(self):
    return 'Piece'

  def getLoc(self):
    return self.__loc

  def possibleAction(self):
    return []

  def goto(self, loc):
    if loc is in self.possibleAction():
      self.__xiangqi_board.movePiece(self, loc)
      self.__loc = loc
      return True
    return False

  def die(self):
    self.__xiangqi_board.killPiece(self)




class Horse(Piece):
  ACTION = [(1,2), (1,-2), (-1,2), (-1,-2), (2,1), (2,-1), (-2,1), (-2,-1)]

  def __str__(self):
    return 'Horse'

  def possibleAction(self):
    cur_x, cur_y = self.__loc
    possible_action_list = [(cur_x + x, cur_y + y) for (x,y)\
                             in ACTION]
    result = []
    for loc in possible_action_list:
      x, y = loc
      x = x - x / abs(x)
      y = y - y / abs(y)

      if self.xiangqi_board.isEmptyLoc(loc) and \
         self.xiangqi_board.isEmptyLoc((x,y)):

        result.append(loc)
    
    return result



class Chariot(Piece):
  ACTION = [(0,1), (0,-1), (1,0), (-1,0)]

  def __str__(self):
    return 'Chariot'

  def possibleAction(self):
    cur_x, cur_y = self.__loc
    result = []

    for (x, y) in ACTION:
      new_loc = (cur_x + x, cur_y + y)
      while self.__xiangqi_board.isEmptyLoc(new_loc)\
        and self.__xiangqi_board.isValidLoc(new_loc):
        result.append(new_loc)
        if not self.__enemy_xiangqi_board.isEmptyLoc(new_loc, enemy=True):
          break
        new_loc = (new_loc[0] + x, new_loc[1] + y)

    return result










