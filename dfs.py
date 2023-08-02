#Busca em profundidade ou deep serach
class MazeSolver:
    def __init__(self, num_edges):
        self.num_edges = num_edges
        self.adj_matrix = [[0] * num_edges for _ in range(num_edges)]

    def add_edge(self, edge):
        if edge[0] < 0 or edge[0] >= self.num_edges or edge[1] < 0 or edge[1] >= self.num_edges:
            raise IndexError("Invalid edge coordinates.")
        self.adj_matrix[edge[0]][edge[1]] = 1
        self.adj_matrix[edge[1]][edge[0]] = 1

    def solve_maze_dfs(self, current, goal, visited=None, path=None):
        if visited is None:
            visited = [False] * self.num_edges
        if path is None:
            path = []

        visited[current] = True
        path.append(current)

        if current == goal:
            return path

        for neighbor in range(self.num_edges):
            if self.adj_matrix[current][neighbor] == 1 and not visited[neighbor]:
                new_path = self.solve_maze_dfs(neighbor, goal, visited, path)
                if new_path:
                    return new_path

        path.pop()
        return None
    def print_maze(self):
      for row in self.adj_matrix:
        print(row)

# Example usage:
maze_solver = MazeSolver(16)

# Adding edges one by one
maze_solver.add_edge((0, 1))
maze_solver.add_edge((1, 5))
maze_solver.add_edge((2, 6))
maze_solver.add_edge((5, 6))
maze_solver.add_edge((6, 10))
maze_solver.add_edge((10, 9))
maze_solver.add_edge((13, 14))
maze_solver.add_edge((14, 15))
maze_solver.add_edge((5, 4))
maze_solver.add_edge((4, 8))
maze_solver.add_edge((8, 12))
maze_solver.add_edge((12, 13))
maze_solver.add_edge((3, 7))
maze_solver.add_edge((7, 11))

start_node = 0
goal_node = 15
maze_solver.print_maze()
solution_path = maze_solver.solve_maze_dfs(start_node, goal_node)
print("Path:", solution_path)
