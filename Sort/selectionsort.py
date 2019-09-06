class SelectionSort():

    def __init__(self, input_list):
        self.list  = input_list

    def sort(self):
        for idx in xrange(0, len(self.list)):
            min_idx = idx
            for j in range(idx + 1, len(self.list)):
                if self.list[min_idx] > self.list[j]:
                    min_idx = j
            self.list[idx], self.list[min_idx] = self.list[min_idx], self.list[idx]
        print(self.list)


input_list = [1,7,3,5,89,4,3,2,4,5,6,7,9,78,6,3,2,56,67,4]
Sort = SelectionSort(input_list)
Sort.sort()
