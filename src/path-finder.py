import pygame
from Maze import Maze
from Runner import Runner

pygame.init()

# ------ Display ------
dis_width = 600
dis_height = 600
dis = pygame.display.set_mode((dis_width, dis_height))
dis.fill((255, 255, 255))
pygame.display.set_caption("Maze Path Finder")

clock = pygame.time.Clock()
fps = 360

# ------ Maze ------
maze = Maze(dis, dis_width)
start = maze.get_start()
maze.solve(start[0], start[1])
print(start)

# ------ Runners ------
runner = Runner((start[1] * maze.block_size) + (maze.block_size / 2), (start[0] * maze.block_size) + (maze.block_size / 2), 10)

count = 0
def gameLoop(count):
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        dis.fill((255, 255, 255))
        block_size = maze.draw()
        if count < len(maze.path):
            for i in range(maze.block_size):
                runner.run(dis, block_size, maze.path[count])
            count += 1
        pygame.display.update()
        # pygame.time.wait(500)
        clock.tick(fps)


gameLoop(count)
pygame.quit()
