import numpy as np

# Statistics
stats = np.array([[22, 35, 66], [45, 56, 33]])
print(stats)
print(np.min(stats))
print(np.max(stats, axis=1))
print(np.sum(stats, axis=0))

