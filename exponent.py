def exp(num, power):
    answer = 1
    for i in range(power):
        answer *= num
    return answer

print(exp(5, 3))
