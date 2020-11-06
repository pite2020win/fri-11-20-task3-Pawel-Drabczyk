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
class Matrix:
  def __init__(self, n1=0, n2=0, n3=0, n4=0):
    self.r1c1 = n1
    self.r1c2 = n2
    self.r2c1 = n3
    self.r2c2 = n4

  def __add__(self, m2):
    return Matrix( self.r1c1 + m2.r1c1, self.r1c2 + m2.r1c2, self.r2c1 + m2.r2c1, self.r2c2 + m2.r2c2)  

  def __str__(self):
    return f'Printing matrix \n {self.r1c1} {self.r1c2}\n|{self.r2c1} {self.r2c2} '  

if __name__ == '__main__':
  m1 = Matrix(1, 1, 1, 1)
  m2 = Matrix(2, 2, 2, 2)
  m3 = m1 + m2
  print(m3)
