num = 12345
sum_of_digits = lambda n: sum(int(digit) for digit in str(n))
print(sum_of_digits(num))
