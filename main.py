# 1st program
print(9 ** 0.5 * 5)

# 2nd program
print(9.99 > 9.98 and 1000 != 1000.1)

# 3rd program
result_without_priority = 2 * 2 + 2
result_with_priority = 2 * (2 + 2)
# cравнение двух результатов
print(result_without_priority)
print(result_with_priority)
print(result_without_priority == result_with_priority)

# 4th program
number_str = '123.456'
number_float = float(number_str)
shifted_number = number_float * 10
shifted_int = int(shifted_number)
first_decimal_digit = shifted_int % 10
print(first_decimal_digit)
