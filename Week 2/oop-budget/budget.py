import csv
class Budget:

    def __init__(self, monthly_income):
        self.monthy_income = monthly_income

    def update_expenses(self):
    ##write expenses
        with open('expenses.csv', 'w', newline='') as csvfile:
            categories_name = ['Living', 'Food', 'Travel', 'Savings', 'Leisure']
            expenseswriter = csv.DictWriter(csvfile, fieldnames=categories_name, delimiter=' ',
                                    quotechar=',', quoting=csv.QUOTE_MINIMAL)
            expenseswriter.writeheader()
            expenses = {}
            for category in categories_name:
                expense = input(f'Please input your {category} expenses.')
                expenses[category] = expense

            expenseswriter.writerow(expenses)
    
    def get_expenses(self):
        with open('expenses.csv', newline='') as csvfile:
            dict_expenses = csv.DictReader(csvfile, delimiter= ' ')
            for row in dict_expenses:
                return row
             

    def update_income(self, new_income):
        self.monthy_income = new_income

    def get_percentage(self):
        expenses_dict = self.get_expenses()
        percentage_dict = {}
        total_spending = 0
        for k,v in expenses_dict.items():
            percentage_dict[k] = int(v)/self.monthy_income
            total_spending += int(v)

        percentage_dict['total_spent'] = total_spending/self.monthy_income
        return percentage_dict


        







