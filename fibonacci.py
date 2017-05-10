def get_fibo_loop(n):
    if (n == 0):
        return 0
    a = 1
    b = 1
    for i in range(2, n):
        tmp = a
        a = b
        b += tmp
    return b

#print(get_fibo_loop(3))

def fibR(n):
 if n==1 or n==2:
  return 1
 return fibR(n-1)+fibR(n-2)

print fibR(11)
