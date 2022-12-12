from algo1 import *
from math import *

def search(array, element):
  for i in range(len(array)):
    if (array[i] == element):
      return i
  return None


def insert(array, element, position):
    if (position < len(array) and position >= 0):
      for i in range(len(array) - 1, position, -1):
        array[i] = array[i-1]

      array[position] = element

      return position

    else:

      return None


def delete(array, element):
  n = search(array, element)
  if (n != None):
    array[n] = None
    for i in range(n, len(array)-1):
      array[i] = array[i+1]
    array[len(array)-1] = None
    return n
  else:
    return None


def length(array):
  long = 0
  for i in range(len(array)):
    if (array[i] != None):
      long += 1
  return long
