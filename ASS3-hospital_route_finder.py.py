#Assessment 3 TECH 6300
# Student Name: Jeisson Nino
# Student ID: 1854803

"""
Mock scenario: A patient needs to get to the hospital as quickly as possible.
 The city is represented as a graph where nodes are intersections and edges are 
 roads with weights representing travel time in minutes. There is a traffic jam 
 on one of the roads, which increases its travel time significantly.
"""



import heapq

class Graph:
    def __init__(self):
        # Dictionary to store the graph: {node: [(neighbor, weight), ...]}
        self.edges = {}

    def add_edge(self, from_node, to_node, weight):
        if from_node not in self.edges:
            self.edges[from_node] = []
        self.edges[from_node].append((to_node, weight))

def dijkstra(graph, start_node, end_node):
    # Priority Queue for event management (stores tuples of (current_time, node))
    # It ensures we always process the node with the shortest accumulated time next.
    priority_queue = []
    heapq.heappush(priority_queue, (0, start_node))
    
    # Dictionary to store the shortest time found to reach each node so far
    min_times = {start_node: 0}
    
    # Dictionary to reconstruct the path later (stores where we came from)
    predecessors = {start_node: None}

    while priority_queue:
        # Event: Pop the node with the smallest time
        current_time, current_node = heapq.heappop(priority_queue)

        # If we reached the hospital, we can stop
        if current_node == end_node:
            break

        # If we found a path to this node that is slower than one we already know, skip it
        if current_time > min_times.get(current_node, float('inf')):
            continue

        # Explore neighbors
        # .get() is used to handle nodes that might be endpoints with no outgoing edges
        for neighbor, weight in graph.edges.get(current_node, []):
            time_to_neighbor = current_time + weight

            # If we found a faster way to the neighbor, update our records
            if time_to_neighbor < min_times.get(neighbor, float('inf')):
                min_times[neighbor] = time_to_neighbor
                predecessors[neighbor] = current_node
                # Push new event to priority queue
                heapq.heappush(priority_queue, (time_to_neighbor, neighbor))

    # Reconstruct the path from End back to Start
    path = []
    current = end_node
    while current is not None:
        path.append(current)
        current = predecessors.get(current)
    
    # Reverse the path to show Start -> End
    return path[::-1], min_times[end_node]

# --- Main Execution based on your Image ---

# 1. Initialize Graph
g = Graph()

# 2. Add Edges (Nodes and weights from the image)
# Format: add_edge(Source, Destination, Minutes)
g.add_edge("Node A", "Node B", 5)
g.add_edge("Node A", "Node C", 10)

g.add_edge("Node B", "Node D", 5)
g.add_edge("Node B", "Node E", 20) # The dashed line (Traffic Jam)

g.add_edge("Node C", "Node D", 2)

g.add_edge("Node D", "Node E", 5)

# 3. Run Algorithm
start_node = "Node A"
target_node = "Node E"

shortest_path, total_time = dijkstra(g, start_node, target_node)

# 4. Output Results
print(f"--- Routing Results ---")
print(f"Start: {start_node}")
print(f"Destination: {target_node} (Hospital)")
print(f"-" * 20)
print(f"Optimal Path: {' -> '.join(shortest_path)}")
print(f"Total Time: {total_time} mins")