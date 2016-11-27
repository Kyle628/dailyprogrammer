import sys

input_str = "100 80\n30 50\n130 75\n90 60\n150 85\n120 70\n200 200\n110 100"

lines = input_str.split('\n')

first_line = lines.pop(0).split(" ")

weight = int(first_line[0])

temp_tolerance = int(first_line[1])

for i,line in enumerate(lines):
    line_arr = line.split(" ")
    weight_capacity = int(line_arr[0])
    soup_temp = int(line_arr[1])
    if weight_capacity > weight and soup_temp < temp_tolerance:
        sys.stdout.write(str(i + 1) + " ")
print ''
