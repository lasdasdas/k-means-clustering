# k-means-clustering
This is an implementation in C++ of the K-Means algorithm. It's rather focused on simplicity than being optimal, hence some of the decisions made.

Once cloned open the containing folder, compile it and run it with:
```
g++ main.cpp -o kmeans
./kmeans
```
The algorithm takes a dataset of 3000 random points in space and separates them in a given number of clusters with a minimal distance for a given number of iterations, normally this iteration would be to a threshold deviation.
