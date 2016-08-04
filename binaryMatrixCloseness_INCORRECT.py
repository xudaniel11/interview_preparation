"""
@author - Daniel Xu

Given a matrix M of number 1 and 0, for each cell in the matrix determine how far
the closest 1 is to the current cell. If the 1 is the current cell, then the distance is 0
because there is no "distance". If the 1 is next to the cell, the distance is 1.

Only consider cardinal directions (up, down, left, right) to consider the distances

WARNING - THIS APPROACH IS WRONG
a) DO NOT WANT TO USE DFS, WANT BFS
b) DANGER OF CYCLES == INCORRECT METHODOLOGY
c) USE binaryMatrixCloseness_v2.py !!!!!

Want to do iterative / successive expansion from the starting 1 points
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
    self.visitMatrix = np.empty(inputMatrix.shape)
    self.visitMatrix[:] = np.NAN

  def resetVisitMatrix(self):
    self.visitMatrix = np.empty(self.inputMatrix.shape)
    self.visitMatrix[:] = np.NAN

  def setClosestOne(self, i, j):
    if i < 0 or i >= self.height or j < 0 or j >= self.width:
      return sys.maxint

    if self.memoMatrix[i,j] != sys.maxint:
      return self.memoMatrix[i,j]

    if self.inputMatrix[i,j] == 1:
      self.memoMatrix[i,j] = 0
      return 0

    if self.visitMatrix[i,j] == True:
      return sys.maxint

    self.visitMatrix[i,j] = True

    #print i,j
    uDist = self.setClosestOne(i+1,j)
    lDist = self.setClosestOne(i,j+1)
    dDist = self.setClosestOne(i-1,j)
    rDist = self.setClosestOne(i,j-1)

    # if i == 2 and j == 3:
    #   print [uDist, lDist, dDist, rDist]

    self.memoMatrix[i,j] = 1 + min(uDist, lDist, dDist, rDist)
    return self.memoMatrix[i,j]


  def calculateMatrixCloseness(self):
    for i in range(self.height):
      for j in range(self.width):
        self.resetVisitMatrix()
        self.setClosestOne(i,j)

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

