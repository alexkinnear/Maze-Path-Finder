import pygame
import random
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

colors = [(255, 0, 0), (2, 255, 0), (0, 0, 255), (255, 255, 0), (0, 255, 255), (255, 0, 255)]

# ------ Maze ------
maze = Maze(dis)

# ------ Runners ------
parents = []
for i in range(4):
    runner = Runner(maze.start_point[0], maze.start_point[1], 10, 5, 200, colors[random.randint(0, len(colors) - 1)])
    [runner.moves.append(random.randrange(0, 4)) for _ in range(runner.num_moves)]
    parents.append(runner)

def gameLoop():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        dis.fill((255, 255, 255))
        maze.draw()
        runners = runner.initialize_population(maze, 10, parents, colors)
        runner.run(dis, maze, runners)
        runner.selection(runners, parents)
        pygame.display.update()
        clock.tick(fps)

gameLoop()
pygame.quit()
