import random

class QuickSort():

    def __init__(self, input_list):
        self.list = input_list

    def sort(self, first, last):
        if first < last:
            pivot = self.partition(first, last)
            self.sort(first, pivot - 1)
            self.sort(pivot + 1, last)
        print self.list


    def partition(self, first, last):
        pivot = first + random.randrange(last - first + 1)
        self.swap(pivot, last)
        for i in range(first, last):
            if self.list[i] <= self.list[last]:
                self.swap(i, first)
                first += 1

        self.swap(first, last)
        return first


    def swap(self, x, y):
        self.list[x], self.list[y] = self.list[y], self.list[x]

input_list = [33,6,3,7,9,35,86,12,44,22,76,45]
Sort = QuickSort(input_list)
Sort.sort(0, len(input_list) -1)