def reverse(x):
    min_value = -2147483648
    max_value = 2147483647
    if (min_value <= x and x <= max_value):
        if x >= 0:
            reverse_ = int(str(x)[::-1])

        else:
            c = -x
            reverse_ = -int(str(c)[::-1])
    else:
        reverse_ = 0
    if (min_value <= reverse_ and reverse_ <= max_value):
        return reverse_
    else:
        return 0
