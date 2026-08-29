numbers = [1, 2, 2, 3, 4]
squares = [number ** 2 for number in numbers]
even_squares = [value for value in squares if value % 2 == 0]
unique_numbers = set(numbers)
length_by_name = {name: len(name) for name in ["KoPy", "Python"]}

print("제곱:", squares)
print("짝수 제곱:", even_squares)
print("고유 개수:", len(unique_numbers))
print("길이:", length_by_name)
