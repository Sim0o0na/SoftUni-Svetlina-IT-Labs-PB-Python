account_balance = float(input())
count_of_operations = int(input())

# count_of_opeations - 1
for i in range(1, count_of_operations + 1):
    action_type = input()
    if action_type == "end":
        break
    current_sum = float(input())
    if action_type == "add":
        account_balance += current_sum
    elif action_type == "withdrawal":
        account_balance -= current_sum

    if account_balance < 0:
        break

print(account_balance)