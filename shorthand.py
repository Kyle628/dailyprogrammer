line = "1,3,7,2,4,1"

list_of_nums = map(int, line.split(','))

result = ''

how_much_to_add = 0
for i,num in enumerate(list_of_nums):
    if num < list_of_nums[i-1]:
        how_much_to_add += 10
        result += str(num + how_much_to_add) + " "
    else:
        result += str(num + how_much_to_add) + " "

print result
