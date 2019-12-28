import numpy as np

class Matrix:
    def __init__(self, matrix_string):
        self.matrix = []
        for myrow in matrix_string.split('\n'):
            self.matrix.append(list(map(int,myrow.split(' '))))


    def row(self, index):
        return self.matrix[index-1]

    def column(self, index):
        arr = np.asarray(self.matrix)
        return list(arr[ : , index-1])
