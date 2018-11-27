import ps1a


def test_func_months_to_save():
    annual_salary = 120000
    portion_saved = 0.10
    total_cost = 1000000

    assert ps1a.get_months_to_save(
        annual_salary, portion_saved, total_cost) == 183

    annual_salary = 80000
    portion_saved = 0.15
    total_cost = 500000

    assert ps1a.get_months_to_save(
        annual_salary, portion_saved, total_cost) == 105
    
