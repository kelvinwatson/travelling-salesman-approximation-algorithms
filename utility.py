#utility functions
import re, math, csv, os

class Vertex:
    id = -1
    adjacent_vertices = [] #list of tuples [(u,distance to u),(v,distance to v)...]
    visited = False
    predecessor = None
    def __init__(self, id):
        self.id=id
        self.adjacent_vertices = []
        self.visited = False
        predecessor = 0

def create_adjacency_list(distance_matrix):
    i = 0
    print "TRACE: distance_matrix="+str(distance_matrix)
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

#computes distances between all vertices and writes to file
def compute_all_distances(cities):
    all_distances = []
    print "TRACE: cities="+str(cities)
    num_cities = len(cities)
    x=0
    y=0
    dist = 0
    for i in range(num_cities):
        for j in range(num_cities):
            delta_x = cities[j][1] - cities[i][1]
            delta_y = cities[j][2] - cities[i][2]
            dist = math.sqrt(math.pow(delta_x,2) + math.pow(delta_y,2))
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

#saves each vertex/city as a row [vertex num, x coord, y coord] in the cities 2D matrix
def read_vertices(filename,num_cities):
    f = open(filename,'r')
    line = f.readline()
    #save cities into a 2D matrix
    cities = []
    i=0
    while len(line) > 1:
        coordinates = re.findall(r'[^,;\s]+', line)
        x = int(coordinates[1])
        y = int(coordinates[2])
        city_row = [i, x, y]
        #print city_row
        cities.append(city_row)
        line = f.readline()
        i=i+1
    f.close()
    return cities

def write_to_txt(cost_and_path):
    cost = cost_and_path[0]
    path = cost_and_path[1]