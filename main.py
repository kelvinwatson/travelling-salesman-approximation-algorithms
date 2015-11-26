# !/usr/bin/env python
# title          :main.py
# description    :project 4
# author         :group 2: Joseph Barlan, Jeff Mueller, Kelvin Watson
# creation date  :25 Nov 15
# last modified  :
# usage          :main.py input_file.txt
# notes          :
# python_version :2.6.6
# ==============================================================================

import sys
import os.path
import utility
import tsp_algorithm as algorithm

if len(sys.argv) != 2:
    print "--ERROR: Incorrect number of arguments--"
    print "  Program expects: main.py input_filename.txt"
    print "  Please try again."
elif os.path.isfile(sys.argv[1]) is False:
    print "--ERROR: " + str(sys.argv[1]) + " is not a valid file--"
    print "  Program expects: main.py input_filename.txt"
    print "  Please try again."
else:
    filename = sys.argv[1]
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

total_cost_and_path = tsp_nearest_neighbor(adjacency_list,0)

filename += ".tour"
utility.write_to_txt(total_cost_and_path,filename)