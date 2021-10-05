def is_palindrome(phrase):
    """Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards).

        >>> is_palindrome('tacocat')
        True

        >>> is_palindrome('noon')
        True

        >>> is_palindrome('robert')
        False

    Should ignore capitalization/spaces when deciding:

        >>> is_palindrome('taco cat')
        True

        >>> is_palindrome('Noon')
        True
    """
    front,back = (0,len(phrase)-1)
    while back > front:
        if phrase[back] == " ":
            back-=1
        elif phrase[front] == " ":
            front+=1
        else:
            if phrase[front].lower() != phrase[back].lower():
                return False
            front += 1
            back -= 1
    return True