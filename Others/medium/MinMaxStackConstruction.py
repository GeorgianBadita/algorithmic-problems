# Feel free to add new properties and methods to the class.
class MinMaxStack:

    def __init__(self):
        self.stack = []
        self.min = None
        self.max = None

    def peek(self):
        if self.stack:
            return self.stack[-1][0]

    def pop(self):
        if self.stack:
            num = self.stack.pop()[0]
            if self.stack:
                _, next_min, next_max = self.stack[-1]

                if next_min != self.min:
                    self.min = next_min
                if next_max != self.max:
                    self.max = next_max
            else:
                self.min = None
                self.max = None

            return num

    def push(self, number):
        if not self.max and not self.min:
            self.min = self.max = number
        else:
            if number > self.max:
                self.max = number
            if number < self.min:
                self.min = number
        self.stack.append((number, self.min, self.max))

    def getMin(self):
        if self.stack:
            return self.min

    def getMax(self):
        if self.stack:
            return self.max
