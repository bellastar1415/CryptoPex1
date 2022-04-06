import random
import math
import time
from time import perf_counter
from colorama import Fore, Style

def power(x, y, starttime):
    # Initialize result
    res = 1

    while (y > 0):

        if (time.perf_counter() - starttime) > 120:
            return -1
        # If y is odd, multiply x with result
        if ((y & 1) != 0):
            res = res * x

        # y must be even now
        y = y >> 1  # y = y/2
        x = x * x  # Change x to x^2

    return res

def PollardsRho(n, starttime):
    a = random.randrange(1, n-1)
    b = a
    count = 0
    while (perf_counter() - starttime) < 120:
        if count > 7:
            a = random.randrange(1, n - 1)
            b = a
            count = 0
        gcd = math.gcd(abs(a-b), n)
        if gcd == 1 or gcd == n:
            a = power(a, 2, starttime) + 1 % n
            b = power((power(b, 2, starttime) + 1 % n), 2, starttime) + 1 % n
            count = count + 1
            if (b == -1 or a == -1):
                return -1, -1
        else:
            print("Found a factor =", Style.BRIGHT + gcd, f"{Style.RESET_ALL}")
            print("a =", a, ", b =", b)
            print("It took", format(time.perf_counter() - starttime, '0.5f'), "seconds.")
            print(Fore.LIGHTWHITE_EX + f"===================================={Style.RESET_ALL}")
            return gcd, n/gcd
    return -1, -1

def BruteForce(n, starttime, prime1):
    max = math.isqrt(n)
    d = 1
    if prime1 != 0:     #if prime1.txt is in
        while d == 1:
            if (prime1 >= max):
                return 0
            if (time.perf_counter() - starttime) > 120:
                print("Ran out of time at factor", prime1)
                return -1
            if (n % prime1) == 0:
                print("Found a factor =", Style.BRIGHT + "", prime1, f"{Style.RESET_ALL}")
                print("It took", format(time.perf_counter() - starttime, '0.5f'), "seconds.")
                print(Fore.LIGHTWHITE_EX + f"===================================={Style.RESET_ALL}")
                return prime1
            prime1 = prime1 + 1
            if prime1 % 2 == 0 or prime1 % 3 == 0:
                prime1 = prime1 + 1
    with open("primes1.txt", 'r') as f:
        lines = f.readlines()
        for line in lines:
            for k in line.split():
                prime = int(k)
                if (time.perf_counter() - starttime) > 120:
                    print("Ran out of time at factor", prime)
                    return -1
                if (prime >= max):
                    return 0
                #print(prime)
                #print("moded = ", n % int(prime))
                if (n % prime) == 0:
                    print("Found a factor =", Style.BRIGHT + "", prime, f"{Style.RESET_ALL}")
                    print("It took", format(time.perf_counter() - starttime, '0.5f'), "seconds.")
                    print(Fore.LIGHTWHITE_EX + f"===================================={Style.RESET_ALL}")
                    return prime
    prime1 = prime
    return BruteForce(n, starttime, prime1)

def PollardsRho1(n, starttime):
    a = random.randint(1, n-1)
    b = a
    d = 1
    count = 0
    iterations = 1
    while (d == 1 and perf_counter() - starttime < 120):
        if count > 7 or a > 10000000:
            a = random.randint(1, n-1)
            b = a
            count = 0
        a = pow(a, 2) + 1 % n
        b = pow(pow(b, 2) + 1 % n, 2) + 1 % n
        d = math.gcd(abs(a - b), n)
        count = count + 1
        if (d > 1 and d < n):
            print("Found a factor =", Style.BRIGHT + "", d, f"{Style.RESET_ALL}")
            print("a =", a, ", b =", b)
            print("It took", format(time.perf_counter() - starttime, '0.5f'), "seconds.")
            print(Fore.LIGHTWHITE_EX + f"===================================={Style.RESET_ALL}")
            return d
        elif (d == n):
            print("Pollards Rho failed three times with values", a, "and", b, ".")
            print(n, "is likely prime")
            return -1
    return 0


