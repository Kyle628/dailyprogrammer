arr = [1, 3, 1, 2, 2, 5, 6, 5, 6]

'''num_occur = {}

for i in range(len(arr)):
    if (arr[i] in num_occur):
        num_occur[arr[i]] += 1
    else:
        num_occur[arr[i]] = 1

print(num_occur)
for freq in num_occur:
    if (num_occur[freq] == 1):
        print(freq)'''

arr.sort()

for i in range(len(arr)):
    if (i == 0):
        if (arr[i+1] != arr[i]):
            print(arr[i])
            break
    else:
        if (arr[i-1] != arr[i] and arr[i+1] != arr[i]):
            print(arr[i])
            break

#print(arr)
