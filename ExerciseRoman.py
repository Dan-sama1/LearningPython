def roman(val):
    roman_num = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
    }
    result = 0
    prev = 0
    for i in val[::-1].upper():
        value = roman_num[i]
        if value < prev:
            result -= value
        else:
            result += value
        prev = value
    return result
enter = input("Enter roman numeral: ")
print(roman(enter))