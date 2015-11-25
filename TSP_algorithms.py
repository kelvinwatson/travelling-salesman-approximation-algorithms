import utility


#nearest neighbor (greedy)
def tsp_nearest_neighbor(adjacency_list, source_vertex):
    #track visited and unvisited vertices
    track_visited_vertices = []
    i = 0
    while i < len(adjacency_list):
        track_visited_vertices.append[False]
    all_visited_flag = False;

    #assign the source vertex as visited as we are starting there
    adjacency_list[source_vertex].visited = True

    current_vertex = source_vertex
    while all_visited_flag is False:
        find_min_destination(current_vertex, adjacency_list[current_vertex])


def find_min_destination(u, adj_u):
    #use binary search to find shortest distance
    


#count number of cities and compute distances between all cities
filename = "tsp_example_1.txt"
num_cities = utility.count_cities(filename)
#print "number of cities in " + filename + "=" + str(num_cities)
cities = utility.read_vertices(filename,num_cities)
#print cities
all_distances = utility.compute_all_distances(cities)

#TESTING A SMALL EXAMPLE
filename = "tsp_example_4.txt"
num_cities = utility.count_cities(filename)
print "number of cities(vertices) in " + filename + "=" + str(num_cities)

cities = utility.read_vertices(filename,num_cities)
print "read vertices into 2D Matrix: "+str(cities)

all_distances = utility.compute_all_distances(cities)
print "all_distances: "+str(all_distances) #this example was small enough to print

adjacency_list = utility.create_adjacency_list(all_distances)
print "adjacency_list: "
for vert in adjacency_list:
    print vert.adjacent_vertices

#tsp_nearest_neighbor(adjacency_list,0)
