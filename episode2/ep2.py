import numpy as np
import matplotlib.pyplot as plt

A = []
b = []
with open('large.txt') as f:
    lines = f.readlines()
n = int(lines[0])
for i in range(1, n+1):
    row = lines[i].split()
    row = [float(i) for i in row]
    A.append(row)
row = lines[n+1].split()
row = [float(i) for i in row]
b.append(row)


A = np.array(A)
b = np.array(b[0])
res = np.linalg.solve(A, b)
print(res)
print(np.allclose(np.dot(A, res), b)) #проверка на исправность

x = np.linspace(0, n-1, len(res))
plt.grid()
plt.bar(x, res)
plt.savefig("large.png")
plt.show()