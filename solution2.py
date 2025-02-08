class NumberContainers:
    def __init__(self):
        self.containers = {}
        self.leastIndexForValue = {}
        
    def change(self, index: int, number: int) -> None:
        if index in self.containers.keys():
            self.leastIndexForValue[self.containers[index]].remove(index)
            if len(self.leastIndexForValue[self.containers[index]]) == 0:
                del self.leastIndexForValue[self.containers[index]]
        self.containers[index] = number
        try:
            self.leastIndexForValue[number].append(index)
            self.leastIndexForValue[number].sort()
        except:
            self.leastIndexForValue[number] = [index]

    def find(self, number: int) -> int:
        return self.leastIndexForValue.get(number)[0] if number in self.leastIndexForValue.keys() else -1