import pygame
import numpy as np
from math import cos, sin

class Rhombicuboctahedron:
    def __init__(self, screen, width, height):
        self.screen = screen
        self.center = [width // 2, height // 2]
        self.scale = 100
        self.angle_x = self.angle_y = self.angle_z = 0
        self.speed = 0.04
        self.color = (255, 0, 0)

        v = [
            [1, -1, 3], [1, 1, 3], [-1, -1, 3], [-1, 1, 3],
            [1, -3, 1], [1, -1, 1], [1, 1, 1], [1, 3, 1],
            [-1, -3, 1], [-1, -1, 1], [-1, 1, 1], [-1, 3, 1],
            [1, -3, -1], [1, -1, -1], [1, 1, -1], [1, 3, -1],
            [-1, -3, -1], [-1, -1, -1], [-1, 1, -1], [-1, 3, -1],
            [1, -1, -3], [1, 1, -3], [-1, -1, -3], [-1, 1, -3],
            [3, -1, 1], [3, 1, 1], [3, -1, -1], [3, 1, -1],
            [-3, -1, 1], [-3, 1, 1], [-3, -1, -1], [-3, 1, -1]
        ]

        self.points = [np.array(vertex) for vertex in v]
        self.projected_points = np.zeros((len(self.points), 2))

        self.projection_matrix = np.array([
            [1, 0, 0],
            [0, 1, 0],
            [0, 0, 0]
        ])

        self.edges = [
            (0, 1), (1, 3), (3, 2), (2, 0),
            (20, 21), (21, 23), (23, 22), (22, 20),
            (24, 25), (25, 27), (27, 26), (26, 24),
            (28, 29), (29, 31), (31, 30), (30, 28),
            (4, 8), (8, 16), (16, 12), (12, 4),
            (7, 11), (11, 19), (19, 15), (15, 7),
            (0, 4), (4, 24), (24, 0), (25, 1), (1, 7), (7, 25),
            (11, 3), (3, 29), (29, 11), (28, 2), (2, 8), (8, 28),
            (12, 20), (20, 26), (26, 12), (21, 27), (27, 15), (15, 21),
            (19, 23), (23, 31), (31, 19), (16, 30), (30, 22), (22, 16)
        ]

    def handle_keys(self, keys):
        if keys[pygame.K_r]:
            self.angle_x = self.angle_y = self.angle_z = 0
        if keys[pygame.K_a]:
            self.angle_y += self.speed
        if keys[pygame.K_d]:
            self.angle_y -= self.speed
        if keys[pygame.K_w]:
            self.angle_x += self.speed
        if keys[pygame.K_s]:
            self.angle_x -= self.speed
        if keys[pygame.K_e]:
            self.scale = max(-1, self.scale - 2)
        if keys[pygame.K_q]:
            self.scale = max(1, self.scale + 2)

    def connect_points(self, i, j):
        pygame.draw.line(
            self.screen, self.color,
            (self.projected_points[i][0], self.projected_points[i][1]),
            (self.projected_points[j][0], self.projected_points[j][1]), 2
        )

    def draw(self):
        rotation_z = np.array([
            [cos(self.angle_z), -sin(self.angle_z), 0],
            [sin(self.angle_z), cos(self.angle_z), 0],
            [0, 0, 1],
        ])

        rotation_y = np.array([
            [cos(self.angle_y), 0, sin(self.angle_y)],
            [0, 1, 0],
            [-sin(self.angle_y), 0, cos(self.angle_y)],
        ])

        rotation_x = np.array([
            [1, 0, 0],
            [0, cos(self.angle_x), -sin(self.angle_x)],
            [0, sin(self.angle_x), cos(self.angle_x)],
        ])

        for i, point in enumerate(self.points):
            rotated = np.dot(rotation_z, point.reshape((3, 1)))
            rotated = np.dot(rotation_x, rotated)
            rotated = np.dot(rotation_y, rotated)
            projected = np.dot(self.projection_matrix, rotated)

            x = int(projected[0][0] * self.scale) + self.center[0]
            y = int(projected[1][0] * self.scale) + self.center[1]

            self.projected_points[i] = [x, y]
            pygame.draw.circle(self.screen, self.color, (x, y), 5)

        for edge in self.edges:
            self.connect_points(edge[0], edge[1])
