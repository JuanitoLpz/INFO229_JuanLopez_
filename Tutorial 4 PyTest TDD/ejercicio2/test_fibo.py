from prog_fibonacci import fibonacci

def test_fibo():
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(10) == 55
