def get_fibo(n):
    first_num = 1
    second_num = 1
    fibo_num = first_num + second_num
    while(n > 0):
        temp = fibo_num
        fibo_num += second_num
        second_num = fibo_num
        n -= 1
    return fibo_num

print(get_fibo(1))
