a = [1,2,3,5,6,7,8]

b = [5,6,7,8,1,2,3]

c = [1,2,3,5,6,7,8,1,2,3,5,6,7,8]

isRotated = True
for i in range(0, len(c)):
    if (c[i] == b[0]):
        start_index = i + 1
        for j in range(1, len(b)):
            if (c[start_index] != b[j]):
                #print(c[start_index], b[j])
                isRotated = False
            start_index += 1
        break

print isRotated
