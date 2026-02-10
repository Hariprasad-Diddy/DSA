def _gcd_or_hcf(a : int, b: int) -> int:
    """
    This function calculates the greatest common divisor (GCD) or highest common factor (HCF) of two numbers
    Args:
        a (int): The first number
        b (int): The second number
    Returns:
        int: The GCD or HCF of the two numbers
    """
    while b != 0:
        a,b = b,a%b
    return a

if __name__ == "__main__":
    a = int(input("Enter a number: "))
    b = int(input("Enter a number: "))
    print(_gcd_or_hcf(a, b))
