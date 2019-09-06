def binarySearch(sorted_list, l, r, x):
    if r >= l:
        mid = l + (r - l) / 2
        if sorted_list[mid] == x:
            return mid
        elif sorted_list[mid] > x:
            return binarySearch(sorted_list, l, mid - 1, x)
        else:
            return binarySearch(sorted_list, mid + 1, r, x)
    else:
        return -1

def exponentialSearch(sorted_list, val):
    if sorted_list[0] == val:
        return 0
    index = 1
    while index < len(sorted_list) and sorted_list[index] <= val:
        index = index * 2
    return binarySearch( sorted_list[:min(index, len(sorted_list))], 0, len(sorted_list), val)


sorted_list = [1,3,4,5,7,10,13,16,20,35,45,55]

x = exponentialSearch(sorted_list, 20)
print sorted_list[x]