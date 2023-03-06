# Assignment_number_1 = Linear Data Structures
# Question_number_9 = Write a program to find the smallest number using a stack.


class MinStack(object):
   min=float('inf')
   def __init__(self):
      self.min=float('inf')
      self.stack = []
   def push(self, x):
      if x<=self.min:
         self.stack.append(self.min)
         self.min = x
      self.stack.append(x)
   def pop(self):
      t = self.stack[-1]
      self.stack.pop()
      if self.min == t:
         self.min = self.stack[-1]
         self.stack.pop()
   def top(self):
      return self.stack[-1]
   def getMin(self):
      return self.min
   
obj = MinStack()
obj.push(8)
obj.push(2)
obj.push(5)
print("Smallest Number in Stack is", obj.getMin())