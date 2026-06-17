from array import *

val= array ('i',[1,2,5])

for i in range(len(val)):
  print(val[i])

#------------------------------------------------------------------------------

arr=array('i',[])

n=int(input("Enter the length of array"))

for i in range(n):
  x=int(input("enter the next element of array"))
  arr.append(x)

print(arr)

#------------------------------------------------------------------------------------

# Three types of copy in array

#normal copy where location of array does not changes

#arr2=arr1

# Shallow copy

#arr2=arr1.view()

# deep copy - where the ids competely changes so if you do any change in one id then it will not change the second also

#arr2=arr1.copy()










