import utility


#nearest neighbor (greedy)
def tsp_nearest_neighbor(distance_matrix, source):
    #mark all vertices as unvisited
    #store vertices in adjacency list
    for i,d in all_distances:
        single_vertex_data = []
        if distance_matrix[i][0] == source:
            if distance_matrix[i][1] != source:
                single_vertex_data.append(all_distances[i])
        find_min_destination(source)

def find_min_destination(u):
    #use binary search to find shortest distance


#count number of cities and compute distances between all cities
filename = "tsp_example_1.txt"
num_cities = utility.count_cities(filename)
print "number of cities in " + filename + "=" + str(num_cities)
cities = utility.read_vertices(filename,num_cities)
print cities
all_distances = utility.compute_all_distances(cities)

#TESTING A SMALL EXAMPLE
filename = "tsp_example_4.txt"
num_cities = utility.count_cities(filename)
print "number of cities in " + filename + "=" + str(num_cities)
cities = utility.read_vertices(filename,num_cities)
print cities
all_distances = utility.compute_all_distances(cities)
print all_distances #this example was small enough to print
tsp_nearest_neighbor(all_distances,0)
