
list_str = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

Primes = []
NotPrimes = []

for i in list_str:
    for j in range(2,i):
        if i % j == 0:
            NotPrimes.append(i)
            break
    if i not in NotPrimes:
        Primes.append(i)
Primes.remove(1)
print(Primes)
print (NotPrimes)