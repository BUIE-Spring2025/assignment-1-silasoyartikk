def int_to_roman(num):
    """
    Convert an integer to a Roman numeral.

    :param num: Integer value between 1 and 3999 inclusive.
    :return: A string representing the Roman numeral of the integer.
    """
    
    x = ""
    if num < 1 or num > 3999:
        return None

    x += num // 1000 * "M"
    num = num - ((num // 1000) * 1000)
    if num // 100 < 4:
        x += num // 100 * "C"
    elif num // 100 == 4:
        x += "CD"
    elif num // 100 == 5:
        x += "D"
    elif num // 100 > 5 and num // 100 < 9:
        x += "D" + ((num // 100)-5) * "C"
    else:
        x += "CM"
    num = num - ((num // 100) * 100)
    if num // 10 < 4:
        x += num // 10 * "X"
    elif num // 10 == 4:
        x += "XL"
    elif num // 10 == 5:
        x += "L"
    elif num // 10 > 5 and num // 10 < 9:
        x += "L" + ((num // 10)-5) * "X"
    else:
        x += "XC"
    num = num - ((num // 10) * 10)
    if num < 4:
        x += num * "I"
    elif num == 4:
        x += "IV"
    elif num == 5:
        x += "V"
    elif num> 5 and num< 9:
        x += "V" + (num-5)* "I"
    else:
        x += "IX"
    return x