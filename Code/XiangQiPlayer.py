from Lib.XiangQiLib import *

class XiangQiGame:
  def __init__(self):
    self.board_list = [XiangQiBoard(), XiangQiBoard()]
    self.player_list = []
    self.history = []
    self.status = True

  def __str__(self):
    return 'Game'

  def addPlayer(self, player):
    if len(self.player_list) < 2:
      self.player_list.append(player)
      return True

    return False

  def removePlayer(self, player):
    self.status = True
    self.player_list.remove(player)

  def startGame(self):
    if len(self.player_list) != 2:
      return False

    for i in range(2):
      own_board = self.board_list[i]
      enemy_board = self.board_list[1-i]

      






class XiangQiPlayer:
  def __init__(self, name):
    self.name = str(name)
    self.game = None

  def __str__(self):
    return self.name

  def isPlaying(self):
    return self.status

  def attendGame(self, game):
    if game.addPlayer(self):
      self.game = game

  def quitGame(self):
    if self.game:
      self.game.removePlayer(self)
      self.game = None





def main():
  p = Player()


main()