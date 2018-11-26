n = int(input())

sum_numbers = 0
# repeat number reading from input -> n times
for i in range(1, n + 1):
    current_number = int(input())
    sum_numbers = sum_numbers + current_number
# sum input number

print(sum_numbers)