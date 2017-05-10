def find_non_repeat(string):
    for i in range(len(string)):
        if string[i] != string[i+1]:
            return string[i+1]

def reverse_string_quick(string):
    return string[::-1]

def reverse_string(string):
    result = ''
    for i in xrange(len(string) - 1, -1, -1):
        print(string[i])
        result += string[i]
    return result

def reverse_string_r(string):
    if (string == ''):
        return string
    else:
        return string[-1] + reverse_string_r(string[:-1])


def palindrome_r(string):
    if (len(string) < 2):
        return True
    else:
        return string[0] == string[-1] and palindrome_r(string[1:-1])

def all_unique(string):
    for i in range(0, len(string) - 1):
        if string[i] in string[:i] + string[i + 1:]:
            return False
    return True

def is_int_or_double(string):
    try:
        int(string)
        return "int"
    except:
        return "double"

def bubble_sort_r(arr):
    is_sorted = True
    for i in range(len(arr) - 1):
        if arr[i] > arr[i+1]:
            is_sorted = False
    if not is_sorted:
        for i in range(len(arr) - 1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                break
        return bubble_sort_r(arr)
    else:
        return arr

def is_p(string):
    rev_ctr = len(string) - 1
    is_p = True
    for i in range(len(string)):
        if string[i] != string[rev_ctr]:
            is_p = False
        rev_ctr -= 1
    return is_p

def shortest_p(string):
    i = 0
    p = string
    while not is_p(p):
        sub = string[:i + 1]
        tmp = p
        tmp += sub[::-1]
        if (is_p(tmp)):
            return tmp
        else:
            i += 1


#can't figure this one out
def permute(s, step = 0):
    if step == len(s):
        print "".join(s)

    for i in range(step, len(s)):
        s_copy = [c for c in s]

        s_copy[step], s_copy[i] = s_copy[i], s_copy[step]

        permute(s_copy, step + 1)




print(permute("abc"))
