def interpolationSearch(sorted_list, val):
    low = 0
    high = (len(sorted_list) - 1)
    while low <= high and val >= sorted_list[low] and val <= sorted_list[high]:
        index = low + int(((float(high - low) / ( sorted_list[high] - sorted_list[low])) * ( val - sorted_list[low])))
        if sorted_list[index] == val:
            return index
        if sorted_list[index] < val:
            low = index + 1;
        else:
            high = index - 1;
    return -1


sorted_list = [1,3,4,5,7,10,13,16,20,35,45,55]

x = interpolationSearch(sorted_list, 20)
print sorted_list[x]