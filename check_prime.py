def check_prime(num):
    if num <=1:
        return False
    
    for i in range(2,num):
        if num%i == 0:
            return False
        else:
            return True
        
num = int(input("Enter the number to check whether it is prime or not \n"))

Res  = check_prime(num)

if Res == True:
    print(f"{num} is prime")
else:
    print(f"{num} is not a prime number")
