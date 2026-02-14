def _power_of_a_number(base_number : int,exponent_number : int) -> float:
    """
    This function calculates the power of a number
    Args:
        base_number (int): The base number
        exponent_number (int): The exponent number
    Returns:
        int: The power of the number
    """    
    power_of_a_number : float = 1
    if exponent_number == 0: return 1
    if base_number == 0 and exponent_number < 0: raise ValueError("ZeroDivisionError or ValueError")
    
    for _ in range(abs(exponent_number)):
        power_of_a_number *= base_number

    if exponent_number < 0: return 1 / power_of_a_number
    
    return power_of_a_number


if __name__ == "__main__":
  base_number : int = int(input("Enter a Base number: "))
  exponent_number : int = int(input("Enter a Exponent number: "))
  print(_power_of_a_number(base = base_number,exponent_number = exponent_number))
