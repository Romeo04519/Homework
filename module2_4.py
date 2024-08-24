numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in numbers:
    if i == 1:
        continue
    #elif i == 2:
        #primes.append(i)
        #continue
    else:
       # is_prime = True
        for a in range(2, i+1):
            if a != i-1 and a != i:
               is_prime = i%a
               if is_prime == 0:
                   not_primes.append(i)
                   break
               else:
                   continue
            else:
                primes.append(i)
                break
print('Primes:', primes)
print('Not_primes:', not_primes)