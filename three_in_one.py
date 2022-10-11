# Author: Lorenzo La Corte

# the goal is to implement three stacks with one array in the efficient possible way

# I'll use 3 portions of the single array: [0, N/3), [N/3, 2N/3), [2N/3, N)

# When the client pushes on a portion that is full, that will expand dinamically, shifting other portions towards right
# The array must be circular so that the last element shift to the start

from collections import deque

class Stacks:
  def __init__(self, capacity):
    self.numStacks = 3
    self.size = 0
    self.capacity = capacity
    self.list = [None] * capacity
    self.start = [0, capacity//self.numStacks, 2*capacity//self.numStacks]
    self.end = [0, capacity//self.numStacks, 2*capacity//self.numStacks]


  def shift(self, stackNum: int) -> None:
    # if elem in position end is not None we should shift the next array
    if(self.list[self.end[stackNum]] != None):
        stackNumF = stackNum+1 if stackNum+1 < self.numStacks else 0
        self.shift(stackNumF)

    # otherwise let's shift
    newEnd = self.end[stackNum] + 1 if self.end[stackNum] + 1 < self.capacity else 0
    while self.start[stackNum] != self.end[stackNum]:
        self.list[self.end[stackNum]] = self.list[self.end[stackNum]-1]     
        self.end[stackNum] = self.end[stackNum] - 1 if self.end[stackNum] - 1 >= 0 else (self.capacity-1)

    self.start[stackNum] = self.start[stackNum] + 1 if self.start[stackNum] + 1 < self.capacity else 0
    self.end[stackNum] = newEnd

  def push(self, stackNum: int, elem: int) -> None:
    if stackNum >= self.numStacks:  raise Exception("Out of Bound.")
    if(self.size == self.capacity): raise Exception("Array is Full.")
    self.size += 1

    # if full shift elements to right
    stackNumF = stackNum+1 if stackNum+1 < self.numStacks else 0
    if(self.end[stackNum] == self.start[stackNumF]):
        self.shift(stackNumF)

    self.list[self.end[stackNum]] = elem
    self.end[stackNum] = self.end[stackNum] + 1 if self.end[stackNum] + 1 < self.capacity else 0
    return

  def pop(self, stackNum: int) -> int:
    # check if it's empty
    if(self.list[self.start[stackNum]] == None): raise Exception("This Stack is Empty.")
    self.size -= 1

    elem = self.list[self.end[stackNum]-1]
    self.list[self.end[stackNum]-1] = None
    self.end[stackNum] = self.end[stackNum] - 1 if self.end[stackNum] - 1 >= 0 else (self.capacity-1)
   
    return elem

  def printStack(self):
    print(self.list)

# testcase
stacks = Stacks(15)

for i in range(5): stacks.push(0, 1)
print(stacks.pop(0))
for i in range(3): stacks.push(0, 11)
for i in range(5): stacks.push(1, 2)
for i in range(3): stacks.push(2, 3)
print(stacks.pop(0))
for i in range(1): stacks.push(1, 22)
stacks.printStack()
