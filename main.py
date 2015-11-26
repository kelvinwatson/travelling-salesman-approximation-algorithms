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
    #print "number of cities(vertices) in " + filename + "=" + str(num_cities)

    cities = utility.read_vertices(filename)
    print "read vertices into 2D Matrix: "+str(cities)

    all_distances = utility.compute_all_distances(cities)
    print "all_distances: "+str(all_distances) #this example was small enough to print

    adjacency_list = utility.create_adjacency_list(all_distances)

    #print "adjacency_list: "
    # for i,vert in enumerate(adjacency_list):
    #     print "vertex " + str(i)+"->",
    #     for v in vert.adjacent_vertices:
    #         print v,
    #     print "\n"

    total_cost_and_path = algorithm.tsp_nearest_neighbor(adjacency_list,0)
    algorithm.tsp_approximation(all_distances,cities,adjacency_list,0)

    filename += ".tour"
    utility.write_to_txt(total_cost_and_path,filename)
    print "TSP approximation complete. Please see "+filename+" for result."
