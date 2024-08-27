def calculate_structure_sum(*args):
    sum_args = 0
    for arg in args:
        if isinstance(arg, int):
            sum_args += arg
        elif isinstance(arg, (tuple, set, list)):
            sum_args += calculate_structure_sum(*arg)
        elif isinstance(arg, str):
            sum_args += len(arg)
        elif isinstance(arg, dict):
            new_list = []
            for key, vol in arg.items():
                new_list.append(key)
                new_list.append(vol)
            sum_args += calculate_structure_sum(new_list)
        # elif arg is None:
        #     pass
    return sum_args

data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]
result2 = calculate_structure_sum(data_structure)
print(result2)