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

sorted_list = [1,3,4,5,7,10,13,16,20,35,45,55,56]

x = binarySearch(sorted_list, 0, len(sorted_list), 20)
print sorted_list[x]