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
maze = Maze(dis)
maze.draw()

# ------ Runners ------
runner = Runner(25, 150, 10, 5, 200)
runners = runner.initialize_population(10)
runner.run(dis, runners)

def gameLoop():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.update()
        clock.tick(fps)


gameLoop()
pygame.quit()
