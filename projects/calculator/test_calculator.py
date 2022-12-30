from projects.calculator.calculator import Calculator


def test_works_always():
    calc = Calculator()
    assert calc.add(2, 3) == 5

def test_works_always_2():
    calc = Calculator()
    assert calc.add(2, 3) == 1

if __name__ == "__main__":
    import pytest
    import sys
    print(f"Version {sys.version}")
    raise SystemExit(pytest.main([__file__]))

# import unittest
# from projects.calculator.calculator import Calculator
# 
# class TestSum(unittest.TestCase):
#     
#     def test_sum(self):
#         calc = Calculator()
#         self.assertEqual(calc.add(2, 3), 3)
# 
# if __name__ == "__main__":
#     unittest.main()
