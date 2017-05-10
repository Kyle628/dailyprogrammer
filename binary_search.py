some_arr = [1, 3, 6, 8, 9, 11, 12, 14]

some_rotated_arr = [11, 12, 14, 1, 3, 6, 8, 9]

test = [1, 3, 6, 8, 9]

def binary_search(num, arr):
    first = 0
    last = len(arr) - 1
    found = False
    while not found and first <= last:
        mid = (first + last) // 2
        if arr[mid] == num:
            found = True
        else:
            if (arr[mid] < num):
                first = mid + 1
            else:
                last = mid - 1
    return found

def rotated_binary_search(num, rotated_arr):
    found = False
    for i in range(len(rotated_arr) - 1):
        if (rotated_arr[i] > rotated_arr[i+1]):
            pivot = i + 1
    arr1 = rotated_arr[0:pivot]
    arr2 = rotated_arr[pivot:]
    found = binary_search(num, arr1)
    if not found:
        found = binary_search(num, arr2)
    return found

print(rotated_binary_search(1, some_rotated_arr))
