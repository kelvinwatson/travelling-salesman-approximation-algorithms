import utility


#nearest neighbor (greedy)
def tsp_nearest_neighbor(adj_list, source_vertex):
    #track visited and unvisited vertices
    track_visited_vertices = []
    i = 0
    while i < len(adj_list):
        track_visited_vertices.append(False)
        i+=1
    all_visited_flag = False

    #assign the source vertex as visited as we are starting there
    adj_list[source_vertex].visited = True

    current_vertex = source_vertex
    while all_visited_flag is False:
        print "TRACE: "+str(adj_list[current_vertex].adjacent_vertices)
        nearest_neighbor = find_min_destination(adj_list[current_vertex].adjacent_vertices)
        current_vertex = nearest_neighbor #change current vertex to nearest neighbor
        adj_list[nearest_neighbor].visited = True #mark the neighbor as visited
        adj_list[nearest_neighbor].predecessor = current_vertex
        all_visited_flag = check_if_all_visited(track_visited_vertices)

def check_if_all_visited(track):
    for x in track:
        if x is True: return True

def find_min_destination(adj_u):
    curr_min = float("inf")
    for x in adj_u:
        if x[1]<curr_min: #x[1] accesses the distance in the tuple
            curr_min=x[0] #x[0] accesses the vertex ID in the tuple
    return curr_min


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

tsp_nearest_neighbor(adjacency_list,0)
