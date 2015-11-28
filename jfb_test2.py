#utility functions
import re, math, csv, os

#saves each vertex/city as a row [vertex num, x coord, y coord] in the cities 2D matrix
def read_vertices(filename, num_citities=0):
    cities = {}
    with open(filename, 'r') as f:
        for line in f:
            city = []
            for num in line.split():
                city.append(int(num))
            cities[city[0]] = [city[1], city[2]]

    #print cities
    return cities #returns: [ [v0, x0, y0], ..., [vn, xn, yn] ]

cities1 = read_vertices('tsp_example_1.txt')

#returns dictionary of {city: distance, ...} corresponding to distance from given city parameter
def compute_distance_from_city_to_all_cities(city, cities):
    city_distances = {}
    dist = 0
    for to_city, coords in cities.iteritems():
            delta_x = cities[city][0] - coords[0]
            delta_y = cities[city][1] - coords[1]
            dist = int(round(math.sqrt(math.pow(delta_x,2) + math.pow(delta_y,2))))
            city_distances[to_city] = dist
    #print city_distances
    return city_distances

#adjacent_matrix = compute_distance_from_city_to_all_cities(0, cities1)
#visited = [0]
#print adjacent_matrix

def find_min_adjacent(adjacent_dict, visited):
    #swap distance and vertext in tuple for easy sorting
    items = [(distance, vertex) for vertex, distance in adjacent_dict.items()]
    items.sort()

    for distance, vertex in items:
        if vertex not in visited:
            return (int(vertex), int (distance))

    return (-1, -1)

#neighbor, weight = find_min_adjacent(adjacent_matrix, visited)

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
            print num_visited

    print visited
    print cost

nn_tsp(cities1, 0)