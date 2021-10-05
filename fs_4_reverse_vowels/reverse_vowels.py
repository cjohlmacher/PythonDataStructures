def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which re not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """
    i = 0
    j = len(s)-1
    while j > i:
        while s[i] not in 'aeiouAEIOU' and i < len(s)-1:
            i += 1
        while s[j] not in 'aeiouAEIOU' and j >= 0:
            j -= 1
        if j > i:
            s = s[0:i]+s[j]+s[i+1:j]+s[i]+s[j+1:]
        i += 1
        j -= 1
    return s