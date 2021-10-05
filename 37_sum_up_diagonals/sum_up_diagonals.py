def sum_up_diagonals(matrix):
    """Given a matrix [square list of lists], return sum of diagonals.

    Sum of TL-to-BR diagonal along with BL-to-TR diagonal:

        >>> m1 = [
        ...     [1,   2],
        ...     [30, 40],
        ... ]
        >>> sum_up_diagonals(m1)
        73

        >>> m2 = [
        ...    [1, 2, 3],
        ...    [4, 5, 6],
        ...    [7, 8, 9],
        ... ]
        >>> sum_up_diagonals(m2)
        30
    """
    i = 0
    j = len(matrix)-1
    k = 0
    sum = 0
    while j > -1 and i < len(matrix):
        sum += matrix[k][i]
        sum += matrix[k][j]
        i += 1
        j -= 1
        k += 1
    return sum