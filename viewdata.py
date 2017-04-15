from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import re
import numpy
import sys
filename="hi.txt"
kclusters=10
# Parsing the flags
if (sys.argv[1]=="-h" or sys.argv[1]=="--help"):
    print("First argument is the data file second one is the cluster number")
    sys.exit()
if len(sys.argv)==3:
    filename=sys.argv[1]
    kclusters=int(sys.argv[2])
#Importing the result file
filecontent = []
with open(filename) as f:
    filecontent = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
filecontent = [x.rstrip() for x in filecontent]
filecontent = [re.split(r'\t+', x) for x in filecontent]
#Transforming from string to the appropiate data types
for row in filecontent:
    row[0]=int(row[0])
    row[1]=float(row[1])
    row[2]=float(row[2])
    row[3]=float(row[3])
    row[4]=int(row[4])-1
#Sorting the clusters
clusterlist=[[[] for i in range(3)]for j in range(kclusters)]
for row in filecontent:
    clusterlist[row[4]][0].append(row[1])
    clusterlist[row[4]][1].append(row[2])
    clusterlist[row[4]][2].append(row[3])

for n in range(len(clusterlist)):
    print("Cluster "+str(n)+" has "+str(len(clusterlist[n][0]))+" points")

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
for n in range(kclusters):
    x =clusterlist[n][0]
    y =clusterlist[n][1]
    z =clusterlist[n][2]
    ax.scatter(x, y, z, c=numpy.random.rand(3,), marker='o')

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()
