class ShellSort():

    def __init__(self, input_list, gaps):
        self.list  = input_list
        self.gaps = gaps

    def sort(self):
        while len(self.gaps) > 0:
            gap = self.gaps.pop()
            for i in range(gap, len(self.list)):
                temp = self.list[i]
                j = i
                while j >= gap and self.list[j - gap] > temp:
                    self.list[j] = self.list[j - gap]
                    j = j - gap
                    self.list[j] = temp
        print(self.list)


input_list = [1,7,3,5,89,4,3,2,4,5,6,7,9,78,6,3,2,56,67,4]
gaps = [1,2,4,8]
Sort = ShellSort(input_list, gaps)
Sort.sort()
