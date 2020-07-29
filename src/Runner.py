import pygame
import random
import threading

class Runner:
    def __init__(self, x, y, width, vel, num_moves):
        self.x = x
        self.y = y
        self.width = width
        self.vel = vel
        self.num_moves = num_moves
        self.moves = []

    def initialize_population(self, pop_size):
        runners = []
        for i in range(pop_size):
            runner = Runner(10, 270, 10, 5, 500)
            runners.append(runner)
        for runner in runners:
            for i in range(self.num_moves):
                runner.moves.append(random.randint(0, 4))
            print(runner.moves)
        return runners

    def run(self, dis, runners):
        def movement(runner):
            for move in runner.moves:
                if move == 0:
                    continue
                elif move == 1:
                    runner.y -= runner.vel
                elif move == 2:
                    runner.x += runner.vel
                elif move == 3:
                    runner.y += runner.vel
                else:
                    runner.x -= runner.vel
                pygame.draw.rect(dis, (255, 0, 0), [runner.x, runner.y, runner.width, runner.width])
                pygame.display.update()
                pygame.event.pump()

        for runner in runners:
            x = threading.Thread(target=movement, args=(runner,))
            x.start()








