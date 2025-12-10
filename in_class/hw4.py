def find_max(numbers):
    """ 
    Returns the maximum number from a list.

    >>> find_max([10, 5, 20])
    20
    >>> find_max([])
    None
    """
    if not numbers:
        return None
    max_number = numbers[0]
    for num in numbers:
        if num > max_number:
            max_number = num
    return max_number
print(find_max([10, 5, 20]))  # Output: 20
print(find_max([]))          # Output: None