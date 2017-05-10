'''def parse_int(string):
    arr = []
    answer = 0
    for char in string:
        arr.append(char)
    for i in range(len(arr) - 1, -1):
        what_to_mult_by = 10 ** i
        arr[i] = (ord(arr[i]) - 48) * what_to_mult_by
    print(arr)
    for j in range(len(arr)):
        answer += arr[j]
    return answer'''


def parse_int(string):
    arr = []
    place = 0
    answer = 0
    for char in reversed(string):
        arr.append(ord(char) - 48)
    for num in arr:
        factor = 10 ** place
        answer += num * factor
        place += 1
    return answer

print(parse_int("536"))
