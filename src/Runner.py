import pygame


class Runner:
    def __init__(self, x, y, vel):
        self.x = x
        self.y = y
        self.vel = vel

    def run(self, dis, block_size, move):
        pygame.draw.rect(dis, (255, 255, 255), [self.x, self.y, block_size/4, block_size/4])
        if move == 'r':
            self.x += 1
        elif move == 'l':
            self.x -= 1
        elif move == 'u':
            self.y -= 1
        elif move == 'd':
            self.y += 1
        rect = [self.x, self.y, block_size/4, block_size/4]
        pygame.draw.rect(dis, (255, 0, 0), rect)
