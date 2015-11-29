#utility functions
import re, math, csv, os, time

#saves each vertex/city as a row [vertex num, x coord, y coord] in the cities 2D matrix
def read_vertices(filename, num_citities=0):
    cities = {}
    with open(filename, 'r') as f:
        for line in f:
            city = []
            for num in line.split():
                city.append(int(num))
            cities[city[0]] = [city[1], city[2]]
    return cities #returns: [ [v0, x0, y0], ..., [vn, xn, yn] ]

#returns dictionary of {city: distance, ...} corresponding to distance from given city parameter
def compute_distance_from_city_to_all_cities(city, cities):
    city_distances = {}
    dist = 0
    for to_city, coords in cities.iteritems():
            delta_x = cities[city][0] - coords[0]
            delta_y = cities[city][1] - coords[1]
            dist = int(round(math.sqrt(math.pow(delta_x,2) + math.pow(delta_y,2))))
            city_distances[to_city] = dist
    return city_distances

def find_min_adjacent(adjacent_dict, visited):
    #swap distance and vertext in tuple for easy sorting
    items = [(distance, vertex) for vertex, distance in adjacent_dict.items()]
    items.sort()
    for distance, vertex in items:
        if vertex not in visited:
            return (int(vertex), int (distance))
    return (-1, -1)

def distance(cities, a, b):
    dx = cities[a][0] - cities[b][0]
    dy = cities[a][1] - cities[b][1]
    dist = int(round(math.sqrt(dx*dx + dy*dy)))
    return dist

def calculate_route_distance(cities, route):
    total_distance = 0
    for i in range(len(route) - 1):
        total_distance += distance(cities, route[i], route[i+1])
    total_distance += distance(cities, route[0], route[-1])
    return total_distance

def nn_tsp(cities, starting_vertex):
    visited = [starting_vertex]
    num_cities = len(cities)
    cost = 0
    num_visited = 1
    while num_cities > num_visited:
        #get the last city visited
        last_node = visited[-1]
        if num_visited > 2:
            second_last_node = visited[-2]
        #compute the distances to all other cities from the last node
        adjacency_last_node = compute_distance_from_city_to_all_cities(last_node, cities)
        #get the nearest neighbor to the last node
        neighbor, weight = find_min_adjacent(adjacency_last_node, visited)
        #Add the nearest neighbor and distance to the visited and cost parameters
        if neighbor == -1:
            raise ValueError, "No path found"
        else:
            cost += weight
            visited.append(neighbor)
            if num_visited > 2:
                del cities[second_last_node]
            num_visited += 1
            #print num_visited
    cost = cost + distance(cities, visited[0], visited[-1])
    return visited, cost

#referenced http://codereview.stackexchange.com/questions/72265/2-opt-algorithm-for-traveling-salesman for route
def two_opt_switch(route, i, j):
    start = route[0:i+1]
    middle = route[i+1:j+1]
    middle = middle[::-1]
    end = route[j+1:]
    new_route = start + middle + end
    return new_route

#give the function the dict of cities and their coordinates, and the current best route
def two_opt(cities, best_route, best_distance, unlimited=True):
    route_len = len(best_route)
    if unlimited:
        outer_range = route_len - 2
    else:
        outer_range = 100
    #to emulate a do while loop
    change_flag = True
    while change_flag:
        change_flag = False
        for i in range(outer_range):
            for j in range(i + 2, route_len - 1):
                #print i, j
                org_edge = distance(cities, best_route[i], best_route[i + 1]) + distance(cities, best_route[j], best_route[j+1])
                new_edge = distance(cities, best_route[i+1], best_route[j+1]) + distance(cities, best_route[i], best_route[j])
                if( new_edge < org_edge):
                    best_distance -= (org_edge - new_edge)
                    best_route = two_opt_switch(best_route, i, j)
                    if unlimited:
                        change_flag = True
    return best_route, best_distance

def write_to_txt(cost, path, filename):
    with open(filename,"w") as text_file:
        text_file.write(str(cost)+"\n")
        for v in path:
            text_file.write(str(v)+"\n")


###code calls
filename = 'tsp_example_1.txt'
cities1 = read_vertices(filename)
start = time.clock()
visited, cost = nn_tsp(cities1, 0)

#re-set the cities1 dict
cities1 = read_vertices(filename)
#2-opt takes a long time to run, n^3
#there are shortcuts to improve but I couldn't implement them properly
if len(cities1) < 3000:
    print "Running 2-opt"
    opt_route, opt_distance = two_opt(cities1, visited, cost)
else:
    print "Running 2-opt limited"
    opt_route, opt_distance = two_opt(cities1, visited, cost, False)


total_time = time.clock() - start
#write results to file
filename = filename + '.tour'
write_to_txt(opt_distance, opt_route, filename)
print visited
print cost
print opt_route
print opt_distance
print total_time