def DixonsAlg(n, t, starttime, PrimeList, expList, count):
    if perf_counter() - starttime > 120:
        return -1
    beginExpList = len(expList)
    if t>= 10000:
        newt = t/12
    if t >= 1000:
        newt = t/6
    elif t >=200:
        newt = t/4
    elif t >= 100:
        newt = t/2
    else:
        newt = t
    while len(expList) < beginExpList + newt:
        count = count + 1
        exponent = []
        y = 1
        originalX = math.isqrt(count*n)
        newX = pow(originalX, 2) % n

        #test the factors against newX
        for i in range(t):
            k = 0
            if time.perf_counter() - starttime > 120:
                return -1
            while newX % PrimeList[i] == 0: # create a loop that adds to exponent until it is no longer divisible by that exponenet
                k = k + 1
                newX = newX / PrimeList[i]
            exponent.append(k)
        #if x has been fully factored
        if newX == 1:
            exponent.append(originalX)
            expList.append(exponent)
            perfectEquation = True
            print(len(expList), " ", originalX, "===", pow(originalX, 2, n) , end="\t")
            for i in range(t):
                #Prints out equation
                print(exponent[i], end=" ")
                #checks for perfect Eq
                if exponent[i] % 2 != 0:
                    perfectEquation = False
            print()

            if perfectEquation == True:
                perfectY = 1
                for i in range(t):
                    if exponent[i] != 0:
                        perfectY = perfectY * int(pow(PrimeList[i], exponent[i]/2)) #generate y
                gcd = math.gcd(abs(originalX-perfectY), n)
                if (gcd != 1 and gcd != n):
                    print("Equation", len(expList), "is a Perfect Equation")
                    print("Found a factor =", Style.BRIGHT +"", gcd, f"{Style.RESET_ALL}")
                    print("It took", format(time.perf_counter()-starttime, '0.3f'), "seconds.")
                    print(Fore.LIGHTWHITE_EX + f"===================================={Style.RESET_ALL}")
                    return gcd

    for base1 in expList:
        for base2 in expList:
            if base2 != base1:
                goodEq = True
                #Loop through FactorBase
                if time.perf_counter() - starttime > 120:
                    return -1
                for fb in range(t):
                    if ((base1[fb] + base2[fb]) % 2 != 0):
                        goodEq = False          #this equation combination is not good
                    if goodEq:
                        y = 1
                        for fb in range(t):
                            y = y * pow(PrimeList[fb], (base1[fb] + base2[fb])//2)
                        x = base1[t] * base2[t]
                        gcd = math.gcd(abs(x - y), n)
                        if(gcd != 1 and gcd != n):
                            print(f"Found a factor =", Style.BRIGHT + "", gcd, f"{Style.RESET_ALL}")
                            print(f"It took", format(perf_counter()-starttime, '0.4f'), "seconds.")
                            print(Fore.LIGHTWHITE_EX + f"===================================={Style.RESET_ALL}")
                            return gcd
    print(Fore.RED + "Last", len(expList), f"equations failed. Increasing number of equations...{Style.RESET_ALL}")
    if len(expList) > t*3:
        return -1
    return DixonsAlg(n, t, starttime, PrimeList, expList, count)


if __name__ == '__main__':
    PrimeList = []
    with open("primes1.txt",'r') as fp:
        lines = fp.readlines()
        for line in lines:
            for primes in line.split():
                PrimeList.append(int(primes))

    print()
    print(Style.BRIGHT + Fore.BLUE + "PEX1 - Factoring Program by the One and Only Isabella Gentile")
    print(f"CyS 431{Style.RESET_ALL}")
    print()

    n = int(input("Enter an integer you wish to factor: "))
    print()

    starttime = perf_counter()
    print(Fore.LIGHTWHITE_EX + f"===================================={Style.RESET_ALL}")
    print(Style.BRIGHT + Fore.BLUE + f"Brute Force Factoring{Style.RESET_ALL}")
    factor = BruteForce(n, starttime, 0)
    if (factor == -1):
        print(Fore.RED + f"Connection Timed Out, The Algorithm Has Exceeded Two Minutes{Style.RESET_ALL}")
        print(Fore.LIGHTWHITE_EX + f"===================================={Style.RESET_ALL}")
    elif (factor == 0):
        print(Style.BRIGHT + f"No factor was found{Style.RESET_ALL}")
        print(n, "is likely prime")
        print(Fore.LIGHTWHITE_EX + f"===================================={Style.RESET_ALL}")
    
    print(Style.BRIGHT + Fore.BLUE + f"Pollard's Rho{Style.RESET_ALL}")
    starttime = perf_counter()
    NewGCD = PollardsRho1(n, starttime)
    if NewGCD == 0:
        print(Fore.RED + f"Connection Timed Out, The Algorithm Has Exceeded Two Minutes{Style.RESET_ALL}")
        print(Fore.LIGHTWHITE_EX + f"===================================={Style.RESET_ALL}")
    if NewGCD == -1:
        print("There is no factor")

    print(Style.BRIGHT + Fore.BLUE + f"Dixon's Algorithm{Style.RESET_ALL}")
    t = int(input("Enter number of factors in factor base: "))
    starttime = perf_counter()
    timeout = DixonsAlg(n, t, starttime, PrimeList, [], 0)
    if timeout == -1:
        print(Fore.RED + f"Connection Timed Out, The Algorithm Has Exceeded Two Minutes{Style.RESET_ALL}")
        print(Fore.LIGHTWHITE_EX + f"===================================={Style.RESET_ALL}")