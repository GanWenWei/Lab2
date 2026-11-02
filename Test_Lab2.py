import ex2_5 as calc

def test_find_Min_max():
    float_list = [2,5,9,8,6,7,4,3]
    result = calc.find_min_max(float_list)
    assert result == [2,9]

def test_cal_avergae():
    float_list = [2,5,9,8,6,7,4,3]
    result = calc.calc_average(float_list)
    assert result == 5.5

def test_median_temperature():
    float_list = [2,5,9,8,6,7,4,3]
    result = calc.calc_median_temperature(float_list)
    assert result == 5.5