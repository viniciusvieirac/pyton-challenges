def validate_list(nums):
    if not all(isinstance(num, int) and
               num >= 0 for num in nums) or len(nums) <= 1:
        return False
    return True


def find_duplicate(nums):
    if not validate_list(nums):
        return False

    numbers = set()
    for num in nums:
        if num in numbers:
            return num
        numbers.add(num)

    return False
