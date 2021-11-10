import math

def isPrime(num):
    prime = True
    if num > 1:
        for i in range(2,int(math.sqrt(num)+1)):
            if num % i == 0:
                prime = False
                break
    else:
        return f'The number {num} is invalid'
    
    return prime


for i in range(100):
    print(isPrime(i),i)