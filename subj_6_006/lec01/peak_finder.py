"""
Peak Finder( O(log n) )

"""


def find_peak(input_list, i=0, j=None):
    if not j:
        j = len(input_list)

    if i + 1 == j:
        return i

    center_idx = (i + j) // 2

    if input_list[center_idx - 1] > input_list[center_idx]:
        return find_peak(input_list, i, center_idx)
    else:
        return find_peak(input_list, center_idx, j)


sample_list = [6, 7, 4, 3, 2, 1, 4, 5]

result_idx = find_peak(sample_list)
print(sample_list[result_idx])
