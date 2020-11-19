#Matrix. 


#Write a class that can represent any 4𝑥4 real matrix. 
#Include two functions to calculate the sum and dot product of two matrices. 
#Next, write a program that imports this library module and use it to perform calculations.
# You CAN'T use numpy.
#Examples:
#
# matrix_1 = Matrix(4.,5.,6.,7.)
# matrix_2 = Matrix(2.,2.,2.,1.)
#
# matrix_3 = matrix_2 @ matrix_1
# matrix_4 = matrix_2 + matrix_1
# matrix_4 = 6 + matrix_1
# matrix_4 = matrix_1 + 6
#
# expand your solution to include other operations like
# - subtraction 
# - inversion
# - string representation 
#
#Try to expand your implementation as best as you can. 
#Think of as many features as you can, and try implementing them.
#Make intelligent use of pythons syntactic sugar (overloading, iterators, generators, etc)
#Most of all: CREATE GOOD, RELIABLE, READABLE CODE.
#The goal of this task is for you to SHOW YOUR BEST python programming skills.
#Impress everyone with your skills, show off with your code.
#
#Your program must be runnable with command "python task.py".
#Show some usecases of your library in the code (print some things)
#Delete these comments before commit!
#
#Good luck.
import math
import logging

class Matrix:
  def __init__(self, listOfLists):
    nRows = len(listOfLists)
    self.dim = nRows
    self.values = []
    for l in listOfLists:
      if len(l) != nRows:
        raise ValueError
      self.values.append(l)
    self.index = 0

  @staticmethod
  def fromArguments(*args):
    mSize = len(args)
    nDim = int( round(math.sqrt(mSize)) )
    listOfLists = []
    if int(math.sqrt(mSize)+0.5)**2 == mSize :
      for i in range( nDim ):
        row = []
        for j in range( nDim ):
          row.append(args[i*nDim+j])
        listOfLists.append(row)
      return Matrix(listOfLists)
    else:
      raise ValueError



  def __next__(self):
    if self.index >= self.dim**2:
      self.index = 0
      raise StopIteration
    else:
      row = int( self.index / self.dim )
      column = self.index - row*self.dim
      self.index += 1
      return self.values[row][column]

  def __iter__(self):
     return self

  def __str__(self):
    text = f'\n'
    for row in self.values:
      for i in row:
        text += str(i)
        text += ' '
      text += '\n'
    return text

  def __add__(self, other):
    tempList = []
    if isinstance(other, float) or isinstance(other, int):
      for i in self:
        tempList.append(i+other)
    elif isinstance(other, Matrix):
      if other.dim != self.dim:
        raise ValueError
      else:
        for i in range(self.dim):
          for j in range(self.dim):
            tempList.append( self.values[i][j] + other.values[i][j] )
    print(tempList)
    return Matrix( tempList )

#  def __add__(self, m2):
#    return Matrix( self.r1c1 + m2.r1c1, self.r1c2 + m2.r1c2, self.r2c1 + m2.r2c1, self.r2c2 + m2.r2c2)

#  def __str__(self):
#    return f'Printing matrix \n {self.r1c1} {self.r1c2}\n|{self.r2c1} {self.r2c2} '

if __name__ == '__main__':
  logger = logging.getLogger()
  logger.setLevel(logging.DEBUG)

  try:
    logging.info(f'Creating matrix from multiple arguments')
    m1 = Matrix.fromArguments(1, 2, 3, 4, 5, 6, 7, 8, 9)
    logging.info(m1)
    logging.info(f'Creating matrix from list of lists')
    m2 = Matrix([[-3,1,-1],[15,-6,5],[-5,2,-2]])
    logging.info(m2)
  except ValueError:
    logging.warning('Incorrect number of elements to create square matrix!!')

  try:
    logging.info(f'Adding matrixes m3 = m1 + m2')
    m3 = m1 + m2
    logging.info(m3)
    logging.info(f'Adding number to matrix m3 = m1 + 2')
    m3 = m1 + 2
    logging.info(m3)
  except ValueError:
    logging.warning(f'Not equal dimensions of matrixes')

  logging.info(f'Iterating throung the matrix!')
  for i in m1:
    logging.info(i)




  try:
    mWrong = Matrix.fromArguments(1, 1, 1)
  except ValueError:
    logging.warning("Trying to pass 3 elements to create matrix in a try block:\nIncorrect number of elements to create square matrix!!")

