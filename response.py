```python
from typing import Union

def add_numbers(x: Union[int, float], y: Union[int, float]) -> Union[int, float]:
  """This function adds two numbers.

  Args:
    x: The first number.
    y: The second number.

  Returns:
    The sum of x and y.
  """
  return x + y

def test_add_numbers():
    """Test cases for add_numbers function."""
    assert add_numbers(5, 3) == 8
    assert add_numbers(0, 0) == 0
    assert add_numbers(-5, 5) == 0
    assert add_numbers(5.5, 2.5) == 8.0
    assert add_numbers(0, 5.5) == 5.5
    assert add_numbers(-2.5, 7.5) == 5.0

# Example usage:
num1: int = 5
num2: int = 3
sum_result: int = add_numbers(num1, num2)
print(f"The sum of {num1} and {num2} is: {sum_result}")


if __name__ == "__main__":
    test_add_numbers()
    print("All test cases passed!")

```