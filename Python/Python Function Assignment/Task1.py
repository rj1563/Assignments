# 1. Advanced Default and Keyword Arguments
        # Write a function calculate_salary that calculates the annual salary of an employee.
        # The function should take the following arguments:
        # base_salary (mandatory).
        # bonus_percent (default is 10%).
        # deductions (default is 5%).
        # Return the calculated annual salary after applying the bonus and deductions.
        # Call the function with different combinations of arguments, using both positional and
        # keyword arguments.

# function for calculating salary
def calculate_salary(base_salary, bonus_percent = 0.10, deductions = 0.05):
    bonus = base_salary * bonus_percent # Calculating total bonus 
    deduction = base_salary * deductions # Calculating total deduction from the base salary

    annual_salary = base_salary + bonus - deduction # Calcuting annual salary
    return annual_salary

# Default Argument
salary1 = calculate_salary(5000)
print(f"Annual Salary (default bonus and deductions): ", salary1)

# Positional Argument
salary2 = calculate_salary(5000, 0.15, 0.07)
print(f"Annual Salary (positional arguments): ", salary2)

# Keyword Argument
salary3 = calculate_salary(base_salary=5000, bonus_percent=0.3, deductions= 0.7)
print(f"Annual Salary (Keyword arguments): ", salary3)