def valid_parentheses(parens):
    """Are the parentheses validly balanced?

        >>> valid_parentheses("()")
        True

        >>> valid_parentheses("()()")
        True

        >>> valid_parentheses("(()())")
        True

        >>> valid_parentheses(")()")
        False

        >>> valid_parentheses("())")
        False

        >>> valid_parentheses("((())")
        False

        >>> valid_parentheses(")()(")
        False
    """
    left_parens = 0
    for char in parens:
        if char == '(':
            left_parens += 1
        else:
            if left_parens > 0:
                left_parens -= 1
            else:
                return False
    if left_parens == 0:
        return True
    return False