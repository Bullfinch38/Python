numbers = list(range(1, 1001))
print(numbers)

odd_numbers = list(range(1,1001,2))
print(odd_numbers)
print(len(odd_numbers))

cubes = [value**3 for value in odd_numbers]
print(cubes)

n = cubes
print('Sum of digits =', sum(int(c) for c in n))

# sum_of_digits = []
for value in cubes:
    sum_of_digit = sum(int(i) for i in str(value))
    print(sum_of_digit)
    # sum_of_digits.append(sum_of_digit)
    # print(sum_of_digits)










