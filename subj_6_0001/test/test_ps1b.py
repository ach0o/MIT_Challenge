from subj_6_0001 import ps1b


def test_func_months_to_save():
    annual_salary = 120000
    portion_saved = 0.05
    total_cost = 500000
    semi_annual_raise = 0.03
    assert ps1b.get_months_to_save(
        annual_salary, portion_saved, total_cost, semi_annual_raise) == 142

    annual_salary = 80000
    portion_saved = 0.1
    total_cost = 800000
    semi_annual_raise = 0.03
    assert ps1b.get_months_to_save(
        annual_salary, portion_saved, total_cost, semi_annual_raise) == 159

    annual_salary = 75000
    portion_saved = 0.05
    total_cost = 1500000
    semi_annual_raise = 0.05
    assert ps1b.get_months_to_save(
        annual_salary, portion_saved, total_cost, semi_annual_raise) == 261
