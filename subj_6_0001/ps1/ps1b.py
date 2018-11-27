"""
6.0001 Introduction to Computer Science and Programming in Python

Assignment
(https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/assignments/)

Problem Set 1B

Solved by achooan
"""


def get_float_input(prompt_msg='Enter a decimal number: '):
    try:
        value = float(input(prompt_msg))
    except ValueError:
        print('input value must be a number')
        return get_float_input(prompt_msg)

    return value


def get_months_to_save(annual_salary, portion_saved, total_cost,
                       semi_annual_raise, portion_down_payment=0.25,
                       current_savings=0, r=0.04):
    monthly_salary = annual_salary / 12
    down_payment_cost = total_cost * portion_down_payment

    months_to_save = 0

    while current_savings < down_payment_cost:
        current_savings += current_savings * r / 12
        current_savings += monthly_salary * portion_saved
        months_to_save += 1

        if months_to_save % 6 == 0:  # apply semi-annual raise
            monthly_salary += monthly_salary * semi_annual_raise

    return months_to_save


if __name__ == '__main__':
    annual_salary = get_float_input('Enter your annual salary: ')
    portion_saved = get_float_input(
        'Enter the percent of your salary to save, as a decimal: ')
    total_cost = get_float_input('Enter the cost of your dream home: ')
    semi_annual_raise = get_float_input(
        'Enter the semi-annual raise, as a decimal: ')

    total_months = get_months_to_save(
        annual_salary, portion_saved, total_cost, semi_annual_raise)

    print(f'Number of months: {total_months}')
