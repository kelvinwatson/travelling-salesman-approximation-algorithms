#utility functions
import re, math, csv, os
import tsp_algorithm as algorithm


#saves each vertex/city as a row [vertex num, x coord, y coord] in the cities 2D matrix
def read_vertices(filename, num_citities=0):
    cities = []
    with open(filename, 'r') as f:
        for line in f:
            city = []
            for num in line.split():
                city.append(int(num))
            cities.append(city)

    #print cities
    return cities #returns: [ [v0, x0, y0], ..., [vn, xn, yn] ]



cities1 = read_vertices('tsp_example_1.txt')


def compute_all_distances(cities):
    all_distances = []
    num_cities = len(cities)
    dist = 0
    for i in range(num_cities):
        for j in range(num_cities):
            delta_x = cities[j][1] - cities[i][1]
            delta_y = cities[j][2] - cities[i][2]
            dist = int(round(math.sqrt(math.pow(delta_x,2) + math.pow(delta_y,2))))
            all_distances.append([i,j,dist])
    #print all_distances
    return all_distances

matrix = compute_all_distances(cities1)


def create_adjacency_dict(distance_matrix):
    i = 0
    adjacency_dict =  {}
    
    while (i < len(distance_matrix)):
        vertexID = distance_matrix[i][0]
        v_adjacent = {}
        while distance_matrix[i][0] == vertexID:
            if distance_matrix[i][1] != vertexID:
                v_adjacent[distance_matrix[i][1]] = distance_matrix[i][2]
            i+=1
            
            if i == len(distance_matrix):
                break
            
        adjacency_dict[vertexID] = v_adjacent

    #print adjacency_dict
    return adjacency_dict

def find_min_adjacent(adjacent_dict, visited):
    #swap distance and vertext in tuple for easy sorting
    items = [(distance, vertex) for vertex, distance in adjacent_dict.items()] 
    items.sort()

    for distance, vertex in items:
        if vertex not in visited:
            return (int(vertex), int (distance))

    return (-1, -1)


g = create_adjacency_dict(matrix)


def nn_tsp(g):
    starting_vertex = 0 #set this to the starting vertex
    visited = [starting_vertex]
    U = [g.pop(starting_vertex)]
    V = g
    cost = 0

    while len(V) > 0:
        #set u/lastnode to most recently added vertext to U
        last_node = U[-1]
        #find vertex v in V closest to u
        neighbor, weight = find_min_adjacent(last_node, visited)
        #Add v to U and remove v from V
        if neighbor == -1:
            raise ValueError, "No path found"
        else:
            cost += weight
            visited.append(neighbor)
            v = V.pop(neighbor)
            U.append(v)
        
    print visited
    print cost
        

nn_tsp(g)
