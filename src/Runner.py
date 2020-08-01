import pygame
import math


class Runner:
    def __init__(self, x, y, width, vel, color, moves):
        self.x = x
        self.y = y
        self.width = width
        self.vel = vel
        self.color = color
        self.moves = []
        self.last_move = 'left'

    def move(self, dis, end_point):

        def safe(x, y, width, vel):
            if dis.get_at((x + width + vel, y)) != (0, 0, 0, 255):  # check right
                if dis.get_at((x - vel, y)) != (0, 0, 0, 255):  # check left
                    if dis.get_at((x, y + width + vel)) != (0, 0, 0, 255):  # check down
                        if dis.get_at((x, y - vel)) != (0, 0, 0, 255):  # check up
                            return True
            return False

        def calculate_distance(x1, y1, x2, y2):
            return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

        def get_poss_moves():
            poss_moves = {}
            if safe(self.x + self.width + self.vel, self.y, self.width, self.vel) and self.last_move != 'left':
                poss_moves['right'] = calculate_distance(self.x + self.vel, self.y, end_point[0], end_point[1])
            if safe(self.x - self.vel, self.y, self.width, self.vel) and self.last_move != 'right':
                poss_moves['left'] = calculate_distance(self.x - self.vel, self.y, end_point[0], end_point[1])
            if safe(self.x, self.y - self.vel, self.width, self.vel) and self.last_move != 'down':
                poss_moves['up'] = calculate_distance(self.x, self.y - self.vel, end_point[0], end_point[1])
            if safe(self.x, self.y + self.width + self.vel, self.width, self.vel) and self.last_move != 'up':
                poss_moves['down'] = calculate_distance(self.x, self.y + self.vel, end_point[0], end_point[1])
            return poss_moves

        def get_best_move(poss_moves):
            best_move = list(poss_moves.keys())[0]
            for move in poss_moves:
                if poss_moves[move] < poss_moves[best_move]:
                    best_move = move
            return best_move

        def detect_pattern():
            patt_size = 2
            for k in range(len(self.moves)):
                for i in range(len(self.moves)):
                    pattern = self.moves[i:i+patt_size]
                    if all(elem == pattern[0] for elem in pattern):
                        continue
                    for j in range(i + patt_size, len(self.moves) - patt_size):
                        if self.moves[j:j+patt_size] == pattern:
                            print("True")
                            break
                        print("False")
                        continue
                patt_size += 1

        next_move = get_best_move(get_poss_moves())
        self.moves.append(next_move)

        if next_move == 'right':
            self.x += self.vel
            self.last_move = 'right'
        elif next_move == 'left':
            self.x -= self.vel
            self.last_move = 'left'
        elif next_move == 'up':
            self.y -= self.vel
            self.last_move = 'up'
        else:
            self.y += self.vel
            self.last_move = 'down'
        detect_pattern()
        pygame.draw.rect(dis, self.color, [self.x, self.y, self.width, self.width])
        pygame.event.pump()

