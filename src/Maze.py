import pygame


class Maze:
    def __init__(self, dis, block_size):
        self.dis = dis
        self.block_size = block_size
        self.dead_ends = []
        self.start_point = (10, 270)
        self.end_point = (580, 270)
        self.maze = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
                    [1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1],
                    [1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1],
                    [1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1],
                    [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
                    [1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1],
                    [1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1],
                    [1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1],
                    [1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1],
                    [1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

    def draw(self):
        for i in range(len(self.maze)):
            for j in range(len(self.maze[0])):
                if self.maze[i][j] == 1:
                    pygame.draw.rect(self.dis, (0, 0, 0), [j*self.block_size, i*self.block_size, self.block_size, self.block_size])

