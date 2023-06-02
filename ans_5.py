def plusOne(digits):
    n = len(digits)
    carry = 1

    for i in range(n - 1, -1, -1):
        digits[i] += carry

        if digits[i] < 10:
            carry = 0
            break

        digits[i] = 0

    if carry == 1:
        digits.insert(0, 1)

    return digits
print(plusOne([1,2,3]))