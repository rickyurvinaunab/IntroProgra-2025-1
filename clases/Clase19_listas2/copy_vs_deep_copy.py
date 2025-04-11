original = [[1, 2], [3, 4]]
copia = original.copy()
copia[0][0] = 99
print("Original:", original)
print("Copia:", copia)
# Original: [[99, 2], [3, 4]]
# Copia: [[99, 2], [3, 4]]

import copy
original = [[1, 2], [3, 4]]
copia_profunda = copy.deepcopy(original)
copia_profunda[0][0] = 99
print("Original:", original)   # [[1, 2], [3, 4]]
print("Copia Profunda:", copia_profunda)  # [[99, 2], [3, 4]]
