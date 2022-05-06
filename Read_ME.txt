Our project, 'Hum Kis Gali Ja Rahen Hain' provides a way for the user to figure out what's the best way to get from point A to point B in Habib.
The website is hosted locally and uses Flask to run. You will have to install it( pip install Flask).
Our folder also consists of a comparealgorithm file, which prints out the shortest path from point A to B but also gives a comparison of the time taken in the execution of the respective algorithms.

Compare algorithms file:
This file is for the comparison of dijkstra and A_star algorithm.
For easier heuristics calculation, only one floor was chosen (the dataset is called edges1 and the positions of different nodes/places on the floor is given in the positions1 list)
The comparison algorithms should be run on nodes from the edges1 list only. As you will see 
on running the the A* execution time will probably display 0.0 units. This is because the time taken is exteremely small that the datatype's least limit is achieved. 
To compare in a better way, try with nodes that are relatively farther from each other. 
It was also observed that even though no smart heuristic approximation was calculated for (h=1) astar_algorithm, the execution time is still
significantly lower than dijkstra.This is because our enqueue function for priority queue utilizes linear search.

The heuristic approximation was done by designing a 2-d coordinate system on pygame and approximately marking all the nodes on floor 1. 
The positions were extracted in the positions1 list and is used for the heuristic approximation. 

The variable of elevation (3rd axis) can be introduced as an upgrade for this project in addition to the designing of a virtual map. 

