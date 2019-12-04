import numpy as np

a = np.array([1, 2, 3], dtype='int32')
print(a)

b = np.array([[9.0, 8.0, 7.0], [6.0, 5.0, 4.0]])
print(b)

# Get dimension
print(a.ndim)
print(b.ndim)

# Get shape
print(a.shape)
print(b.shape)

# Get type
print(a.dtype)
print(b.dtype)

# Get size
print(str(a.itemsize) + " bytes")

# Get total size
print(a.size)
print(a.nbytes)
