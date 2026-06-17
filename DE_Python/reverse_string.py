# reverse a string without using slice
str='puja'

#take a string input

#loop it in reverse order and print

i=0

#range(start, stop, step)

for i in range(len(str)-1,-1,-1):
  print(str[i],end='')

# ---------------------------------------

# with using slice

s=input("enter string ")

print(s[::-1])

# string[start : stop : step]
# start → where to begin
# stop → where to end (not included)
# step → how many positions to move each time






