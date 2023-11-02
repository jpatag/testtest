def digit_sum(n):
    d = n // 10
    if d == 0:
        return (n % 10)
    else:
        return digit_sum(d) + (n % 10)


print(digit_sum(1234))


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # Divide the array into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Recursively sort the two halves
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # Merge the sorted halves
    merged = []
    i = j = 0
    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            merged.append(left_half[i])
            i += 1
        else:
            merged.append(right_half[j])
            j += 1
    merged += left_half[i:]
    merged += right_half[j:]

    return merged

test = [5,7,2,6,8,4,1,4]

def find_mode(arr):
    if not arr:
        return None

    # Count the occurrences of each element in the array
    counts = {}
    for num in arr:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1

    # Find the element with the maximum count
    mode = None
    max_count = 0
    for num in counts:
        if counts[num] > max_count:
            mode = num
            max_count = counts[num]

    # Recursive case: if there are ties for the mode, remove one occurrence and recurse
    ties = [num for num in counts if counts[num] == max_count]
    if len(ties) > 1:
        new_arr = [num for num in arr if num != ties[0]]
        return find_mode(new_arr)

    # Base case: if there is a unique mode, return it
    return mode

print(find_mode(test))

def check_palindrome(string):
    if len(string) < 2:
        return True
    elif string[0] == string[len(string) - 1]:
        return check_palindrome(string[1:len(string) - 1])
    else:
        return False


