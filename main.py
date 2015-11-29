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
import utility
import nn_algorithm as algorithm
import csv, math, os, re, sys, time

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

    cities1 = algorithm.read_vertices(filename)
    start = time.clock()
    visited, cost = algorithm.nn_tsp(cities1, 0)

    #re-set the cities1 dict
    cities1 = algorithm.read_vertices(filename)
    #2-opt takes a long time to run, n^3
    #there are shortcuts to improve but I couldn't implement them properly
    if len(cities1) < 3000:
        print "Running 2-opt... ",
        opt_route, opt_distance = algorithm.two_opt(cities1, visited, cost)
    else:
        print "Running 2-opt limited... ",
        opt_route, opt_distance = algorithm.two_opt(cities1, visited, cost, False)
    print "2-opt complete\n"


    total_time = time.clock() - start
    #write results to file
    filename = filename + '.tour'
    algorithm.write_to_txt(opt_distance, opt_route, filename)
    print "==Nearest Neighbor TS Results=="
    print "Visited vertices: "+str(visited)
    print "Distance: "+str(cost)

    print "\n==Results After 2-Optimization=="
    print "Visited vertices: "+str(opt_route)
    print "Distance: "+str(opt_distance)
    print "Running Time: "+str(total_time)

    print "TSP approximation complete. Please see "+filename+" for result."
