import utility


#nearest neighbor (greedy)
#def tsp_nearest_neighbor():



#count number of cities
filename = "tsp_example_1.txt"
num_cities = utility.count_cities(filename)
print "number of cities in " + filename + "=" + str(num_cities)
cities = utility.read_vertices(filename,num_cities)
print cities
all_distances = utility.compute_all_distances(cities)
#read_coordinates(num_cities)

#a simple example


filename = "tsp_example_4.txt"
num_cities = utility.count_cities(filename)
print "number of cities in " + filename + "=" + str(num_cities)
cities = utility.read_vertices(filename,num_cities)
print cities
all_distances = utility.compute_all_distances(cities)
print all_distances
#read_coordinates(num_cities)
