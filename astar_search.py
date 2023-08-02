import random

class MazeSolver:
    def __init__(self, num_edges):
        self.num_edges = num_edges
        self.adj_matrix = [[float('inf')] * num_edges for _ in range(num_edges)]

    def add_edge(self, edge, weight):
        # Check for valid edge coordinates
        if edge[0] < 0 or edge[0] >= self.num_edges or edge[1] < 0 or edge[1] >= self.num_edges:
            raise IndexError("Invalid edge coordinates.")
        # Set the weight for the edge in the adjacency matrix
        self.adj_matrix[edge[0]][edge[1]] = weight
        self.adj_matrix[edge[1]][edge[0]] = weight

    def solve_maze_astar(self, start, goal):

        def heuristic(node):
            x1, y1 = node // 4, node % 4
            x2, y2 = goal // 4, goal % 4
            return abs(x1 - x2) + abs(y1 - y2)  

        distances = [float('inf')] * self.num_edges
        distances[start] = 0
        open_set = {start}
        parent = [-1] * self.num_edges

        step = 0  # Step counter

        while open_set:
            # Select the node with the minimum f-score from open_set
            current = min(open_set, key=lambda node: distances[node] + heuristic(node))
            open_set.remove(current)

            print(f"Step {step}: Visiting Node {current} with Weight {distances[current]}")

            if current == goal:
                return self._construct_path(parent, start, goal)

            for neighbor in range(self.num_edges):
                weight = self.adj_matrix[current][neighbor]
                if weight < float('inf'):
                    # Calculate the new distance from the start node to the neighbor
                    new_dist = distances[current] + weight
                    if new_dist < distances[neighbor]:
                        distances[neighbor] = new_dist
                        open_set.add(neighbor)
                        parent[neighbor] = current

            step += 1

        return None

    def _construct_path(self, parent, start, goal):
        path = []
        current = goal
        while current != start:
            path.append(current)
            current = parent[current]
        path.append(start)
        path.reverse()
        return path
    def print_maze(self):
      for row in self.adj_matrix:
        print(row)

# Example usage:
maze_solver = MazeSolver(16)

# Adding edges one by one with random weights

maze_solver.add_edge((0, 1), 1)
maze_solver.add_edge((1, 5), 1)
maze_solver.add_edge((2, 6), 1)
maze_solver.add_edge((5, 6), 1)
maze_solver.add_edge((6, 10), 1)
maze_solver.add_edge((10, 9), 1)
maze_solver.add_edge((9, 13), 1)
maze_solver.add_edge((13, 14), 1)
maze_solver.add_edge((14, 15), 1)
maze_solver.add_edge((5, 4), 1)
maze_solver.add_edge((4, 8), 1)
maze_solver.add_edge((8, 12), 1)
maze_solver.add_edge((12, 13), 1)
maze_solver.add_edge((3, 7), 1)
maze_solver.add_edge((7, 11), 1)

maze_solver.print_maze()
start_node = 2
goal_node = 12
solution_path = maze_solver.solve_maze_astar(start_node, goal_node)
print("Path:", solution_path)
