import pygame
import math
import random
from threading import Thread


class Runner:
    def __init__(self, x, y, width, vel, num_moves, color):
        self.x = x
        self.y = y
        self.width = width
        self.vel = vel
        self.num_moves = num_moves
        self.color = color
        self.fitness = 0
        self.moves = []

    def initialize_population(self, maze, pop_size, parents, colors):
        runners = []
        for i in range(pop_size):
            runner = Runner(maze.start_point[0], maze.start_point[1], 10, 5, 200, colors[random.randint(0, len(colors)-1)])
            runners.append(runner)

        for runner in runners:
            for i in range(self.num_moves):
                num = random.randint(0, 3)
                if num == 0:
                    runner.moves.append(parents[0].moves[i])
                elif num == 1:
                    runner.moves.append(parents[1].moves[i])
                elif num == 2:
                    runner.moves.append(parents[2].moves[i])
                else:
                    runner.moves.append(parents[3].moves[i])
            print(runner.moves)
        return runners

    def run(self, dis, maze, runners):
        def movement(runner):  # Decide movement and check for walls
            def fitness(curr_runner):
                return math.sqrt((maze.end_point[0] - curr_runner.x)**2 + (maze.end_point[1] - curr_runner.y)**2)
            # pygame.draw.rect(dis, (255, 255, 255), [runner.x, runner.y, runner.width, runner.width])
            for move in runner.moves:
                if move == 0:
                    continue
                elif move == 1 and dis.get_at((runner.x - runner.vel, runner.y)) != (
                0, 0, 0, 255) and runner.x - runner.vel > 0:  # LEFT
                    runner.x -= runner.vel
                elif move == 2 and dis.get_at((runner.x + runner.vel + runner.width, runner.y)) != (
                0, 0, 0, 255):  # RIGHT
                    runner.x += runner.vel
                elif move == 3 and dis.get_at((runner.x, runner.y - runner.vel)) != (0, 0, 0, 255):  # UP
                    runner.y -= runner.vel
                elif dis.get_at((runner.x, runner.y + runner.vel + runner.width)) != (0, 0, 0, 255):  # DOWN
                    runner.y += runner.vel
                runner.fitness = fitness(runner)
                pygame.draw.rect(dis, runner.color, [runner.x, runner.y, runner.width, runner.width])
                pygame.display.update()
                pygame.event.pump()

        threads = []
        for runner in runners:
            process = Thread(target=movement, args=(runner,))
            process.start()
            threads.append(process)
        for process in threads:
            process.join()

    def selection(self, runners, parents):
        first, second, third, fourth = 1000, 1000, 1000, 1000
        runner1, runner2, runner3, runner4 = runners[0], runners[1], runners[2], runners[3]
        for runner in runners:
            if runner.fitness < first:
                runner4 = runner3
                runner3 = runner2
                runner2 = runner1
                runner1 = runner
                fourth = third
                third = second
                second = first
                first = runner.fitness
            elif runner.fitness < second:
                runner4 = runner3
                runner3 = runner2
                runner2 = runner
                fourth = third
                thrid = second
                second = runner.fitness
            elif runner.fitness < third:
                runner4 = runner3
                runner3 = runner
                fourth = third
                third = runner.fitness
            elif runner.fitness < fourth:
                runner4 = runner
                fourth = runner.fitness
        parents = [runner1, runner2, runner3, runner4]
        for i in range(len(parents[0].moves)):
            if parents[0].moves[i] == parents[1].moves[i] == parents[2].moves[i] == parents[3].moves[i]:
                for parent in parents:
                    parent.moves[i] = random.randint(0, 4)
        return parents
