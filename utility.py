#utility functions
import re, math, csv, os

class Vertex:
    id = -1
    adjacent_vertices = [] #list of tuples [(u,distance to u),(v,distance to v)...]
    visited = False
    predecessor = None
    key = float("inf")
    def __init__(self, id):
        self.id=id
        self.adjacent_vertices = []
        self.visited = False
        self.predecessor = None
        self.key = float("inf")
    def __eq__(self, other):
        return self.id == other.id

def create_adjacency_list(distance_matrix):
    i = 0
    adjacency_list= []
    while (i < len(distance_matrix)):
        vertexID = distance_matrix[i][0]
        v = Vertex(vertexID)
        while distance_matrix[i][0] == vertexID:
            if distance_matrix[i][1] != vertexID:
                #store as tuple of vertexID,distance this vertex
                v.adjacent_vertices.append((distance_matrix[i][1],distance_matrix[i][2]))
            i+=1
            if i == len(distance_matrix):
                break
        adjacency_list.append(v)

    return adjacency_list


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

    print adjacency_dict
    return adjacency_dict


#computes distances between all vertices and writes to file
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
    write_distances_to_csv("allDistances.csv", all_distances)
    return all_distances

def write_distances_to_csv(file,all_distances):
    try:
        os.remove(file)
    except OSError:
        pass
    with open(file, 'ab') as csvfile:
        for row in all_distances:
            statswriter = csv.writer(csvfile)
            statswriter.writerow(row)

#utility
def write_row_to_csv(file_name,row):
    write_mode = 'ab'
    with open(file_name, write_mode) as csvfile:
        statswriter = csv.writer(csvfile)
        statswriter.writerow(row)


def count_cities(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i+1


def read_vertices(filename, num_cities=0):
    """ saves each vertex/city as a row [vertex num, x coord, y coord] in the cities 2D matrix
        returns: [ [v0, x0, y0], ..., [vn, xn, yn] ] """"
    cities = []
    with open(filename, 'r') as f:
        for line in f:
            city = []
            for num in line.split():
                city.append(int(num))
            cities.append(city)

    return cities

def write_to_txt(cost_and_path,filename):
    cost = str(cost_and_path[0])
    path = cost_and_path[1]
    with open(filename,"w") as text_file:
        text_file.write(cost+"\n")
        for v in path:
            text_file.write(str(v)+"\n")

def create_list_of_vertices(all_distances):
    vertex_list = []
    for x in all_distances:
        vertex_list.append(Vertex(x[0]))
    return vertex_list
