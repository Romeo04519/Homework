my_lyst = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
time_cycle = 1
my_lyst_index = 0
while time_cycle <= len(my_lyst):
    if my_lyst[my_lyst_index] > 0:
        print(my_lyst[my_lyst_index])
        my_lyst_index += 1
        time_cycle += 1
        continue
    elif my_lyst[my_lyst_index] == 0:
        my_lyst_index += 1
        time_cycle += 1
        continue
    else:
        break
print('я встретил отрицательное число или список закончился')