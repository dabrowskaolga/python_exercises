number_list = [5, 8, 2, 3, 7, 10]
max_number = number_list[0]

for i in range(1, len(number_list)):
    if number_list[i] > max_number:
        max_number = number_list[i]

print(max_number)

min_number = number_list[0]
for i in range(1, len(number_list)):
    if number_list[i] < min_number:
        min_number = number_list[i]

print(min_number)
