def generate_cc_number():
    # Start with a random 16-digit number
    cc_number = [random.randint(0, 9) for _ in range(16)]

    # Calculate the Luhn checksum
    total = 0
    for i in range(15, -1, -1):
        if (i % 2) == 0:
            total += cc_number[i]
        else:
            digit = cc_number[i] * 2
            if digit > 9:
                digit = (digit % 10) + 1
            total += digit
    check_digit = (10 - (total % 10)) % 10

    # Add the check digit to the end
    cc_number.append(check_digit)

    return ''.join(map(str, cc_number))

print(generate_cc_number())