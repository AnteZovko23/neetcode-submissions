class MinStack:
    def __init__(self):
        self.container = []
        self.min_container = []

    def push(self, val: int) -> None:
        self.container.append(val)
        if len(self.min_container) > 0:
            self.min_container.append(min(val, self.min_container[-1]))

    def pop(self) -> None:
        self.container.pop()
        self.min_container.pop()
        

    def top(self) -> int:
        return self.container[-1]
        

    def getMin(self) -> int:
        return self.min_container[-1]
        
