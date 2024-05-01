sample_list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

indices = [0, 4, 5]
result_list = [sample_list[i] for i in range(len(sample_list)) if i not in indices]

print(result_list)