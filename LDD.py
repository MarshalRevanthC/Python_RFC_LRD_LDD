
def _sum(arr):
    sum = 0;
    for i in arr :
        sum = sum + i
    return (sum)

import numpy as np

count_1= []
level_1= []
count_2= []
level_2= []
cum_dam = []
m = 4
ldd = 630720000

level_r_1= np.loadtxt(r"C:\Users\MARVN\OneDrive - Vestas Wind Systems A S\Desktop\Marshal-Work\AEMO_frequency\py_ldd\ldd.txt",  usecols=1, skiprows=2, dtype=float)
count_r_1= np.loadtxt(r"C:\Users\MARVN\OneDrive - Vestas Wind Systems A S\Desktop\Marshal-Work\AEMO_frequency\py_ldd\ldd.txt",  usecols=2, skiprows=2, dtype=float)
level_r_2= np.loadtxt(r"C:\Users\MARVN\OneDrive - Vestas Wind Systems A S\Desktop\Marshal-Work\AEMO_frequency\py_ldd\ldd_1.txt",  usecols=1, skiprows=2, dtype=float)
count_r_2= np.loadtxt(r"C:\Users\MARVN\OneDrive - Vestas Wind Systems A S\Desktop\Marshal-Work\AEMO_frequency\py_ldd\ldd_1.txt",  usecols=2, skiprows=2, dtype=float)

for i in level_r_1:
    level_1.append(i)
for j in count_r_1:
    count_1.append(j)
for k in level_r_2:
    level_2.append(k)
for l in count_r_2:
    count_2.append(l)

for n in range(len(level_1)):
    cum_dam.append(((pow(level_1[n],m))*count_1[n])+((pow(level_2[n],m))*count_2[n]))

total_fati = (sum(cum_dam));
cum_damage = total_fati/ldd;
print (cum_damage)