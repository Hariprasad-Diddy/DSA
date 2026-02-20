def _product_of_digits(number : int) -> int:
    """
    This function calculates the product of the digits of a number
    Args:
        number (int): The number to calculate the product of the digits of
    Returns:
        int: The product of the digits of the number
    """

    if number == 0: return 0

    counter : int = 1
    number = abs(number)
    while number > 0:
        counter *= number % 10
        number //= 10
    return counter    

        

if __name__ == "__main__":
    number = int(input("Enter a number: "))
    print(_product_of_digits(number))
