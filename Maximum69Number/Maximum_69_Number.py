def maximum69Number(num):
    if (type(num) != int):
        raise TypeError("Input must be an integer")
    if len(str(num)) == str(num).count('9'):
        return num

    digits = list(str(num))

    return changeOneSixToNine(digits)


def changeOneSixToNine(digits):
    i = 0
    for digit in digits:
        if digit == '6':
            digits[i] = '9'
            digits = "".join(digits)
            return int(digits)
        i += 1
