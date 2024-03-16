def square(a):
    return a**2


lis = [1, 2, 3, 4, 5]

for i in map(square, lis):
    print(i)

print(map(square, lis))

# if we want list

lis_square = list(map(square, lis))
print(lis_square)

# filter


def check_even(num):
    return num % 2 == 0


print(filter(check_even, lis))

# to get a list
print(list(filter(check_even, lis)))

# lambda expression which is similar to annonymous function consider the square function
# syntax

# lambda num : num**2

# map list with square
print(list(map(lambda num: num**2, lis)))

# filtering even numbers

print(list(filter(lambda num: num % 2 == 0, lis)))
