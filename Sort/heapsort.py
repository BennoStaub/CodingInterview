class HeapSort():

    def __init__(self, input_list):
        self.list = input_list

    def sort(self):
        # convert aList to heap
        length = len(self.list) - 1
        leastParent = length / 2
        for i in range(leastParent, -1, -1):
            self.moveDown(i, length)

        # flatten heap into sorted array
        for i in range(length, 0, -1):
            if self.list[0] > self.list[i]:
                self.swap(0, i)
                self.moveDown(0, i - 1)
        print self.list

    def moveDown(self, first, last):
        largest = 2 * first + 1
        while largest <= last:
            # right child exists and is larger than left child
            if (largest < last) and (self.list[largest] < self.list[largest + 1]):
                largest += 1

            # right child is larger than parent
            if self.list[largest] > self.list[first]:
                self.swap(largest, first)
                # move down to largest child
                first = largest;
                largest = 2 * first + 1
            else:
                return  # force exit


    def swap(self, x, y):
        tmp = self.list[x]
        self.list[x] = self.list[y]
        self.list[y] = tmp

input_list = [1,7,3,0,4,15,13,73,96,44,30]
Sort = HeapSort(input_list)
Sort.sort()