class BubbleSort():
    def __init__(self, input_list):
        self.list = input_list

    def sort(self):
    # Swap the elements to arrange in order
        for iter_num in range(len(self.list)-1,0,-1):
            for idx in range(iter_num):
                if self.list[idx] > self.list[idx+1]:
                    temp = self.list[idx]
                    self.list[idx] = self.list[idx+1]
                    self.list[idx+1] = temp
        print self.list


input_list = [19,2,31,45,6,11,121,27]
Sort = BubbleSort(input_list)
Sort.sort()