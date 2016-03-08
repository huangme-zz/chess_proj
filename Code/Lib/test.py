from XiangQi import *

def createGame():
  xiangqi_board_list = [XiangQiBoard(), XiangQiBoard()]
  piece_list = []
  for board in xiangqi_board_list:
    pass




def main():
  b = XiangQiBoard()
  c = Horse(b)
  temp = Chariot(b, loc=(1,0))

  print c.tryGoto((2,1))

if __name__ == '__main__':
  main()
