def _is_palindrome_string(value : str) -> bool:
    """
    This function checks if a string is a palindrome
    Args:
        value (str): The value to check if it is a palindrome
    Returns:
        bool: True if the value is a palindrome, False otherwise
    """
        
    value = value.lower()
    left,right = 0, len(value) - 1
    while left < right:
        if value[left] != value[right]:
            return False
        left += 1
        right -=1
    return True
    

if __name__ == "__main__":      
    print(_is_palindrome_string("HeH"))
    print(_is_palindrome_string("Hell0"))
