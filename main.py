import linkedlist as link
from algo1 import *
from mylib import *
from calculate_expression import *

L = link.LinkedList()
link.add(L,"2+2")
link.add(L,"5-2")
link.add(L,"8*2")
link.add(L,"12/5")

L = link.revert(L)

print(calculate_expression(L,3))

