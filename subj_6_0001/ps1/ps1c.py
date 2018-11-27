"""
6.0001 Introduction to Computer Science and Programming in Python

Assignment
(https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/assignments/)

Problem Set 1C

Solved by achooan
"""


def get_float_input(prompt_msg='Enter a decimal number: '):
    try:
        value = float(input(prompt_msg))
    except ValueError:
        print('input value must be a number')
        return get_float_input(prompt_msg)

    return value


def get_savings(starting_salary, months_to_save, saving_rate,
                r=0.04, semi_annual_raise=0.07):

    monthly_salary = starting_salary / 12
    current_savings = 0

    for i in range(months_to_save):
        current_savings += current_savings * r / 12  # add interest
        current_savings += monthly_salary * saving_rate

        if i % 6 == 0:  # apply semi-annual raise
            monthly_salary += monthly_salary * semi_annual_raise
    return current_savings


def guess_saving_rate(starting_salary, months_to_save, down_payment_cost):
    high = 1
    low = 0
    guess = (high + low) / 2.0
    num_step = 0
    epsilon = 0.01

    if get_savings(starting_salary, months_to_save, high) >= down_payment_cost:
        # find the right rates only when salary is enough
        # to cover the down payment

        current_savings = get_savings(starting_salary, months_to_save, guess)

        while abs(current_savings - down_payment_cost) >= epsilon:
            if current_savings < down_payment_cost:
                low = guess
            else:
                high = guess

            num_step += 1
            # print(num_step, guess, low, high,
            #      down_payment_cost, current_savings)
            guess = (high + low) / 2.0
            current_savings = get_savings(
                starting_salary, months_to_save, guess)

        return round(guess, 6), num_step
    else:
        print('It is not possible to pay the down payment in three years')
        return None, None


if __name__ == '__main__':
    starting_salary = get_float_input('Enter the starting salary: ')

    months_to_save = 36
    total_cost = 1000000
    portion_down_payment = 0.25
    down_payment_cost = total_cost * portion_down_payment

    guess, steps = guess_saving_rate(
        starting_salary, months_to_save, down_payment_cost)

    if not guess:
        print(f'Best savings rate: {guess}')
        print(f'Steps in bisection search: {steps}')
