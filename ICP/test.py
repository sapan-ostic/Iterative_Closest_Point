import csv
import numpy as np
from pyntcloud import PyntCloud
import matplotlib
from mpl_toolkits.mplot3d import Axes3D 
import matplotlib.pyplot as plt

data = np.loadtxt('data_bunny.txt')
# print(data)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
x = data[:,0]
y = data[:,1]
z = data[:,2]

ax.scatter(x, y, z, marker='.')

data = np.loadtxt('model_bunny.txt')
# print(data)

x = data[:,0]
y = data[:,1]
z = data[:,2]

ax.scatter(x, y, z, marker='.',)
ax.set_xlim3d([-1, 1])
plt.show()

# point_cloud = np.empty([1,3])

# with open('test_.txt', newline='') as csvfile:
#     spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
#     randomIterator = iter(spamreader)
#     next(randomIterator)
#     for row in spamreader:
#         point_cloud = np.append(point_cloud, np.array(row).reshape(1,3), axis=0 )

# point_cloud = np.delete(point_cloud, 0, axis=0)

# # print(np.shape(point_cloud))     
# print(point_cloud)   

# cloud = PyntCloud.from_file("pyntcloud_plot.ply")
# cloud.plot()

# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')

# xs = 
# ax.scatter(xs, ys, zs, marker=m)
 