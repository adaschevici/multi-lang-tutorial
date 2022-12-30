import pytest
from projects.calculator.calculator import Calculator


def test_works_always():
    calc = Calculator()
    assert calc.add(2, 3) == 5

def test_works_always_2():
    calc = Calculator()
    with pytest.raises(AssertionError):
        assert calc.add(2, 3) == 1

if __name__ == "__main__":
    import sys
    print(f"Version {sys.version}")
    raise SystemExit(pytest.main([__file__]))
