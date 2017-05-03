input_str = "1 50"

input_arr = map(int, input_str.split(" "))

start = input_arr[0]
end = input_arr[1]

list_of_kaprekars = []

def is_kaprekar(n):
    square = n*n
    square_str = str(square)
    print square_str
    i = 1
    for num in square_str:
        if int(square_str[:i]) + int(square_str[i:]) == square:
            print True
        i += 1
is_kaprekar(45)
