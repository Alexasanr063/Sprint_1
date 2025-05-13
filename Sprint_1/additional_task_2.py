def digit_root(num):
    while num > 9:
        num = sum(int(digit) for digit in str(num))
    return num


print(digit_root(889987))
