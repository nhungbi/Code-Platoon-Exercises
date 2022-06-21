# After you write all your classes, use this file to call them all together and run your program
from budget import Budget

budget1 = Budget(5000)
budget1.update_expenses()
print(budget1.get_expenses())
print(budget1.get_percentage())