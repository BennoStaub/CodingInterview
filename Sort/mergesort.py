class MergeSort():

    def __init__(self, input_list):
        self.list = input_list

    def sort(self, unsorted_list):
        print "unsorted list" + str(unsorted_list)
        if len(unsorted_list) <= 1:
            return unsorted_list
    # Find the middle point and devide it
        middle = len(unsorted_list) // 2
        left_list = unsorted_list[:middle]
        right_list = unsorted_list[middle:]

        left_list = self.sort(left_list)
        right_list = self.sort(right_list)
        return list(self.merge(left_list, right_list))

    # Merge the sorted halves

    def merge(self, left_half, right_half):

        res = []
        while len(left_half) != 0 and len(right_half) != 0:
            if left_half[0] < right_half[0]:
                res.append(left_half[0])
                left_half.remove(left_half[0])
            else:
                res.append(right_half[0])
                right_half.remove(right_half[0])
        if len(left_half) == 0:
            res = res + right_half
        else:
            res = res + left_half
        return res

input_list = [64, 34, 25, 12, 22, 11, 90]

Sort = MergeSort(input_list)
new_list = Sort.sort(Sort.list)
print new_list