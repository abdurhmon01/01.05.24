sample_lists = [[1, 2, 3], [4, 5, 6], [10, 11, 12], [7, 8, 9]]

max_sum_list = max(sample_lists, key=lambda x: sum(x))

print("Sample lists:")
for lst in sample_lists:
    print(lst)

print("\nList with the highest sum of elements:")
print(max_sum_list)