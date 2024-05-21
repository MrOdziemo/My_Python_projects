import time
import numpy as np


def multiplication(x, y):
    result = [[0, 0], [0, 0]]
    for i in range(len(x)):
        for j in range(len(y[0])):
            for k in range(len(y)):
                result[i][j] += x[i][k] * y[k][j]
    return result


array1 = np.array([[1,2,3],
                  [4,5,6]])
print(f"Macierz 1: {array1}\n")

array2 = np.array([[9,8],
                  [1,4],
                  [6,5]])
print(f"Macierz 2: {array2}\n")

start1 = time.time()
multiplication(array1.tolist(), array2.tolist())
end1 = time.time()
print(f"Mnożenie dwóch macierzy 2x3 za pomocą listy: {multiplication(array1, array2)}, czas wykonania {end1 - start1} sekund\n")

start2 = time.time()
multiplication_np = np.dot(array1, array2)
end2 = time.time()
print(f"Mnożenie dwóch macierzy 2x3 za pomocą numpy i funkcji 'doc': {multiplication_np}, czas wykonania {end2 - start2} sekund\n")
