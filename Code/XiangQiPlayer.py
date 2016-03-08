from Lib.XiangQiLib import *

class XiangQiPlayer:
  def __init__(self, name):
    self.name = str(name)
    self.status = True
    self.xiangqi_board = XiangQiBoard()

  def __str__(self):
    return self.name

  def isPlaying(self):
    return self.status

  def startGame(self):
    self.status = False

  def quitGame(self):
    self.xiangqi_board.clear()
    self.status = True





def main():
  p = Player()


main()