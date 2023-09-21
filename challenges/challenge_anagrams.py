def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    middle = len(arr) // 2
    left_half = merge_sort(arr[:middle])
    right_half = merge_sort(arr[middle:])

    merged = []
    left_index = right_index = 0

    while left_index < len(left_half) and right_index < len(right_half):
        if left_half[left_index] < right_half[right_index]:
            merged.append(left_half[left_index])
            left_index += 1
        else:
            merged.append(right_half[right_index])
            right_index += 1

    merged.extend(left_half[left_index:])
    merged.extend(right_half[right_index:])

    return merged


def is_anagram(first_string, second_string):
    if not first_string and not second_string:
        return ('', '', False)

    def clean_and_sort(s):
        return ''.join(merge_sort(list(filter(str.isalpha, s.lower()))))

    cleaned_first = clean_and_sort(first_string)
    cleaned_second = clean_and_sort(second_string)

    is_anagram = cleaned_first == cleaned_second

    return (cleaned_first, cleaned_second, is_anagram)
