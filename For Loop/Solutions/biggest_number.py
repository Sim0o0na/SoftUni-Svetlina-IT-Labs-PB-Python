n = int(input())

minimum_number = 1000000
for i in range(1, n + 1):
    current_num = int(input())
    if current_num < minimum_number:
        minimum_number = current_num

if minimum_number == 1000000:
    print("")
else:
    print(minimum_number)