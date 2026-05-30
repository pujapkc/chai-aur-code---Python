list1= [1,2,2,5,5,5,5]

freq={}

for num in list1:
  if num in freq:
    freq[num]+=1
  else:
    freq[num]=1

print(freq)

