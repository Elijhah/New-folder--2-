# ! Bank account amount
# !Take amounts from account
# 

customer_name = input("Welcome, what is your name?")
starting_balance = 5000.25
print(customer_name, 'your starting balance is ', starting_balance)

pay_check = float(input("How much would you like to deposit? "))
deposit = input("Looks like you went shopping. What did you buy?")
price = float(input("How much was the " + str(deposit) ))

balance = starting_balance - price

print("Good day, Elijhah. Your starting account is now $" + str(balance))