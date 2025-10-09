def salary_input(self):
    salary = float(input("Enter a salary number: "))
    tax_rate = float(input("Enter a tax rate (0-1): "))
    return calculate_money_available_after_tax(salary, tax_rate)

def calculate_money_available_after_tax(salary, tax_rate):
    if salary < 0: 
        raise ValueError("Salary cannot be negative.")
    if not 0 <= tax_rate <= 1:
        raise ValueError("Tax rate must be between 0 and 1")
    tax_amount = salary * tax_rate
    available = salary - tax_amount
    return available

investments = []
def add_investment(name, amount, type):
    investments.append({"name": name, "amount":amount, "type":type})

def get_investments():
    return investments







 


