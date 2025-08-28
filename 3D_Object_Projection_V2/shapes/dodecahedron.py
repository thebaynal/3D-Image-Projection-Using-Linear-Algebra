import pygame
import numpy as np
import math
from math import cos, sin

class Dodecahedron:
    def __init__(self, screen, width, height):
        self.screen = screen
        self.width = width
        self.height = height
        self.scale = 100
        self.center = [width // 2, height // 2]
        self.angle_x = self.angle_y = self.angle_z = 0
        self.speed = 0.04

        self.hedron_pos = self.center

        phi = (1 + math.sqrt(5)) / 2
        self.points = [
            np.matrix([1, 1, 1]),
            np.matrix([-1, 1, 1]),
            np.matrix([1, -1, 1]),
            np.matrix([-1, -1, 1]),
            np.matrix([0, 1/phi, phi]),
            np.matrix([0, -1/phi, phi]),
            np.matrix([phi, 0, 1/phi]),
            np.matrix([-phi, 0, 1/phi]),
            np.matrix([1/phi, phi, 0]),
            np.matrix([-1/phi, phi, 0]),
            np.matrix([1/phi, -phi, 0]),
            np.matrix([-1/phi, -phi, 0]),
            np.matrix([0, 1/phi, -phi]),
            np.matrix([0, -1/phi, -phi]),
            np.matrix([phi, 0, -1/phi]),
            np.matrix([-phi, 0, -1/phi]),
            np.matrix([1, 1, -1]),
            np.matrix([-1, 1, -1]),
            np.matrix([-1, -1, -1]),
            np.matrix([1, -1, -1])
        ]

        self.projected_points = [[0, 0] for _ in self.points]
        self.projection_matrix = np.array([
            [1, 0, 0],
            [0, 1, 0]
        ])

    def handle_keys(self, keys):
        if keys[pygame.K_r]:
            self.angle_x = self.angle_y = self.angle_z = 0
        if keys[pygame.K_a]:
            self.angle_y += self.speed
        if keys[pygame.K_d]:
            self.angle_y -= self.speed
        if keys[pygame.K_w]:
            self.angle_x -= self.speed
        if keys[pygame.K_s]:
            self.angle_x += self.speed
        if keys[pygame.K_e]:
            self.scale = max(1, self.scale + 2)
        if keys[pygame.K_q]:
            self.scale = max(1, self.scale - 2)

    def connect_cube_points(self, i, j):
        pygame.draw.line(self.screen, (0, 0, 0), (self.projected_points[i][0], self.projected_points[i][1]), (self.projected_points[j][0], self.projected_points[j][1]))

    def draw(self):
        rotation_z = np.array([
            [cos(self.angle_z), -sin(self.angle_z), 0],
            [sin(self.angle_z), cos(self.angle_z), 0],
            [0, 0, 1]
        ])

        rotation_y = np.array([
            [cos(self.angle_y), 0, sin(self.angle_y)],
            [0, 1, 0],
            [-sin(self.angle_y), 0, cos(self.angle_y)]
        ])

        rotation_x = np.array([
            [1, 0, 0],
            [0, cos(self.angle_x), -sin(self.angle_x)],
            [0, sin(self.angle_x), cos(self.angle_x)]
        ])

        for i, point in enumerate(self.points):
            rotated = rotation_z @ point.reshape((3, 1))
            rotated = rotation_y @ rotated
            rotated = rotation_x @ rotated

            projected = self.projection_matrix @ rotated
            x = int(projected[0][0] * self.scale + self.hedron_pos[0])
            y = int(projected[1][0] * self.scale + self.hedron_pos[1])

            self.projected_points[i] = [x, y]
            pygame.draw.circle(self.screen, (255, 255, 255), (x, y), 1)

        edges = [
            (14, 19), (13, 19), (12, 13), (12, 16), (14, 16),
            (13, 18), (15, 18), (15, 17), (12, 17), (11, 18),
            (7, 15), (10, 19), (10, 11), (6, 14), (9, 8),
            (9, 17), (8, 16), (1, 7), (1, 9), (0, 4),
            (0, 8), (0, 6), (1, 4), (4, 5), (3, 5),
            (3, 7), (3, 11), (2, 6), (2, 5), (2, 10)
        ]

        for i, j in edges:
            self.connect_cube_points(i, j)
