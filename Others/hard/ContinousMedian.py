import heapq

# Do not edit the class below except for
# the insert method. Feel free to add new
# properties and methods to the class.


class ContinuousMedianHandler:
    def __init__(self):
        # Write your code here.
        self.median = None
        self.__lowers = []
        self.__highers = []

    def insert(self, number):
        if not self.__lowers or number < -self.__lowers[0]:
            heapq.heappush(self.__lowers, -number)
        else:
            heapq.heappush(self.__highers, number)
        self.__rebalance_heaps()
        self.__update_median()

    def __rebalance_heaps(self):
        if abs(len(self.__lowers) - len(self.__highers)) > 1:
            if len(self.__lowers) > len(self.__highers):
                number = -heapq.heappop(self.__lowers)
                heapq.heappush(self.__highers, number)
            else:
                number = -heapq.heappop(self.__highers)
                heapq.heappush(self.__lowers, number)

    def __update_median(self):
        if len(self.__lowers) == len(self.__highers):
            self.median = (-self.__lowers[0] + self.__highers[0]) / 2
        elif len(self.__lowers) > len(self.__highers):
            self.median = -self.__lowers[0]
        else:
            self.median = self.__highers[0]

    def getMedian(self):
        return self.median


arr = [5, 10, 100]


handler = ContinuousMedianHandler()

for elem in arr:
    handler.insert(elem)
    handler.getMedian()
    print(handler.getMedian())
