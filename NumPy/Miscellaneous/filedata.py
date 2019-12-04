import numpy as np

# Load data from file
file_data = np.genfromtxt('data.txt', delimiter=',', dtype='int32')
print(file_data)

# Boolean Masking and Advanced Indexing
print(file_data > 50)
print(file_data[file_data > 100])

# You can index with a list in NumPy
a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(a[[1, 2, 8]])

print(np.any(file_data > 50, axis=0))
print(np.all(file_data > 10, axis=0))

print("Now")
print((file_data > 50) & (file_data < 1000))
print("Inverse")
print(~((file_data > 50) & (file_data < 1000)))

array = np.array([[1, 2, 3, 4, 5],
                  [6, 7, 8, 9, 10],
                  [11, 12, 13, 14, 15],
                  [16, 17, 18, 19, 20],
                  [21, 22, 23, 24, 25],
                  [26, 27, 28, 29, 30]])

print(array[2:4, 0:2])
print(array[[0, 1, 2, 3], [1, 2, 3, 4]])
print(array[[0, 4, 5], 3:])
