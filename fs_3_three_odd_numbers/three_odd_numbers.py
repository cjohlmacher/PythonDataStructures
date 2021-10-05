def three_odd_numbers(nums):
    """Is the sum of any 3 sequential numbers odd?"

        >>> three_odd_numbers([1, 2, 3, 4, 5])
        True

        >>> three_odd_numbers([0, -2, 4, 1, 9, 12, 4, 1, 0])
        True

        >>> three_odd_numbers([5, 2, 1])
        False

        >>> three_odd_numbers([1, 2, 3, 3, 2])
        False
    """
    if len(nums) < 3:
        return False
    running_sum = sum(nums[0:3])
    for i in range(3,len(nums)):
        if running_sum % 2 == 1:
            return True
        running_sum -= nums[i-3]
        running_sum += nums[i]
    if running_sum % 2 == 1:
        return True
    return False
