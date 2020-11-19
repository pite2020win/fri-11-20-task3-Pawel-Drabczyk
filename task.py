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
  def fromList(list):
    mSize = len(list)
    nDim = int( round(math.sqrt(mSize)) )
    listOfLists = []
    if int(math.sqrt(mSize)+0.5)**2 == mSize :
      for i in range( nDim ):
        row = []
        for j in range( nDim ):
          row.append(list[i*nDim+j])
        listOfLists.append(row)
      return Matrix(listOfLists)
    else:
      raise ValueError

  @staticmethod
  def fromArguments(*args):
    list = []
    for i in args:
      list.append(i)
    return Matrix.fromList(list)

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
        text += f'{i:.2f} '
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
    return Matrix.fromList( tempList )

  def __radd__(self, other):
    tempList = []
    if isinstance(other, float) or isinstance(other, int):
      for i in self:
        tempList.append(i+other)
      return Matrix.fromList( tempList )

  def __sub__(self, other):
    tempList = []
    if isinstance(other, float) or isinstance(other, int):
      for i in self:
        tempList.append(i-other)
    elif isinstance(other, Matrix):
      if other.dim != self.dim:
        raise ValueError
      else:
        for i in range(self.dim):
          for j in range(self.dim):
            tempList.append( self.values[i][j] - other.values[i][j] )
    return Matrix.fromList( tempList )

  def __matmul__(self, other):
    if self.dim == other.dim:
      dotProduct = 0
      for i in range(self.dim):
        for j in range(self.dim):
          dotProduct += self.values[i][j]*other.values[i][j]
      return dotProduct
    else:
      raise ValueError

  def __mul__(self, other):
    tempList = []
    if isinstance(other, float) or isinstance(other, int):
      for i in self:
        tempList.append(i*other)
    elif isinstance(other, Matrix):
      if other.dim != self.dim:
        raise ValueError
      else:
        for i in range(self.dim):
          for j in range(self.dim):
            tempList.append( self.values[i][j] * other.values[i][j] )
    return Matrix.fromList( tempList )

  def __rmul__(self, other):
    tempList = []
    if isinstance(other, float) or isinstance(other, int):
      for i in self:
        tempList.append(i*other)
      return Matrix.fromList( tempList )

  def __truediv__(self, other):
    tempList = []
    if isinstance(other, float) or isinstance(other, int):
      for i in self:
        tempList.append(i*1./other)
    elif isinstance(other, Matrix):
      if other.dim != self.dim:
        raise ValueError
      else:
        for i in range(self.dim):
          for j in range(self.dim):
            tempList.append( self.values[i][j] * 1. / other.values[i][j] )
    return Matrix.fromList( tempList )

if __name__ == '__main__':
  logger = logging.getLogger()
  logger.setLevel(logging.DEBUG)

  try:
    logging.info(f'Creating matrix from multiple arguments')
    m1 = Matrix.fromArguments(1, 2, 3, 4, 5, 6, 7, 8, 9)
    logging.info(m1)
    logging.info(f'Creating matrix from list of lists')
    m2 = Matrix([[9,8,7],[6,5,4],[3,2,1]])
    logging.info(m2)
    logging.info(f'Creating matrix from list')
    m3 = Matrix([[1,0,0],[0,1,0],[0,0,1]])
    logging.info(m3)
  except ValueError:
    logging.warning('Incorrect number of elements to create square matrix!!')

  try:
    logging.info(f'Adding matrixes m4 = m1 + m2')
    m4 = m1 + m2
    logging.info(m4)
    logging.info(f'Adding number to matrix m4 = m1 + 2')
    m4 = m1 + 2
    logging.info(m4)
    logging.info(f'Adding number to matrix m4 =  2 + m1')
    m4 = 2 + m1
    logging.info(m4)

    logging.info(f'Subtracting matrixes m4 = m1 - m2')
    m4 = m1 - m2
    logging.info(m4)
    logging.info(f'Subtracting number from matrix m4 = m1 - 2')
    m4 = m1 - 2
    logging.info(m4)

    logging.info(f'Multiplying matrixes m4 = m1 * m2')
    m4 = m1 * m2
    logging.info(m4)
    logging.info(f'Multiplying matrix by number m4 = m1 * 2')
    m4 = m1 * 2
    logging.info(m4)
    logging.info(f'Multiplying number by matrix m4 =  2 * m1')
    m4 = 2 * m1
    logging.info(m4)

    logging.info(f'Division of matrixes m4 = m1 / m2')
    m4 = m1 / m2
    logging.info(m4)
    logging.info(f'Dividing matrix by number m4 = m1 / 2')
    m4 = m1 / 2
    logging.info(m4)

    logging.info(f'Dot product of two matrices m1 @ m3 = {m1 @ m3}')

  except ValueError:
    logging.warning(f'Not equal dimensions of matrixes')

  logging.info(f'Iterating throung the matrix!')
  for i in m2:
    logging.info(i)

  try:
    mWrong = Matrix.fromArguments(1, 1, 1)
  except ValueError:
    logging.warning("Trying to pass 3 elements to create matrix in a try block:\nIncorrect number of elements to create square matrix!!")

