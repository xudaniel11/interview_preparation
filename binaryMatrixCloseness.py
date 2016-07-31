"""
@author - Daniel Xu

Given a matrix M of number 1 and 0, for each cell in the matrix determine how far
the closest 1 is to the current cell. If the 1 is the current cell, then the distance is 0
because there is no "distance". If the 1 is next to the cell, the distance is 1.

Only consider cardinal directions (up, down, left, right) to consider the distances

1) Find all cells with value 1, add those points to a list
2) For each point inside the pointList, add adjacent points
3) Increment distance for each point (while memoizing)
4) Do not add adjacent points if you hit a boundary (go off matrix), or if the current point has been visited before
5) If the current point has been hit before, compare the current distance vs the stored distance. Store the minimum.

Essentially running a BFS from each starting point
Want to do iterative / successive expansion from the starting 1 value points
"""

import numpy as np
import sys

class BinaryMatrix:
  def __init__(self, inputMatrix):
    self.inputMatrix = inputMatrix
    self.height = inputMatrix.shape[0]
    self.width = inputMatrix.shape[1]
    self.memoMatrix = np.empty(inputMatrix.shape)
    self.memoMatrix[:] = sys.maxint

  def findAllOnes(self):
    onePointDistList = []
    for i in range(self.height):
      for j in range(self.width):
        if self.inputMatrix[i,j] == 1:
          # Setting the starting distance to be -1 for value 1 points because of the
          # recursive relation in iterativeExpand. The function automatically adds
          # a distance unit upon call.
          #
          # Therefore, the stored distance unit will be 0 for the starting points
          onePointDistList.append((i,j,-1))

    return onePointDistList


  def iterativeExpand(self, currPoint):
    i,j,oneDist = currPoint
    currDist = oneDist + 1

    if i < 0 or i >= self.height or j < 0 or j >= self.width:
      return []

    if self.memoMatrix[i,j] != sys.maxint:
      self.memoMatrix[i,j] = min(self.memoMatrix[i,j], currDist)
      return []

    self.memoMatrix[i,j] = currDist
    return [(i+1, j, currDist),
            (i, j+1, currDist),
            (i-1, j, currDist),
            (i, j-1, currDist)]


  def calculateMatrixCloseness(self):
    pointList = self.findAllOnes()
    while len(pointList) > 0:
      currPoint = pointList.pop(0)
      newPoints = self.iterativeExpand(currPoint)
      pointList.extend(newPoints)

    self.printMemoMatrix()

  def printMemoMatrix(self):
    np.set_printoptions(precision=0)
    np.set_printoptions(suppress=True)
    print np.around(self.memoMatrix)



testMatrix_1 = np.matrix([[0,0,1,0,0],[1,1,1,0,1],[1,0,1,0,0],[0,0,0,0,1],[1,0,0,0,0]])
testMatrix_2 = np.matrix([[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]])
testMatrix_3 = np.matrix([[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1]])
testMatrix_4 = np.matrix([[1,1,1,1,1],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[1,1,1,1,1]])

t1 = BinaryMatrix(testMatrix_1)
t2 = BinaryMatrix(testMatrix_2)
t3 = BinaryMatrix(testMatrix_3)
t4 = BinaryMatrix(testMatrix_4)

print "Testing\n %s" % testMatrix_1
t1.calculateMatrixCloseness()

print "\n\nTesting\n %s" % testMatrix_2
t2.calculateMatrixCloseness()

print "\n\nTesting\n %s" % testMatrix_3
t3.calculateMatrixCloseness()

print "\n\nTesting\n %s" % testMatrix_4
t4.calculateMatrixCloseness()

