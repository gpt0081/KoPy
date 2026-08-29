def transform(value, multiplier=2, offset=0):
    result = value * multiplier + offset
    return result


def apply_twice(function, value):
    return function(function(value))


def add_one(value):
    return value + 1


print(transform(5))
print(transform(5, offset=3))
print(apply_twice(add_one, 10))
