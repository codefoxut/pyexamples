import copy


def max_element(S, start, stop):
    """Returns max element in sequence S."""
    if start > stop:
        val = 0
    elif start == stop - 1:
        val = S[start]
    else:
        val = max_element(S, start + 1, stop)
        if val < S[start]:
            val = S[start]

    return val


def harmonic_number(n):
    if n == 0:
        val = 0
    else:
        val = (1.0 / n) + harmonic_number(n - 1)
    print(val, n)
    return val


def isabel_sum(S):
    n = len(S)
    S2 = [S[2 * i] + S[(2 * i) + 1] for i in range((n / 2 - 1) + 1)]
    if len(S2) == 1:
        val = S2[0]
    else:
        val = isabel_sum(S2)
    print(val, S2)
    return val


def min_max_no_loop(S, start, stop):
    """find max and min element with recursion
    :param S:
    :param start:
    :param stop:
    :return:
    """
    if start > stop:
        min, max = 0, 0
    elif start == stop - 1:
        min, max = S[start], S[start]
    else:
        min, max = min_max_no_loop(S, start + 1, stop)
        if min > S[start]:
            min = S[start]
        if max < S[start]:
            max = S[start]
    print(min, max, S, start)
    return min, max


def product_with_add_sub(m, n):
    """

    Parameters
    ----------
    m
    n

    Returns
    -------

    """
    print(m, n)
    if n < m:
        m, n = n, m
    if m == 1:
        val = n
    else:
        val = n + product_with_add_sub(m - 1, n)
    print(val, m, n)
    return val


def tower_of_hanoi(n, a, b, c):
    """

    Args:
        n: height of tower
        a: tower that has discs
        b: tower on which we have to move all discs
        c: tower to help
    Returns:

    """
    if n == 1:
        print("moved disc %s from %s to %s" % (n, a, b))
    else:
        tower_of_hanoi(n - 1, a, c, b)
        print("moved disc %s from %s to %s" % (n, a, b))
        tower_of_hanoi(n - 1, c, b, a)


def all_subsets(S):
    """

    Args:
        S: Set to find all subsets

    Returns:

    """
    if len(S) == 0:
        S_sub = [set([])]
    else:
        elem = S.pop()
        S_sub = all_subsets(S)
        S_sub2 = copy.deepcopy(S_sub)
        for s1 in S_sub2:
            s1.add(elem)
            S_sub.append(s1)
    print(S_sub)
    return S_sub


def reverse_string(s):
    """

    Args:
        s:
        start:
        stop:

    Returns:

    """
    if len(s) <= 1:
        val = s
    else:
        val = reverse_string(s[1:]) + s[0]
    print(val)
    return val


def is_palindrome_recur(s):
    """

    Args:
        s:

    Returns:

    """
    print(s)
    if len(s) <= 1:
        val = True
    else:
        val = (s[0] == s[-1])
        if val:
            val = is_palindrome_recur(s[1:-1])
    print(val, s)
    return val


if __name__ == "__main__":
    data = [2, 4, 6, 9, 10, 15, 17, 19, 21, 26, 27, 29, 34, 37, 38, 40, 42, 47, 50]
    data1 = [4, 45, 78, 2, 85, 5, 63, 36, 69, 65, 78, 24, 19, 92, 83, 94, 57]
    # S_a = {10, 17, 41, 81, 90, 41, 18, 5, 9, 63, 96}
    S_a = {10, 20, 5, 11}
    data2 = data[:8]
    print("max_element", max_element(data, 0, len(data)))

    # print harmonic_number(40)
    # print isabel_sum(data2)
    # print min_max_no_loop(data1, 0, len(data1))
    # print product_with_add_sub(119, 19)
    # tower_of_hanoi(4, 'A', 'B', 'C')
    # print all_subsets(S_a)
    # print reverse_string("ujjwal tak")
    print(is_palindrome_recur("asdfgwfdsax"))
