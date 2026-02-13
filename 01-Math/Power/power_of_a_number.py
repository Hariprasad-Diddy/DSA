def _power_of_a_number(base : int, exponent_number : int) -> float:
  """
  This function calculates the power of a number
  Args:
      base number (int): The base number
      exponent_number (int): The exponent number
  Returns:
      float: The power of a number
  """

  power_of_a_number : float = 1.0
  for _ in range(exponent_number):
    power_of_a_number *= base_number
  return power_of_a_number


if __name__ == "__main__":
  base_number : int = int(input("Enter a Base number: "))
  exponent_number : int = int(input("Enter a Exponent number: "))
  print(_power_of_a_number(base = base_number,exponent_number = exponent_number))
