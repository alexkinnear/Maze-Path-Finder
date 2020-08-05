import pygame


class Maze:
    def __init__(self, dis, block_size):
        self.dis = dis
        self.block_size = block_size
        self.path = []
        self.maze = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                     [1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
                     [1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1],
                     [1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1],
                     [1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1],
                     [2, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 3],
                     [1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1],
                     [1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1],
                     [1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1],
                     [1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1],
                     [1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1],
                     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
        self.visited = []
        for row in self.maze:
            new_row = row.copy()
            self.visited.append(new_row)

        for i in range(len(self.visited)):
            for j in range(len(self.visited[0])):
                self.visited[i][j] = False

    def get_start(self):
        for i in range(len(self.maze)):
            for j in range(len(self.maze[0])):
                if self.maze[i][j] == 2:
                    return i, j
        return 1

    def is_valid(self, row, col, visited):
        if 0 <= row <= len(self.maze[0]) and 0 <= col <= len(self.maze):  # Check Boundaries
            if self.maze[row][col] != 1 and visited[row][col] != True:  # Check for wall and if already visited
                return True
        return False

    def get_neighbors(self, row, col):
        neighbors = []
        if self.is_valid(row + 1, col, self.visited):
            neighbors.append('r')
        if self.is_valid(row - 1, col, self.visited):
            neighbors.append('l')
        if self.is_valid(row, col + 1, self.visited):
            neighbors.append('d')
        if self.is_valid(row, col - 1, self.visited):
            neighbors.append('u')
        return neighbors

    def solve(self, row, col):
        if self.maze[row][col] == 3:
            print(self.path)
            return
        self.visited[row][col] = True
        poss_moves = self.get_neighbors(row, col)
        if len(poss_moves) == 0:
            last_move = self.path.pop()
            if last_move == 'r':    # Go Left
                self.solve(row-1, col)
            elif last_move == 'l':  # Go Right
                self.solve(row+1, col)
            elif last_move == 'd':  # Go Up
                self.solve(row, col-1)
            elif last_move == 'u':  # Go Down
                self.solve(row, col+1)
        else:
            next_move = poss_moves[0]
            self.path.append(next_move)
            if next_move == 'r':  # Go Right
                self.solve(row + 1, col)
            elif next_move == 'l':  # Go Left
                self.solve(row - 1, col)
            elif next_move == 'd':  # Go Down
                self.solve(row, col + 1)
            elif next_move == 'u':  # Go Up
                self.solve(row, col - 1)