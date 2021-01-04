# Do not edit the class below except for the buildHeap,
# siftDown, siftUp, peek, remove, and insert methods.
# Feel free to add new properties and methods to the class.
class MinHeap:
    def __init__(self, array):
        # Do not edit the line below.
        self.heap = self.buildHeap(array)

    def buildHeap(self, array):
        last_leaf = int(len(array) / 2) - 1
        for i in range(last_leaf, -1, -1):
            self.siftDown(i, array)

        return array

    def siftDown(self, i, arr):
        left = 2 * i + 1
        right = 2 * i + 2
        smallest = i

        if left < len(arr) and arr[smallest] > arr[left]:
            smallest = left

        if right < len(arr) and arr[smallest] > arr[right]:
            smallest = right

        if smallest != i:
            arr[i], arr[smallest] = arr[smallest], arr[i]
            self.siftDown(smallest, arr)

    def siftUp(self, i, arr):
        parent = (i - 1) // 2 if i % 2 == 0 else i // 2

        if arr[parent] > arr[i]:
            arr[i], arr[parent] = arr[parent], arr[i]
            self.siftUp(parent, arr)

    def peek(self):
        return self.heap[0]

    def remove(self):
        to_return = self.heap[0]
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        del self.heap[-1]
        self.siftDown(0, self.heap)
        return to_return

    def insert(self, value):
        self.heap.append(value)
        self.siftUp(len(self.heap) - 1, self.heap)


arr = [48, 12, 24, 7, 8, -5, 24, 391, 24, 56, 2, 6, 8, 41]
heap = MinHeap(arr)

print(heap.heap)
heap.insert(76)
print(heap.heap)
print(heap.peek())
heap.remove()
print(heap.heap)
