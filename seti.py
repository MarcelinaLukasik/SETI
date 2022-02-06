def decimal_to_binary(decimal_number):
    """Returns the array of digits in binary representation of a decimal number"""
    binary = []
    while decimal_number != 0:
        modulo = decimal_number % 2
        binary.append(modulo)
        decimal_number = decimal_number // 2
    return binary[::-1]    


def binary_to_decimal(binary_digits):
    """Returns the decimal (number) representation of a binary number represented by an array of 0/1 digits"""
    decimal = 0
    for index, item in enumerate(binary_digits[::-1]):
        decimal = decimal + (2**index) * int(item)
    return decimal    


def decimal_to_base(decimal_number, destination_base):
    """Returns the digits in destination_base representation of the decimal number"""
    pass


def base_to_decimal(digits, original_base):
    """Returns the decimal (number) representation of an array of digits given in original_base"""
    pass


def digits_as_string(digits, base):
    """Returns the string representation of an array of digits given in base"""
    pass


def convert_base(original_digits, original_base, destination_base):
    """Conversion from any base to any other base"""
    pass


if __name__ == "__main__":
    table = [1, 0, 0, 0, 1, 1, 0, 1, 1]

    output = binary_to_decimal(table)
    print(output)

    print(decimal_to_binary(283))