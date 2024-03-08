# Python program for Dijkstra's 
# single source shortest 
# path algorithm. The program 
# is for adjacency matrix 
# representation of the graph
cities = ['Ankara','Balıkesir','Muğla','Antalya','İzmir','Çanakkale']

#Class to represent a graph 
class Graph: 
	# A utility function to find the 
	# vertex with minimum dist value, from 
	# the set of vertices still in queue
	def ShortCut(self,dist,queue): 
        # Initialize min value and min_index as -1 
		minimum = float("Inf") 
		
        # from the dist array,pick one which 
		# has min value and is till in queue 
		for i in range(len(dist)): 
			if dist[i] < minimum and i in queue: 
				minimum = dist[i] 
				min_index = i 
		return min_index 
    # Function to print shortest path 
	# from source to j 
	# using parent array 
	def ShortestPath(self, parent, j): 
		#Base Case : If j is source
		if parent[j] == -1 : 
			print(cities[j],end='-'),
			return
		self.ShortestPath(parent , parent[j]) 
		print (cities[j],end='-'), 
	# A utility function to print 
	# the constructed distance 
	# array 	
	def printSolution(self, dist, parent): 
		src = 0
		print("Destination\t\tDistance to Destination (KM)\t The Route Being Followed") 
		for i in range(1, len(dist)): 
			print("\n%s --> %s \t\t\t\t%s \t\t\t\t" % (cities[src], cities[i], dist[i]),end=''), 
			self.ShortestPath(parent,i) 

    #'''Function that implements Dijkstra's single source shortest path 
	#algorithm for a graph represented using adjacency matrix 
	#representation'''
	def dijkstra(self, graph, src): 

		row = len(graph) 
		col = len(graph[0])
		src = cities.index(src)

        # The output array. dist[i] will hold 
		# the shortest distance from src to i 
		# Initialize all distances as INFINITE 
		dist = [float("Inf")] * row 
        #Parent array to store 
		# shortest path tree 
		parent = [-1] * row 
        # Distance of source vertex 
		# from itself is always 0 
		dist[src] = 0
        # Add all vertices in queue
		queue = [] 
		for i in range(row): 
			queue.append(i) 
        #Find shortest path for all vertices 
		while queue:
            # Pick the minimum dist vertex 
			# from the set of vertices 
			# still in queue
			u = self.ShortCut(dist,queue)
            # remove min element
			queue.remove(u)
            # Update dist value and parent 
			# index of the adjacent vertices of 
			# the picked vertex. Consider only 
			# those vertices which are still in 
			# queue
			for i in range(col): 
				
				if graph[u][i] and i in queue: 
					if dist[u] + graph[u][i] < dist[i]: 
						dist[i] = dist[u] + graph[u][i] 
						parent[i] = u
        # print the constructed distance array
		self.printSolution(dist,parent)

# We have defined the s_p variable for functions defined in def dijkstra.    
s_p = Graph()
# We have defined the ways the algorithm will use as a matrix.
matris_g = [[0, 200, 500, 100, 0, 0],
        [200, 0, 300, 200, 0, 0], 
        [500, 300, 0, 300, 100, 500], 
        [100, 200, 300, 0, 100, 0], 
        [0, 0, 100, 100, 0, 200],
        [0, 0, 500, 0, 200, 0]]
# Print the solution
s_p.dijkstra(matris_g,str(input("Which City Are You In Right Now?: ")))

