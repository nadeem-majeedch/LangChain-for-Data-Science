# NumPy for Numerical Computing

## Overview
NumPy (Numerical Python) provides the foundation for numerical computing in Python. It offers fast array operations and mathematical functions.

## Key Features
- **N-dimensional arrays (ndarrays)**: Fast, memory-efficient containers
- **Vectorized operations**: Element-wise operations without loops
- **Broadcasting**: Operations on arrays of different shapes
- **Linear algebra**: Matrix operations, decompositions
- **Random number generation**: Statistical distributions

## Creating Arrays
```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5])       # From list
zeros = np.zeros((3, 4))               # 3x4 zeros
ones = np.ones((2, 3))                 # 2x3 ones
eye = np.eye(4)                        # 4x4 identity matrix
rand = np.random.randn(3, 3)           # 3x3 random normal
```

## Array Operations
```python
a + b          # Element-wise addition
a * b          # Element-wise multiplication
a @ b          # Matrix multiplication
np.dot(a, b)   # Dot product
np.sum(a)      # Sum of all elements
np.mean(a)     # Mean
np.std(a)      # Standard deviation
```

## Indexing and Slicing
```python
arr[0]         # First element
arr[1:5]       # Elements 1-4
arr[::2]       # Every other element
arr2d[0, :]    # First row
arr2d[:, 1]    # Second column
```

## Why NumPy is Fast
- Arrays are stored in contiguous memory blocks
- Operations are implemented in C, not Python
- No type checking overhead (unlike Python lists)
- Vectorization eliminates explicit loops
