#utility functions
import re, math
import csv

#computes distances between all vertices and writes to file
def compute_all_distances(cities):
    file_name = "allDistances.csv"
    all_distances = []
    num_cities = len(cities)
    print "len = " + str(len(cities))
    x=0
    y=0
    dist = 0
    for i in range(num_cities-1):
        for j in range(num_cities-1):
            delta_x = cities[i+1][1] - cities[i][1]
            delta_y = cities[j+1][2] - cities[j][2]
            dist = math.sqrt(math.pow(delta_x,2) + math.pow(delta_y,2))
            row = "dist from "+str(i)+" to "+str(j)
            write_row_to_csv(file_name, [row, str(dist)])
            all_distances.append(["dist from "+str(i)+" to "+str(j), dist])
    return all_distances

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
        print city_row
        cities.append(city_row)
        line = f.readline()
        i=i+1
    f.close()
    return cities

#utility
def write_row_to_csv(file_name,row):
    write_mode = 'ab'
    with open(file_name, write_mode) as csvfile:
        statswriter = csv.writer(csvfile)
        statswriter.writerow(row)

#TESTS