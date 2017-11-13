
def factorial_recurs(n):
    if n==0:
        val = 1
    else:
        val = n * factorial_recurs(n-1)
    return val


def draw_line(tick_length, tick_label=''):
    """Draw one line with given tick length (followed by optional label)."""
    line = '-' * tick_length
    if tick_label is not '':
        line  = "%s %s" %(line, tick_label)
    print line

def draw_interval(center_length):
    """Draw tick interval based upon a central tick length."""
    if center_length > 0: # stop when length drops to 0
        draw_interval(center_length - 1) # recursively draw top ticks
        draw_line(center_length) # draw center tick
        draw_interval(center_length - 1) # recursively draw bottom ticks

def draw_ruler(num_inches, major_length):
    """Draw English ruler with given number of inches, major tick length."""
    draw_line(major_length, 0) # draw inch 0 line
    for j in range(1, 1 + num_inches):
        draw_interval(major_length - 1) # draw interior ticks for inch
        draw_line(major_length, str(j)) # draw inch j line and label


# Binary search
def binary_search(data, target, low, high):
    """Return True if target is found in indicated portion of a Python list.

    The search only considers the portion from data[low] to data[high] inclusive.
    """
    if low > high:
        val = False
    else:
        mid = (low + high)/2
        if target == data[mid]:
            val = True
        elif target < data[mid]:
            # recur on the portion right of the middle
            val = binary_search(data, target, low, mid-1)
        else:
            # recur on the portion right of the middle
            val = binary_search(data, target, mid+1, high)

    return val

# DISK USage
import os
def disk_usage(path):
    """Return the number of bytes used by a file/folder and any descendents."""
    total = os.path.getsize(path) # account for direct usage
    if os.path.isdir(path): # if this is a directory,
        for filename in os.listdir(path): # then for each child:
            childpath = os.path.join(path, filename) # compose full path to child
            total += disk_usage(childpath) # add child's usage to total

    print '{0:<7}'.format(total), path # descriptive output (optional)
    return total # return the grand total


# reverse a sequence with recursion
def reverse_sequence(S, start, stop):
    """Reverse elements in implicit slice S[start:stop]."""
    if start < stop-1:
        S[start], S[stop-1] = S[stop-1], S[start]
        print S
        reverse_sequence(S, start+1, stop-1)

# Recursive Algorithms for computing powers
def power_recurs(x, n):
    """Compute the value x**n for integer n."""
    if n == 0:
        val = 1
    else:
        val = x * power_recurs(x, n-1)
    return val

def power_recurs2(x, n):
    """Compute the value x**n for integer n."""
    if n == 0:
        val = 1
    else:
        partial = power_recurs2(x, n/2)
        val = partial * partial
        if n%2 ==1:
            val = x * val
    return val

def binary_sum_recurs(S, start, stop):
    """Return the sum of the numbers in implicit slice S[start:stop]."""
    if start >= stop:
        val = 0
    elif start == stop-1:
        val = S[start]
    else:
        mid = (start+stop)/2
        val = binary_sum_recurs(S, start, mid) + binary_sum_recurs(S, mid, stop)
    return val


if __name__ == '__main__':
    print "factorial 10", factorial_recurs(10)
    # draw_ruler(3, 4)
    data = [2, 4, 6, 9, 10, 15, 17, 19, 21, 26, 27, 29, 34, 37, 38, 40, 42, 47]
    print binary_search(data, 38, 0, len(data))
    # print disk_usage("/Users/ujjwal/Projects/ds_python")
    print data
    # reverse_sequence(data, 0, len(data))
    print "2^^10 = ", power_recurs(2, 10)
    print "S sum from 5:7", binary_sum_recurs(data, 4, 8)