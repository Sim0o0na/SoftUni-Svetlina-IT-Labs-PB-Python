n = int(input())

min = 10
sum_numbers = 0
for i in range(1, n + 1):
    # i + 1
    current_num = int(input())

    if current_num < 3 or current_num > 10:
        i -= 1
        continue

    if current_num < min:
        min = current_num

    sum_numbers += current_num

print("minimum number = " + str(min))
print("average number = " + str(sum_numbers / n))