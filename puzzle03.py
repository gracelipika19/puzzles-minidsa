def sum_even(input_nums):
    return sum(num for num in input_nums if num % 2 == 0)


print(sum_even([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))