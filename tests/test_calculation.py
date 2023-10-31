from calculation.calculator import sum_array


def test_sum_array():
    assert sum_array([1, 2, 3, 4, 5]) == 15
    assert sum_array([-1, -2, -3, -4, 1, 2, 3, 4]) == 0
