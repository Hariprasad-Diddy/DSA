def _digit_root(number : int) -> int:
    """
    This function calculates the digit root of a number
    Args:
        number (int): The number to calculate the digit root of
    Returns:
        int: The digit root of the number
    """
    counter : int = 0

    if number == 0: return 0
    number = abs(number)
    while number > 0:
        counter += number % 10
        number //= 10

    if counter < 10: return counter
    else: return digit_root(counter) 
        

if __name__ == "__main__":
    number = int(input("Enter a number: "))
    print(_digit_root(number))
