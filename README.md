# k-means-clustering
This is an implementation in C++ of the K-Means algorithm. It's rather focused on simplicity than being optimal, hence some of the decisions made.

Once cloned, open the containing folder, compile it and run it with:
```
g++ main.cpp -o kmeans -std=gnu++11
./kmeans
```
The algorithm takes a dataset of 3000 random points in space and separates them in a given number of clusters with a minimal distance for a given number of iterations, normally this iteration would be controlled by a threshold deviation. The parameters are on the header for you to tweak.
Once finished, the data is stored in a vector and printed on the terminal.

To view the data, you can use the python3 script that relies on matplotlib, regex and numpy. If you haven't already, you should install those with pip. The script can parse the output of the terminal and make a scatter graph with it. On any \*nix system you should be able to dump the output on a file with:
```
./kmeans > data.txt
python3 viewdata.py data.txt 30
```
Where thirty is the number of clusters made on the first program and the first argument is the output file.
This is the outcome:

![K-Means-Cluster](images/graph1.png?raw=true "Kmeans")
