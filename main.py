import numpy as np
from numpy import random

numbers = np.zeros(10)  ##creating an array of 10 0's
print(numbers)
matrix = np.zeros((3,4,6))  #creating matrix of 3x4(RXC) containing 0's
print(matrix)
n=[1,2,3,4,5]
print(n[:2]) #slicing just like def pythoin
n1=np.array(n)
print(type(n1))  #converting list to np array type

print(len(n1))  #checking length of array
print(n1.itemsize)  # checking bitesize of the array
print(n1.dtype) #checking data type

#Arange function
a = np.arange(1,20,2) #start to make array from 1 until 20 with incr of 2 default is 1 if not mentioned
print(list(a))


#Dimesion and operators
print(matrix.ndim)  #check dimension of the array
print(matrix<=1)  #comparing matrix with the int

#checking min max sum
b = np.linspace(1, 10, 20) #creating list from 1-10 with 20 elements
print(list(b))
print(b.max())
print(b.min())
print(b.sum())


#using ramdoms from numpy

rand =random.randint(20) #generating random int form 0-20 
rand_n = random.randint(100,size=20) #gen rands from 0-100 of 20 elements
rand1=random.rand(10) # gen 10 random numbers random form if not arg only one
rand_matrix =random.rand(3,4) #array of (3,4) random
print(rand_n)
print(random.choice(rand_n))

#using axis to sum row and columns
axe_sum0 = rand_matrix.sum(axis=0) #1 for row and 0 for column
print(axe_sum0)
axe_sum1 = rand_matrix.sum(axis=1)
print(axe_sum1)

#more mathmatical functions w array
sqrt = np.sqrt(rand_matrix)
print(sqrt)
std = np.std(rand_matrix) #standard deviation
print(std)

#all other sum div mul sub are as std

#Stacking  
s1 =random.randint(0,10,size=(3,3))
s2 =random.randint(0,10,size=(3,3))
print("--------I am are here now---------")
print(s1)
print(s2)
print(np.vstack((s1,s2)))
print(np.hstack((s1,s2)))
