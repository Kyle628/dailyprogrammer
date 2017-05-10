arr = [5, 6, 4, 5, 2, 3, 6, 8]

have_seen = []

'''for i in range(0, len(arr) - 1):
    curr = arr[i]
    for j in range(1, len(arr) - 1):
        if (curr + arr[j] == 10):
            print("found pair %d %d", curr, arr[j])'''

for num in arr:
    what_i_need = 10 - num
    if (what_i_need in have_seen):
        print(num, what_i_need)
    have_seen.append(num)
