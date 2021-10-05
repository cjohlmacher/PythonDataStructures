def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    num1 = str(num1)
    num2 = str(num2)
    if len(num1) != len(num2):
        return False
    dict1,dict2 = {},{}
    for i in range(len(num1)):
        dict1[num1[i]] = dict1.get(num1[i],0) + 1
        dict2[num2[i]] = dict2.get(num2[i],0) + 1
    return dict1 == dict2