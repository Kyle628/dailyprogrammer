def multiply(num, num_to_mult_by):
    answer = 0
    for i in range(num_to_mult_by):
        answer += num
    return answer

print(multiply(5, 3))
