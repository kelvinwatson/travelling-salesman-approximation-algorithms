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
    starting_vertex = 0 #set this to the starting vertex
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
    cost = cost + distance(cities, visited[0], visited[-1])
    return visited, cost

#referenced http://codereview.stackexchange.com/questions/72265/2-opt-algorithm-for-traveling-salesman for route
def two_opt_switch(route, i, j):
    start = route[0:i]
    middle = route[i:j]
    middle = middle[::-1]
    end = route[j:]
    new_route = start + middle + end
    return new_route

#give the function the dict of cities and their coordinates, and the current best route
def two_opt(cities, best_route, best_distance):
    route_len = len(best_route)
    #to emulate a do while loop
    change_flag = True
    while change_flag:
        change_flag = False
        print best_distance
        for i in range(route_len - 1):
            for j in range(i + 1, route_len):
                new_route = two_opt_switch(best_route, i, j)
                new_distance = calculate_route_distance(cities, new_route)
                if(new_distance < best_distance):
                    best_distance = new_distance
                    best_route = new_route
                    change_flag = True
    return best_route, best_distance

def write_to_txt(cost, path, filename):
    with open(filename,"w") as text_file:
        text_file.write(str(cost)+"\n")
        for v in path:
            text_file.write(str(v)+"\n")



###code calls
filename = 'tsp_example_2.txt'
cities1 = read_vertices(filename)
start = time.clock()
visited, cost = nn_tsp(cities1, 0)

#re-set the cities1 dict
cities1 = read_vertices(filename)
#2-opt takes a long time to run, n^3
#there are shortcuts to improve but I couldn't implement them properly
print "Running 2-opt"
opt_route, opt_distance = two_opt(cities1, visited, cost)
total_time = time.clock() - start

#write results to file
filename = filename + '.tour'
write_to_txt(opt_distance, opt_route, filename)
print visited
print cost
print opt_route
print opt_distance
print total_time




