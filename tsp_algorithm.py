import utility
import heapq as q

#nearest neighbor (greedy)
def tsp_nearest_neighbor(adj_list, source_vertex):
    #track visited and unvisited vertices
    track_visited_vertices = []
    path = []
    path_cost = 0
    i = 0
    while i < len(adj_list):
        track_visited_vertices.append(False)
        i+=1
    all_visited_flag = False

    #assign the source vertex as visited as we are starting there
    track_visited_vertices[source_vertex] = adj_list[source_vertex].visited = True
    path.append(source_vertex)

    current_vertex = source_vertex
    while all_visited_flag is False:
        #nearest neighbor is a tuple of (vertexID,distance)
        #which can be accessed like a list using square brackets nn[0]==vertexID, nn[1]==distance
        nearest_neighbor = find_min_destination(adj_list[current_vertex].adjacent_vertices, adj_list) #find nearest neighbor
        path.append(nearest_neighbor[0])
        path_cost += nearest_neighbor[1]
        #print "nn="+str(nearest_neighbor[0])+","+str(nearest_neighbor[1])
        #print "path_cost="+str(path_cost)
        current_vertex = nearest_neighbor[0] #current vertex is now the nearest identified neighbor
        track_visited_vertices[nearest_neighbor[0]] = adj_list[nearest_neighbor[0]].visited = True #mark the neighbor as visited
        adj_list[nearest_neighbor[0]].predecessor = current_vertex
        all_visited_flag = check_if_all_visited(track_visited_vertices)
    #add path from last vertex to source
    cost = adj_list[current_vertex].adjacent_vertices[source_vertex][1]
    path_cost += cost
    #path.append(adj_list[current_vertex].adjacent_vertices[source_vertex][0])
    #print path_cost
    #print path
    return int(path_cost),path

def check_if_all_visited(track):
    for x in track:
        if x is False: return False
    return True

#returns a tuple of the vertexID and distance
def find_min_destination(adj_u,adj_list):
    curr_min = (-1,float("inf"))
    for v in adj_u:
        if adj_list[v[0]].visited is False: #if vertex not yet visited
            if v[1]<curr_min[1]: #v[1] accesses the distance in the tuple
                curr_min=v #v[0] accesses the vertex ID in the tuple
    return curr_min

#all_distances = sorted(all_distances,key=lambda x: x[2]) #sort edges ASC

def prim(vertex_list, adj_list, r):
    #print "PRIM"
    #for i,vert in enumerate(adj_list):
        #print "vertex " + str(i)+"->",
        #for v in vert.adjacent_vertices:
        #    print v,
        #print "\n"
    queue = []
    mst = []
    for v in vertex_list:     #initialize vertices
        #print str(v.id)+","+str(v.key)+","+str(v.predecessor)
        if v.id == r: v.key=0 #find the root and set its key to 0
        q.heappush(queue,(v.key, v))
    #print "printing vertices in heap!"
    #for v in queue: #each v is a tuple, (key,v object)
    #    print str(v[0]) +" " +str(v[1].id)+" "+str(v[1].predecessor)
    while queue:
        u = q.heappop(queue) #extract min
        mst.append(u[1])
        #print "just popped vertex "+str(u[1].id)+" predecessor="+str(u[1].predecessor)+" dist="+str(u[0]);
        for v in adj_list[u[1].id].adjacent_vertices:
            #print "v = "+str(v)
            #check if a vertex with id of v[0] is in queue
            for a in queue:
                if v[0] == a[1].id: #vertex a with id v[0] is in queue
                    if v[1] < a[1].key:
                        a[1].predecessor=u[1].id
                        a[1].key=v[1]
                        break
    return mst

def tsp_approximation(all_distances,cities,adj_list,source):
    vertex_list = utility.create_list_of_vertices(cities)
    #print vertex_list
    mst = prim(vertex_list,adj_list,source)
    path = []
    print "MST"
    #for m in mst:
    #    print "id="+str(m.id)+" key="+str(m.key)+" predecessor="+str(m.predecessor)

    #preorder walk
    path_len=0
    for i,m in enumerate(mst):
        if i < len(mst)-1:
            v1=mst[i].id
            v2=mst[i+1].id
            #search thru list of edges for matching src and dest
            for n in all_distances:
                if v1==n[0] and v2==n[1]:
                    path_len+=n[2]
    #add path from last vertex to src
    v1=mst[len(mst)-1].id
    v2=source
    for n in all_distances:
        if v1==n[0] and v2==n[1]:
            path_len+=n[2]
    print path_len
    mst.append(mst[0])
    for m in mst:
        print "id="+str(m.id)+" key="+str(m.key)+" predecessor="+str(m.predecessor)
        path.append(m.id)
    return path_len,path
