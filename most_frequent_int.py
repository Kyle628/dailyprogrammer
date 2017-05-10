arr = [1 ,2, 3, 4, 5, 3]

'''
frequencies = {}

for num in arr:
    if num in frequencies:
        frequencies[num] += 1
    else:
        frequencies[num] = 1

print(frequencies)'''

most_frequent = arr[0]
highest_frequency = 0

for i in range(0, len(arr)):
    curr = arr[i]
    currfreq = 1
    for j in range(1, len(arr) - 1):
        if (curr == arr[j]):
            currfreq += 1
        if (currfreq > highest_frequency):
            most_frequent = curr

print(most_frequent)
