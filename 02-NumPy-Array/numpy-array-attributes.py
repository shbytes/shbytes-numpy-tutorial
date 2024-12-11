import numpy as np
# ndarray.shape
array_6 = np.array([12, 22, 32, 44, 45, 56]) # 1-D array
print(array_6.shape)  # Output => (6,)

array_4x2 = np.array([[12, 22], [44, 45], [82, 62], [42, 85]]) # 2-D array
print(array_4x2.shape)  # Output => (4, 2)

array_2x2x2 = np.array([[[12, 22], [44, 45]], [[82, 62], [42, 85]]]) # 3-D array
print(array_2x2x2.shape)  # Output => (2, 2, 2)

print("\n-----------------------------\n")

# ndarray.ndim
array_1 = np.array([12, 22, 32, 44, 45, 56]) # 1-D array
print(array_1.ndim)  # Output => 1

array_2 = np.array([[12, 22], [44, 45], [82, 62], [42, 85]]) # 2-D array
print(array_2.ndim)  # Output => 2

array_3 = np.array([[[12, 22], [44, 45]], [[82, 62], [42, 85]]]) # 3-D array
print(array_3.ndim)  # Output => 3

print("\n-----------------------------\n")

# ndarray.size
array_6 = np.array([12, 22, 32, 44, 45, 56]) # 1-D array
print(array_6.size)  # Output => 6

array_10 = np.array([[12, 22], [44, 45], [82, 62], [42, 85], [78, 85]]) # 2-D array
print(array_10.size)  # Output => 10

array_8 = np.array([[[12, 22], [44, 45]], [[82, 62], [42, 85]]]) # 3-D array
print(array_8.size)  # Output => 8

print("\n-----------------------------\n")
# ndarray.shape vs. ndarray.size

array_5x2 = np.array([[12, 22], [44, 45], [82, 62], [42, 85], [78, 85]]) # 2-D array
print(array_5x2.shape)  # Output => (5, 2)
print(array_5x2.size)  # Output => 10

array_2x2x2 = np.array([[[12, 22], [44, 45]], [[82, 62], [42, 85]]]) # 3-D array
print(array_2x2x2.shape)  # Output => (2, 2, 2)
print(array_2x2x2.size)  # Output => 8

print("\n-----------------------------\n")
# ndarray.dtype

array_int = np.array([12, 22, 32, 44, 45, 56]) # 1-D array
print(array_int.dtype)  # Output => int32

array_float = np.array([[12.23, 22.3], [44.6, 45.7], [82.9, 62.2], [42, 85]]) # 2-D array
print(array_float.dtype)  # Output => float64

array_complex = np.array([[[1+2j, 2+1j]], [[5+4j, 6+4j]]]) # 3-D array
print(array_complex.dtype)  # Output => complex128

print("\n-----------------------------\n")
# ndarray.itemsize

array_int = np.array([12, 22, 32, 44, 45, 56]) # 1-D array
print(array_int.itemsize)  # Output => 4

array_float = np.array([[12.23, 22.3], [44.6, 45.7], [82.9, 62.2], [42, 85]]) # 2-D array
print(array_float.itemsize)  # Output => 8

array_complex = np.array([[[1+2j, 2+1j]], [[5+4j, 6+4j]]]) # 3-D array
print(array_complex.itemsize)  # Output => 16

print("\n-----------------------------\n")
# ndarray.nbytes

array_int = np.array([12, 22, 32, 44, 45, 56]) # 1-D array
print(array_int.nbytes)  # Output => 24 (4 x 6)

array_float = np.array([[12.23, 22.3], [44.6, 45.7], [82.9, 62.2], [42, 85]]) # 2-D array
print(array_float.nbytes)  # Output => 64 (8 x 8)

array_complex = np.array([[[1+2j, 2+1j]], [[5+4j, 6+4j]]]) # 3-D array
print(array_complex.nbytes)  # Output => 64 (16 x 4)

print("\n-----------------------------\n")
# ndarray.T

array_6 = np.array([12, 22, 32, 44, 45, 56]) # 1-D array
print(array_6.T)  # Output => [12 22 32 44 45 56]

array_4x2 = np.array([[12, 22], [44, 45], [82, 62], [42, 85]]) # 2-D array
print(array_4x2.T)
# [[12 44 82 42]
#  [22 45 62 85]]
print(array_4x2.T.shape) # Output => (2, 4)

array_3x2x1 = np.array([[[12], [44]], [[82], [42]], [[22], [72]]]) # 3-D array
print(array_3x2x1.T)
# [[[12 82 22]
#   [44 42 72]]]
print(array_3x2x1.T.shape) # Output => (1, 2, 3)

print("\n-----------------------------\n")
# ndarray.real and ndarray.imag

array_complex_1d = np.array([1+2j, 2+1j]) # 1-D array
print(array_complex_1d.real)  # Output => [1. 2.]
print(array_complex_1d.imag)  # Output => [2. 1.]

array_complex_2d = np.array([[1+2j, 2+1j], [5+4j, 6+4j]]) # 2-D array
print(array_complex_2d.real)  # Output => [[1. 2.] [5. 6.]]
print(array_complex_2d.imag)  # Output => [[2. 1.] [4. 4.]]

array_complex_3d = np.array([[[1+2j, 2+1j]], [[5+4j, 6+4j]]]) # 3-D array
print(array_complex_3d.real)  # Output => [[[1. 2.]]  [[5. 6.]]]
print(array_complex_3d.imag)  # Output => [[[2. 1.]]  [[4. 4.]]]

print("\n-----------------------------\n")
# ndarray.strides

array_6 = np.array([12, 22, 32, 44, 45, 56]) # 1-D array
print(array_6.strides)  # Output => (4,)

array_4x2 = np.array([[12, 22], [44, 45], [82, 62], [42, 85]]) # 2-D array
print(array_4x2.strides) # Output => (8, 4)

array_3x2x1 = np.array([[[12], [44]], [[82], [42]], [[22], [72]]]) # 3-D array
print(array_3x2x1.strides) # Output => (8, 4, 4)

print("\n-----------------------------\n")
# ndarray.flags

array_4x2 = np.array([[12, 22], [44, 45], [82, 62], [42, 85]]) # 2-D array
print(array_4x2.flags)
#   C_CONTIGUOUS : True
#   F_CONTIGUOUS : False
#   OWNDATA : True
#   WRITEABLE : True
#   ALIGNED : True
#   WRITEBACKIFCOPY : False
