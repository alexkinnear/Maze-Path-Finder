import pygame
import math


class Runner:
    def __init__(self, x, y, width, vel, color):
        self.x = x
        self.y = y
        self.width = width
        self.vel = vel
        self.color = color
        self.moves = []
        self.last_move = 'left'
        self.patt_count = 0

    def move(self, dis, start_point, end_point, block_size, dead_ends):

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
            if self.patt_count > 50:
                return True
            patt_size = 2
            for k in range(len(self.moves)):
                for i in range(len(self.moves)):
                    pattern = self.moves[i:i + patt_size]
                    if all(elem == pattern[0] for elem in pattern):
                        continue
                    for j in range(i + patt_size, len(self.moves) - patt_size):
                        if self.moves[j:j + patt_size] == pattern:
                            self.patt_count += 1
                        continue
                patt_size += 1
            return False

        def get_dist_each_side():
            dist_each_side = {}
            right = left = up = down = 0
            while dis.get_at((self.x + right, self.y)) != (0, 0, 0, 255):
                right += 5
            dist_each_side['right'] = right
            while dis.get_at((self.x - left, self.y)) != (0, 0, 0, 255):
                left += 5
            dist_each_side['left'] = left
            while dis.get_at((self.x + self.width, self.y - up)) != (0, 0, 0, 255):
                up += 5
            dist_each_side['up'] = up
            while dis.get_at((self.x + self.width, self.y + down)) != (0, 0, 0, 255):
                down += 5
            dist_each_side['down'] = down
            return dist_each_side

        def find_escape(distances, arr):
            # Find the direction(s) where the block can escape
            if len(arr) == 0:
                for key, value in distances.items():
                    if value > block_size:
                        arr.append(key)
            if len(arr) == 1:
                if arr[0] == 'left':
                    pygame.draw.rect(dis, (255, 255, 255), [self.x, self.y, self.width, self.width])
                    dead_end = [self.x + self.width, self.y - distances['up'], distances['right'], distances['up'] + distances['down']]
                    dead_ends.append(dead_end)
                    self.x -= self.vel
                    pygame.draw.rect(dis, self.color, [self.x, self.y, self.width, self.width])
                    pygame.display.update()
                    pygame.event.pump()
                elif arr[0] == 'right':
                    pygame.draw.rect(dis, (255, 255, 255), [self.x, self.y, self.width, self.width])
                    dead_end = [self.x - distances['left'], self.y - distances['up'], distances['left'], distances['up'] + distances['down']]
                    dead_ends.append(dead_end)
                    self.x += self.vel
                    pygame.draw.rect(dis, self.color, [self.x, self.y, self.width, self.width])
                    pygame.display.update()
                    pygame.event.pump()
                    find_escape(get_dist_each_side(), [])
                elif arr[0] == 'up':
                    pygame.draw.rect(dis, (255, 255, 255), [self.x, self.y, self.width, self.width])
                    dead_end = [self.x - distances['left'], self.y + self.width, distances['left'] + distances['right'], distances['down']]
                    dead_ends.append(dead_end)
                    self.y -= self.vel
                    pygame.draw.rect(dis, self.color, [self.x, self.y, self.width, self.width])
                    pygame.display.update()
                    pygame.event.pump()
                    find_escape(get_dist_each_side(), [])
                elif arr[0] == 'down':
                    pygame.draw.rect(dis, (255, 255, 255), [self.x, self.y, self.width, self.width])
                    dead_end = [self.x - distances['left'], self.y - distances['up'], distances['left'] + distances['right'], distances['up']]
                    dead_ends.append(dead_end)
                    self.y += self.vel
                    pygame.draw.rect(dis, self.color, [self.x, self.y, self.width, self.width])
                    pygame.display.update()
                    pygame.event.pump()
                    find_escape(get_dist_each_side(), [])
            else:
                while len(arr) != 1:
                    arr.pop()
                for i in range(10):
                    if arr[0] == 'right':
                        pygame.draw.rect(dis, (255, 255, 255), [self.x, self.y, self.width, self.width])
                        self.x += self.vel
                        pygame.draw.rect(dis, self.color, [self.x, self.y, self.width, self.width])
                    elif arr[0] == 'left':
                        pygame.draw.rect(dis, (255, 255, 255), [self.x, self.y, self.width, self.width])
                        self.x -= self.vel
                        pygame.draw.rect(dis, self.color, [self.x, self.y, self.width, self.width])
                    elif arr[0] == 'up':
                        pygame.draw.rect(dis, (255, 255, 255), [self.x, self.y, self.width, self.width])
                        self.y -= self.vel
                        pygame.draw.rect(dis, self.color, [self.x, self.y, self.width, self.width])
                    elif arr[0] == 'down':
                        pygame.draw.rect(dis, (255, 255, 255), [self.x, self.y, self.width, self.width])
                        self.y += self.vel
                        pygame.draw.rect(dis, self.color, [self.x, self.y, self.width, self.width])
                    pygame.display.update()
                    pygame.event.pump()
                find_escape(get_dist_each_side(), [])

        for end in dead_ends:
            pygame.draw.rect(dis, (0, 0, 0, 255), end)

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
        if detect_pattern():
            self.patt_count = 0
            dist = get_dist_each_side()
            find_escape(dist, [])

        pygame.draw.rect(dis, self.color, [self.x, self.y, self.width, self.width])
        pygame.event.pump()
