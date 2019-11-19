import csv
import numpy as np

point_cloud = np.empty([1,3])

with open('model_bunny.txt', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    randomIterator = iter(spamreader)
    next(randomIterator)
    for row in spamreader:
        point_cloud = np.append(point_cloud, np.array(row).reshape(1,3), axis=0 )

point_cloud = np.delete(point_cloud, 0, axis=0)

print(np.shape(point_cloud))     
# print(point_cloud)   


