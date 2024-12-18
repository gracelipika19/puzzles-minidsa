def sum_if_less_than_fifty(num_one,num_two):
    total_sum = num_one + num_two

    if total_sum <50:
        return total_sum
    else:
        return None

print(sum_if_less_than_fifty(23,8))
print(sum_if_less_than_fifty(45,54))
