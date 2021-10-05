def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    for i in range(len(phrase)):
        char = phrase[i]
        if char == to_swap.lower() or char == to_swap.upper():
            phrase = phrase[0:i] + char.swapcase() + phrase[i+1:]
    return phrase
