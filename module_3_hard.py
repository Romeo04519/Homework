def calculate_structure_sum(*args):
    sum_args = 0
    for i in args:
        if isinstance(i, int):
            sum_args = sum_args + i
        elif isinstance(i, tuple):
            calculate_structure_sum(*i)
        elif isinstance(i, set):
            calculate_structure_sum(*i)
        elif isinstance(i, list):
            calculate_structure_sum(*i)
        elif isinstance(i, str):
            sum_args = sum_args + len(i)
        elif isinstance(i, dict):
            new_list = []
            for key, vol in i.items():
                new_list.append(key)
                new_list.append(vol)
            calculate_structure_sum(new_list)
    print(sum_args)




#result = calculate_structure_sum(2,(1,2),1,[1,2,3,4],'asda',{'a': (4,1,25), 'bc': 8})
data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]
result2 = calculate_structure_sum(data_structure)

print(result2)

#result = calculate_structure_sum(data_structure)
#print(result)