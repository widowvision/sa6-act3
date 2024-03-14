def find_maximum(lst, comp):
    max_num = lst[0]
    for num in lst[1:]:
        if comp(num, max_num) > 0:
            max_num = num
    return max_num

numbers = [10, 5, 8, 20, 15]
max_number = find_maximum(numbers, lambda x, y: x - y)
print(max_number)
