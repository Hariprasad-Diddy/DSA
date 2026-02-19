def _lcm_of_two_numbers(first_num: int, second_num: int) -> int:
    """
    Compute and print the LCM for two integers.

    Args:
        first_num: First integer input.
        second_num: Second integer input.

    Returns:
        The LCM of the two numbers.
    """
    gcd_value = first_num
    original_second = second_num
    while second_num != 0:
        gcd_value, second_num = second_num, gcd_value % second_num
    print("GCD : ", gcd_value)
    lcm_value = (first_num * original_second) // gcd_value
    print("LCM : ", lcm_value)
    return lcm_value

if __name__ == "__main__":
    a = int(input("Enter a number: "))
    b = int(input("Enter a number: "))
    print(_lcm_of_two_numbers(a, b))
