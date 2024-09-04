def is_prime(func):
    def wrapper(*sum):
        sum1 = func(*sum)
        interval = int(sum1/2+1)
        for i in range(2, interval):
            if sum1 % i == 0:
                print ('Составное')
        print('Простое')
        return sum1
    return wrapper


@is_prime
def sum_three(a, b, c):
    sum = a + b + c
    return sum

result = sum_three(2, 3, 6)
print(result)