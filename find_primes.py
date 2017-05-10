def find_primes(n):
    count = 0
    num = 2
    primes = [1]
    while (len(primes) < n):
        for i in range(2, num):
            if (num % i == 0):
                num += 1
                continue
        primes.append(num)
        num += 1

    print(primes)

find_primes(20)
