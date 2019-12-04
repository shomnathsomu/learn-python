import numpy as np

# Mathematics
a = np.array([1, 2, 3])
a = a + 10
print(a)

a = a - 2
print(a)

a = a * 2
print(a)

a = a / 3
print(a)

b = np.array([3, 2, 1])
c = np.array([7, 8, 9])
c += b
print(c)

c = c**2
print(c)
print(np.sin(c))

# Linear Algebra
aa = np.ones((2, 3))
bb = np.full((3, 2), 2)
print(np.matmul(aa, bb))

# Find the determinant
d = np.identity(3)
print(np.linalg.det(d))

# Reference docs (https://docs.scipy.org/doc/numpy/reference/routines.linalg.html)
# Determinant
# Trace
# Singular Vector Decomposition
# Eigenvalues
# Matrix Norm
# Inverse
