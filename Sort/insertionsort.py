class InsertionSort():

    def __init__(self, input_list):
        self.list  = input_list

    def sort(self):
        for i in xrange(1, len(self.list)):
            next_element = self.list[i]
            while self.list[i-1] > next_element and i-1 >= 0:
                self.list[i] = self.list[i-1]
                self.list[i-1] = next_element
                i -= 1
        print(self.list)



list = [1,7,3,5,89,4,3,2,4,5,6,7,9,78,6,3,2,56,67,4]
Sort = InsertionSort(list)
Sort.sort()
