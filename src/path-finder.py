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
maze = Maze(dis, 50)
start = maze.get_start()
maze.solve(start[0], start[1])

# ------ Runners ------
runner = Runner()


# def gameLoop():
#     running = True
#     while running:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 running = False
        # dis.fill((255, 255, 255))
        # maze.draw()
        # if len(runner.moves) > 8:
        #     runner.moves = runner.moves[-8:]
        # runner.move(dis, maze.start_point, maze.end_point, maze.block_size, maze.dead_ends)
        # pygame.display.update()
        # clock.tick(fps)

#
# gameLoop()
pygame.quit()
