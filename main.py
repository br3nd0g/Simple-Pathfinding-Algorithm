import os
import time
import random

size = 36
obstacleSize = 7

pathChar = "■"
obstacleChar = "▒"
goalReached = False
curPos = [0, 0]


def getInputs():

  xPer = int(
    input("How far along (in percentage) do you wish to set the X goal: "))
  yPer = int(
    input("How far along (in percentage) do you wish to set the Y goal: "))
  numObs = int(input("How many obstacles do you wish there to be: "))

  goal = [0, 0]
  goal[0] = (round((size / 100) * xPer)) - 1
  goal[1] = (round((size / 100) * yPer)) - 1

  return goal, numObs


def setupBoard(boardSize):

  board = [['█'] * boardSize for _ in range(boardSize)]
  board[0][0] = pathChar

  return board


def showBoard(curBoard):

  for row in curBoard:
    print("".join(row))

  if goalReached == False:
    time.sleep(0.7)
    os.system('clear')


def move(boardArray, posCoord, goalCoord):

  posBackup = [posCoord[0], posCoord[1]]

  if goalCoord == posCoord:
    return boardArray, posCoord, True

  if abs(goalCoord[0] - posCoord[0]) > abs(goalCoord[1] - posCoord[1]):

    #need to move horizontal
    if (goalCoord[0] - posCoord[0]) > 0:
      #move right
      posCoord[0] += 1
    else:
      #move left
      posCoord[0] -= 1

  elif abs(goalCoord[0] - posCoord[0]) < abs(goalCoord[1] - posCoord[1]):

    #need to move vertical
    if (goalCoord[1] - posCoord[1]) > 0:
      #move down
      posCoord[1] += 1
    else:
      #move up
      posCoord[1] -= 1

  elif abs(goalCoord[0] - posCoord[0]) == abs(goalCoord[1] - posCoord[1]):
    #move right as backup
    posCoord[0] += 1

  if boardArray[posCoord[1]][posCoord[0]] == obstacleChar:

    #coord being moved to is obstacle
    if posCoord[1] > posBackup[1]:
      #obstacle is beneath, move right
      posCoord = posBackup
      posCoord[0] += 1

    elif posCoord[0] > posBackup[0]:
      #obstacle is right, move down
      posCoord = posBackup
      posCoord[1] += 1

  boardArray[posCoord[1]][posCoord[0]] = pathChar

  return boardArray, posCoord, False


def getRandomCoord():

  xCoord = random.randint(1, size - (obstacleSize + 1))
  yCoord = random.randint(1, size - (obstacleSize + 1))

  return [xCoord, yCoord]


def placeObstacles(boardArray, amountToPlace):

  for obstacle in range(amountToPlace):

    obsOriginCoord = getRandomCoord()

    for height in range(obstacleSize):
      for width in range(obstacleSize):
        boardArray[obsOriginCoord[1]][obsOriginCoord[0] + width] = obstacleChar

      obsOriginCoord[1] += 1

  return boardArray


goal, obstacleAmount = getInputs()
board = setupBoard(size)
board = placeObstacles(board, obstacleAmount)
showBoard(board)

while goalReached != True:

  board, curPos, goalReached = move(board, curPos, goal)

  showBoard(board)
