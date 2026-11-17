import os, sys
import json

def calc(a,b,op):
  if op=="add":
      return a+b
  elif op=="sub":
    return a-b
  elif op=="mul":
      return a*b
  else:
      return None

def evens(nums):
  result=[]
  for n in nums:
    if n%2==0:
      result.append(n)
  return result

class user:
  def __init__(self,name,age):
    self.name=name
    self.age=age
  def greet(self):
    print("Hello "+self.name+", you are "+str(self.age))

