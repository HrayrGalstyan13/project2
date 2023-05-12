import random

def numbers(c):
    a = random.randint(1, 6)
    b = random.randint(1, 6)
    c = a + b
    print("The sum of dice is " + str(a) + " + " + str(b) + " = " + str(c))
    return c

sum1 = 0
sum1 = numbers(sum1)
if sum1 == 7 or sum1 == 11:
    print("You won")
elif sum1 == 3 or sum1 == 2 or sum1 == 12:
    print("You lose")
else:
    print("Now your goal number is " + str(sum1))
    sum2 = 0
    sum2 = numbers(sum2)
    while sum2 != sum1 and sum2 != 7:
        sum2 = numbers(sum2)
    if sum2 == sum1:
        print("You won")
    else:
        print("You lose")
