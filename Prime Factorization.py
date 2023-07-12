###Prime Factorization####

###Have the user enter a number and find all Prime Factors (if there are any) and display them.##

import math

def Prime_num(n):
    prime_num = []
    while True:
        if n % 2 ==0:
            n = n / 2
        else:
            break

    for i in range(3,int(math.sqrt(n))+1,2):
        while (n % i == 0):
            prime_num.append(i)
            n = n/i
    print(f"Prime Factors: {prime_num}")

while True:
    x  = input("Please Enter a Number: ")

    if x.isnumeric():
        ab = int(x)
        break

Prime_num(int(x))
