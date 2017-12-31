# /usr/local/bin/python3
def binary_search_iterative(data, target):
    """Return True if target is found in the given Python list."""
    low = 0
    bn_flag = False
    high = len(data) - 1
    while low <= high:
        mid = (low + high) / 2
        if target == data[mid]:  # found a match
            bn_flag = True
            break
        elif target < data[mid]:
            high = mid - 1  # only consider values left of mid
        else:
            low = mid + 1  # only consider values right of mid

    return bn_flag  # loop ended without success


def reverse_iterative(S):
    """Reverse elements in sequence S."""
    start, stop = 0, len(S)
    while start < stop - 1:
        S[start], S[stop-1] = S[stop-1], S[start] # swap first and last
        start, stop = start + 1, stop - 1 # narrow the range


if __name__ == '__main__':
    data = [2, 4, 6, 9, 10, 15, 17, 19, 21, 26, 27, 29, 34, 37, 38, 40, 42, 47]
    print (binary_search_iterative(data, 38))
    print (data)
    reverse_iterative(data)
    print (data)

