from calculation.calculator import sum_array, fibonacci


def test_sum_array():
    assert sum_array([1, 2, 3, 4, 5]) == 15
    assert sum_array([-1, -2, -3, -4, 1, 2, 3, 4]) == 0


def test_fibonacci():
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(10) == 55
    assert fibonacci(20) == 6765
    assert fibonacci(30) == 832040
