def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    letter_count = dict()
    for num in nums:
        letter_count[num] = letter_count.get(num,0) + 1
    maxVal = 0
    maxKey = None
    for (key,val) in letter_count.items():
        if val > maxVal:
            maxVal = val
            maxKey = key
    return maxKey
