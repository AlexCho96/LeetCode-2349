class NumberContainers:
#Time Limit Exceed on the test case 37/45
    def __init__(self):
        self.containers = {}
        
    def change(self, index: int, number: int) -> None:
        self.containers[index] = number        

    def find(self, number: int) -> int:
        if number not in self.containers.values():
            return -1
        min_idx = list(self.containers.keys())[list(self.containers.values()).index(number)]
        for idx, nmb in self.containers.items():
            if number == nmb and idx < min_idx:
                min_idx = idx
        return min_idx