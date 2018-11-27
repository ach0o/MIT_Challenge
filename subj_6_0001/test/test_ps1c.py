from subj_6_0001 import ps1c


def test_func_get_savings():
    starting_salary = 70000
    months_to_save = 36
    saving_rate = 0.1

    assert int(ps1c.get_savings(starting_salary,
                                months_to_save, saving_rate)) == int(27989)


def test_func_guess_rate():
    starting_salary = 150000
    months_to_save = 36
    down_payment_cost = 1000000 * 0.25

    guess, steps = ps1c.guess_saving_rate(
        starting_salary, months_to_save, down_payment_cost)

    assert guess == 0.416819

    actual_savings = ps1c.get_savings(starting_salary, months_to_save, guess)

    assert down_payment_cost == int(actual_savings)
