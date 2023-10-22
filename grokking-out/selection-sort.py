class List:
    def __init__(self, data=[]):
        self._data = data
    
    def __str__(self):
        return f'Data : {self._data}'
    
    @property
    def get_data(self):
        return self._data
    
    @get_data.setter
    def set_data(self, new_data_set):
        if isinstance(new_data_set, list):
            self._data = new_data_set
        # elif isinstance(new_data_set, int) or isinstance(new_data_set, float):
        #     self._data.append(new_data_set)
    
    def findSmallest(self):
        smallest = self._data[0]
        smallest_index = 0
        for i in range(1, len(self._data)):
            if self._data[i] < smallest:
                smallest = self._data[i]
                smallest_index = i
        return smallest_index
            
    def selectionSort(self):
        newArr = []
        for i in range(len(self._data)):
            smallest = self.findSmallest()
            newArr.append(self._data.pop(smallest))
            
        return newArr

myList = List([5, 3, 6, 2, 10])

print(myList._data)
print(myList._data[0])
print(myList.findSmallest())
print(myList.selectionSort())


