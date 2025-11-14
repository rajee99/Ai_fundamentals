import numpy as np

u = np.array([3, 2])


magnitude = np.linalg.norm(u) #In AI, physics, and math, “norm” = “how big is this vector?”
 #  linalg = Short for Linear Algebra.
unit_u = u / magnitude
print("u :", u)
print("magnitude :", magnitude)
print(unit_u)