import math
import random

print(math.floor(-3))

# trunc   - goes towards 0

print(math.trunc(4.5))

print(random.random())

# randint()  - to get random values between any range (Return random integer in range [a, b], including both end points.)

print(random.randint(20,30))

l1 = ['2','3','5']

print(random.choice(l1))

#for correct decimal calculation

from decimal import Decimal

print(Decimal(0.1)+Decimal(0.2)-Decimal(0.2))

#sets

setone={1,2,3,4}

print(setone)

settwo={5,6,7,8,4}

print(setone & settwo) #intersection
print(setone | settwo) #union

print(setone - {1,2,3,4}) # empty set is defined as set() because empty {} define as dictionary





