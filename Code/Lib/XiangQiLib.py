''' Board Part '''
class XiangQiBoardException(Exception):
  def __init__(self):
    pass


''' Class Name: XiangQiBoard

    Class Introduction:
        Creating a Xiang Qi board for playing Xiang Qi game

    Class Member:
        board (private): a 9-by-10 2D list, use integer as its entry
        pieces (private): a list of attended pieces, the index of a piece
            is the nickname of this piece which will be used in the board
        dead (private): a list of died pieces
'''
class XiangQiBoard:
  PALACE = [(x,y) for x in range(3) for y in range(3,6)]

  ''' Construct a XiangQiBoard object '''
  def __init__(self):
    self.board = [[-1, -1, -1, -1, -1, -1, -1, -1, -1],

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
    
    self.pieces = []
    self.dead = []


  ''' Return the board '''
  def getBoard(self):
    return self.board

  ''' Print out the board which only have own pieces '''
  def printSideBoard(self):
    pass

  ''' Check whether the given location is not occupied by other piece
      If 'enemy' is set to True, then the location will be reversed first 
  '''
  def isEmptyLoc(self, loc, enemy=False):
    x, y = loc

    if enemy == True:
      x = 9 - x
      y = 8 - y

    if self.board[x][y] != -1:
      return False

    return True

  ''' Check whether the given location is in range of the board or not
      If 'enemy' is set to True, then the location will be reversed first
  '''
  def isValidLoc(self, loc, enemy=False):
    x, y = loc

    if enemy == True:
      x = 9 - x
      y = 8 - y

    if x > -1 and x < 10 and y > -1 and y < 9:
      return True

    return False

  ''' Check whether the location is in own area '''
  def inOwnArea(self, loc):
    x, y = loc

    if x > -1 and x < 9 and y > -1 and y < 5:
      return True

    return False

  ''' Check whether the location is in own Palace '''
  def inPalace(self, loc):
    if loc in self.PALACE:
      return True

    return False

  ''' Add a piece to this board 
      Note: this function only add piece to the board, check if this action
          is permitted and valid before calling this function
  '''
  def addPiece(self, piece):
    x, y = piece.getLoc()
    self.board[x][y] = len(self.pieces)
    self.pieces.append(piece)

  ''' Move a piece to a give location of this board
      Note: this function only move piece to the given location, check if
          this action is permitted and valid before calling this function
  '''
  def movePiece(self, piece, loc):
    cur_x, cur_y = piece.getLoc()
    x, y = loc
    self.board[x][y] = self.board[cur_x][cur_y]
    self.board[cur_x][cur_y] = -1

  ''' Append a piece to the dead list '''
  def killPiece(self, piece):
    x, y = piece.getLoc()
    self.board[x][y] = -1
    self.dead.append(piece)










''' Piece Part '''
type_tuple = type(())

class PieceException(Exception):
  def __init__(self):
    pass

class LocationException(PieceException):
  pass

''' Helper Functions '''

''' Return the sum of v1 and v2
    v1 and v2 are 2D vectors
'''
def addVector(v1, v2): ## Promised ##
  return (v1[0] + v2[0], v1[1] + v2[1])


''' Return the difference from v2 to v1 (v1 - v2)
    v1 and v2 are 2D vectors
'''
def subVector(v1, v2): ## Promised ##
  return (v1[0] - v2[0], v1[1] - v2[1])


''' Return the negation of v
    v is a 2D vector
'''
def negVector(v): ## Promised ##
  return (-1 * v[0], -1 * v[1])


''' Return the direction of v
    v is a 2D vector
    e.g (+3, 0) --> (+1, 0)
        (0, -4) --> (0, -1)
'''
def getDirection(v): ## Promised ##
  x, y = v
  if x != 0:
    x /= abs(x)

  if y != 0:
    y /= abs(y)

  return (x,y)



''' Main Functions & Classes '''

''' Class Name: Piece

    Class Introduction: 
        Creating a Piece and put it to the given Xiang Qi Board
        Will form a connection with Xiang Qi Board

    Class Member:
        xiangqi_board (private): the Xiang Qi Board of one's own
        enemy_xiangqi_board (private): the Xiang Qi Board of enemy
        loc (private): the current location of this Piece
'''
class Piece:

  ''' Construct a Piece object '''
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

    self.loc = loc
    self.xiangqi_board = xiangqi_board
    self.xiangqi_board.addPiece(self)
    self.enemy_xiangqi_board = enemy_xiangqi_board



  def __str__(self):
    return 'Piece'

  ''' Return the current location '''
  def getLoc(self):
    return self.loc

  ''' Update the current location '''
  def goto(self, loc, user=True):
    if user:
      if not self.tryGoto(loc):
        return False

    self.xiangqi_board.movePiece(self, loc)
    self.loc = loc
    self.update()

    if user:
      return True

  ''' Check if the location is available '''
  def tryGoto(self, loc, user=True):
    # check if the location can be occupied (valid and empty)
    if not self.tryOccupy(loc):
      return False

    # check if the location can be reached by this piece
    if user:
      if not self.tryReach(loc):
        return False

    # check if this piece can move to the location under its own rules
    if not self.tryMove(loc):
      return False

    return True

  def tryOccupy(self, loc):
    if not self.xiangqi_board.isValidLoc(loc):
      return False

    if not self.xiangqi_board.isEmptyLoc(loc):
      return False
      
    return True

  def tryReach(self, loc):
    action = subVector(loc, self.loc)
    if action in self.ACTION:
      return True

    return False

  def tryMove(self, loc):
    return True

  def getPossibleAction(self):
    ''' Return a list of possible action

        Note: available action and possible action are not identical. available
            action means the action is possible to do for this Piece and is
            available to put this Piece to the target location, while possible
            action only focus on whether the action can be done by this Piece
    '''
    return self.ACTION

  def getAvailableTargetLoc(self):
    ''' Return a list of available target location

        Note: available action and possible action are not identical. available
            action means the action is possible to do for this Piece and is
            available to put this Piece to the target location, while possible
            action only focus on whether the action can be done by this Piece
    '''
    result = []

    for action in self.ACTION:
      loc = addVector(self.loc, action)

      if self.tryGoto(loc):
        result.append(action)

    return result

  def update(self):
    pass

  def die(self):
    self.xiangqi_board.killPiece(self)
    self.loc = (-1,-1)













class Soldier(Piece):
  def __init__(self, xiangqi_board,\
                enemy_xiangqi_board=XiangQiBoard(),\
                loc=(0,0)):
    Piece.__init__(self, xiangqi_board, enemy_xiangqi_board, loc)
    if loc[1] < 5:
      self.ACTION = [(0,1)]
    else:
      self.ACTION = [(0,1), (1,0), (-1,0)]

  def __str__(self):
    return 'Soldier'

  def update(self):
    if self.xiangqi_board.inOwnArea(loc):
      self.ACTION = [(0,1)]

    else:
      self.ACTION = [(0,1), (1,0), (-1,0)]



class Chariot(Piece):
  ACTION = [(0,1), (0,-1), (1,0), (-1,0)]

  def __str__(self):
    return 'Chariot'

  def tryReach(self, loc):
    action = subVector(loc, self.loc)
    if action[0] != 0 and action[1] != 0:
      return False
    return True

  def tryMove(self, loc):
    # check if there are some pieces between the current location and target
    #   location
    action = subVector(loc, self.loc)
    direction = getDirection(action)
    cur_loc = addVector(self.loc, direction)
    while cur_loc != loc:
      if not self.xiangqi_board.isEmptyLoc(cur_loc) or\
         not self.enemy_xiangqi_board.isEmptyLoc(cur_loc, enemy=True):
        return False
      cur_loc = addVector(cur_loc, direction)

    return True

  def getAvailableTargetLoc(self):
    result = []

    for action in self.ACTION:
      cur_loc = addVector(self.loc, action)
      while self.xiangqi_board.isValidLoc(cur_loc):
        if not self.xiangqi_board.isEmptyLoc(cur_loc):
          break

        if not self.enemy_xiangqi_board.isEmptyLoc(cur_loc, enemy=True):
          result.append(cur_loc)
          break

        result.append(cur_loc)
        cur_loc = addVector(cur_loc, action)

    return result



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

  def tryMove(self, loc):
    x, y = subVector(loc, self.loc)
    x = x - x / abs(x)
    y = y - y / abs(y)
    action = (x,y)
    loc = addVector(self.loc, action)
    if not self.xiangqi_board.isEmptyLoc(loc) or\
       not self.enemy_xiangqi_board.isEmptyLoc(loc, enemy=True):
      return False
    return True



class Cannon(Piece):
  ACTION = [(0,1), (0,-1), (1,0), (-1,0)]

  def __str__(self):
    return 'Cannon'

  def tryReach(self, loc):
    action = subVector(loc, self.loc)
    if action[0] != 0 and action[1] != 0:
      return False
    return True

  def tryMove(self, loc):
    # check if there are some pieces between the current location and target
    #   location
    action = subVector(loc, self.loc)
    direction = getDirection(action)
    cur_loc = addVector(self.loc, direction)
    num_pieces_in_between = 0
    while cur_loc != loc:
      if not self.xiangqi_board.isEmptyLoc(cur_loc) or\
         not self.enemy_xiangqi_board.isEmptyLoc(cur_loc, enemy=True):
        num_pieces_in_between += 1
      cur_loc = addVector(cur_loc, direction)

    if num_pieces_in_between == 0:
      if self.enemy_xiangqi_board.isEmptyLoc(loc, enemy=True):
        return True

    if num_pieces_in_between == 1:
      if not self.enemy_xiangqi_board.isEmptyLoc(loc, enemy=True):
        return True

    return False

  def getAvailableTargetLoc(self):
    result = []

    for action in self.ACTION:
      cur_loc = addVector(self.loc, action)
      while self.xiangqi_board.isValidLoc(cur_loc):
        if not self.xiangqi_board.isEmptyLoc(cur_loc) or\
           not self.enemy_xiangqi_board.isEmptyLoc(cur_loc, enemy=True):
          break

        result.append(cur_loc)
        cur_loc = addVector(cur_loc, action)

      cur_loc = addVector(cur_loc, action)
      while self.xiangqi_board.isValidLoc(cur_loc):
        if not self.xiangqi_board.isEmptyLoc(cur_loc):
          break

        if not self.enemy_xiangqi_board.isEmptyLoc(cur_loc, enemy=True):
          result.append(cur_loc)
          break

        cur_loc = addVector(cur_loc, action)

    return result



class Elephant(Piece):
  ACTION = [(2,2), (2,-2), (-2,2), (-2,-2)]
  def __str__(self):
    return 'Elephant'

  def tryMove(self, loc):
    # check if the location is in own area
    if not self.xiangqi_board.inOwnArea(loc):
      return False

    # check if the Elephant is obstructed
    action = subVector(loc, self.loc)
    action = getDirection(action)
    loc = addVector(self.loc, action)
    if not self.xiangqi_board.isEmptyLoc(loc) or\
       not self.enemy_xiangqi_board.isEmptyLoc(loc, enemy=True):
      return False

    return True




class Advisor(Piece):
  ACTION = [(1,1), (1,-1), (-1,-1), (-1,1)]
  def __init__(self, xiangqi_board,\
                enemy_xiangqi_board=XiangQiBoard(),\
                loc=(0,0)):
    # check if the location is in Palace
    if xiangqi_board.inPalace(loc):
      raise LocationException()
    Piece.__init__(self, xiangqi_board, enemy_xiangqi_board, loc)

  def __str__(self):
    return 'Advisor'

  def canMove(self, loc):
    # check if the location is in palace
    if not self.xiangqi_board.inPalace(loc):
      return False

    return True




class General(Piece):
  ACTION = [(0,1), (-1,0), (0,-1), (1,0)]

  def __init__(self, xiangqi_board,\
                enemy_xiangqi_board=XiangQiBoard(),\
                loc=(0,0)):
    # check if the location is in Palace
    if xiangqi_board.inPalace(loc):
      raise LocationException()
    Piece.__init__(self, xiangqi_board, enemy_xiangqi_board, loc)

  def __str__(self):
    return 'General'

  def canMove(self, loc):
    # check if the location is in palace
    if not self.xiangqi_board.inPalace(loc):
      return False

    return True







''' test functions '''
def testHorse():
  main_board = XiangQiBoard()
  horse = Horse(main_board, loc=(1,0))
  print horse.goto((2,2)) == True
  print horse.getLoc() == (2,2)
  print horse.goto((4,2)) == False
  print horse.getLoc() == (2,2)
  piece = Piece(main_board, loc=(2,3))
  print horse.goto((3,4)) == False
  print horse.getLoc() == (2,2)

def testElephant():
  main_board = XiangQiBoard()
  e = Elephant(main_board, loc=(2,0))
  e.goto((4,2))
  e.goto((6,4))
  print e.goto((4,6))
  print e.getLoc()



if __name__ == '__main__':
  testHorse()

