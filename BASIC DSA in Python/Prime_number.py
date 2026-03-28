n=int(input("Enter a number to check if it is prime or not\n"))

if n==1:
  print("Not a prime number")

i=2

while i<n:
  if n%i==0:
    print(f"{n} is not a prime number")
    break

  i+=1

print(f"{n} is a prime number")