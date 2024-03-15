def is_any_number_even(li):
    for i in li:
        if i % 2 == 0:
            return True
        else:
            pass
    return False


ans = is_any_number_even([1, 3, 5, 7, 9, 10])


def all_even_number(li):
    even_list = []
    for i in li:
        if i % 2 == 0:
            even_list.append(i)
        else:
            pass
    return even_list if len(even_list) > 0 else "there are no even numbers"


# all list even numbers

all_even = all_even_number([1, 3, 5, 7, 9, 10])
print(ans)
print(all_even)
