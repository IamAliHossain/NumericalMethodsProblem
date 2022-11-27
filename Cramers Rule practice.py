import numpy as np

from scipy import linalg

# slove this problem
# 0.3x + 0.52y + z = -.01
# 0.5x + y + 1.9z = 0.67
# 0.1x + 0.3y 0.5z = -0.44

a = np.array([[0.3, 0.52, 1],
            [0.5, 1, 1.9],
            [0.1, 0.3, 0.5]],
            float)

ax = np.array([[-0.01, 0.52, 1],
            [0.67, 1, 1.9],
            [-0.44, 0.3, .5]],
            float)
ay = np.array([[0.3, -0.01, 1],
            [0.5, 0.67, 1.9],
            [0.1, -0.44, .5]],
            float)
az = np.array([[0.3, 0.52, -0.01],
            [0.5, 1, 0.67],
            [0.1, 0.3, -0.44]],
            float)


det_A = np.linalg.det(a)
det_Ax = np.linalg.det(ax)
det_Ay = np.linalg.det(ay)
det_Az = np.linalg.det(az)

ax = det_Ax / det_A
ay = det_Ay / det_A
az = det_Az / det_A
print("The coefficient of X : ", ax)
print("The coefficient of X : ", ay)
print("The coefficient of X : ", az)