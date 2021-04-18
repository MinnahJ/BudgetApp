import budget
from budget import create_spend_chart
from unittest import main

food = budget.Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
print(food.get_balance())
clothing = budget.Category("Clothing")
food.transfer(50, clothing)
clothing.withdraw(25.55)
clothing.withdraw(100)
print(clothing.get_balance())
auto = budget.Category("Auto")
auto.deposit(1000, "initial deposit")
auto.withdraw(15)
print(auto.get_balance())

print(food)
print(clothing)

print(create_spend_chart([food, clothing, auto]))


main(module='test_module', exit=False)
