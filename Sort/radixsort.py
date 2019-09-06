class RadixSort():

    def __init__(self, input_list):
        self.list = input_list

    def sort(self):
        RADIX = 10
        maxLength = False
        tmp, placement = -1, 1

        while not maxLength:
            maxLength = True
            # declare and initialize buckets
            buckets = [list() for _ in range(RADIX)]

            # split list between lists
            for i in self.list:
                tmp = i / placement
                buckets[tmp % RADIX].append(i)
                if maxLength and tmp > 0:
                    maxLength = False

            # empty lists into aList array
            a = 0
            for buck in buckets:
                for i in buck:
                    self.list[a] = i
                    a += 1

            # move to next digit
            placement *= RADIX
        print self.list

input_list = [3,5,7,78,4,2,45,76,44,32,12,15]
Sort = RadixSort(input_list)
Sort.sort()