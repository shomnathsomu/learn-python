import numpy as np

a = np.array([[1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14]])

# Get a specific element [r, c]
print(a[1, 5])

# Get a specific row
print(a[1, :])

# Get a specific column
print(a[:, 2])

# Getting a little more fancy [start_index:end_index:step_index]
print(a[0, 1:6:2])

a[1, 5] = 20
print(a)

a[:, 3] = [1, 2]
print(a)

# 3-D array example
b = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(b)
print(b[0, 1, 1])

# Get specific element (work outside in)
print(b[:, 1, :])
print(b[:, 1, 0])
print(b[0, 1, 1])

# Replace
b[:, 1, :] = [[9, 9], [8, 8]]
print(b)
