class NumberContainers:
    def __init__(self):
        self.index_to_num = {}  # Maps index to number
        self.num_to_indices = {}  # Maps number to a sorted list of indices

    def change(self, index: int, number: int) -> None:
        # If the index already has a number, remove it from the old number's list
        if index in self.index_to_num:
            old_num = self.index_to_num[index]
            if old_num in self.num_to_indices:
                # Remove the index from the old number's list using binary search
                self._remove_from_sorted_list(self.num_to_indices[old_num], index)

        # Update the index with the new number
        self.index_to_num[index] = number

        # Add the index to the new number's list while maintaining sorted order
        if number not in self.num_to_indices:
            self.num_to_indices[number] = []
        self._insert_into_sorted_list(self.num_to_indices[number], index)

    def find(self, number: int) -> int:
        if number in self.num_to_indices and self.num_to_indices[number]:
            # Return the smallest index (first element in the sorted list)
            return self.num_to_indices[number][0]
        return -1  # Number not found

    def _insert_into_sorted_list(self, sorted_list: list, value: int) -> None:
        """Inserts a value into a sorted list while maintaining order."""
        low, high = 0, len(sorted_list)
        while low < high:
            mid = (low + high) // 2
            if sorted_list[mid] < value:
                low = mid + 1
            else:
                high = mid
        sorted_list.insert(low, value)

    def _remove_from_sorted_list(self, sorted_list: list, value: int) -> None:
        """Removes a value from a sorted list using binary search."""
        low, high = 0, len(sorted_list)
        while low < high:
            mid = (low + high) // 2
            if sorted_list[mid] < value:
                low = mid + 1
            elif sorted_list[mid] > value:
                high = mid
            else:
                sorted_list.pop(mid)
                return