import pygame
import numpy as np
from math import cos, sin, sqrt

class RhombicTriacontahedron:
    def __init__(self, screen, width, height):
        self.screen = screen
        self.width = width
        self.height = height
        self.center = [width // 2, height // 2]
        self.scale = 100
        self.angle_x = 0
        self.angle_y = 0
        self.angle_z = 0
        self.speed = 0.04

        phi = (1 + sqrt(5)) / 2
        self.points = [
            np.matrix([phi, 1, 0]), np.matrix([-phi, 1, 0]), np.matrix([0, phi, 1]), np.matrix([0, -phi, 1]),
            np.matrix([1, 0, phi]), np.matrix([1, 0, -phi]), np.matrix([-1, 0, phi]), np.matrix([-1, 0, -phi]),
            np.matrix([phi, -1, 0]), np.matrix([-phi, -1, 0]), np.matrix([0, -phi, -1]), np.matrix([0, phi, -1]),
            np.matrix([1/phi, 1/phi, 1/phi]), np.matrix([-1/phi, 1/phi, 1/phi]), np.matrix([-1/phi, -1/phi, 1/phi]),
            np.matrix([1/phi, -1/phi, 1/phi]), np.matrix([1/phi, 1/phi, -1/phi]), np.matrix([-1/phi, 1/phi, -1/phi]),
            np.matrix([-1/phi, -1/phi, -1/phi]), np.matrix([1/phi, -1/phi, -1/phi])
        ]

        self.projected_points = [[0, 0] for _ in self.points]
        self.projection_matrix = np.array([
            [1, 0, 0],
            [0, 1, 0]
        ])

        self.edges = [
            (14, 3), (14, 6), (14, 9), (15, 3), (15, 8), (15, 4),
            (17, 1), (17, 11), (17, 18), (17, 7), (12, 15), (12, 16), (12, 13),
            (13, 17), (13, 14), (14, 15), (14, 18), (19, 18), (19, 15),
            (16, 19), (16, 17), (19, 8), (19, 5), (19, 10), (18, 10),
            (18, 9), (18, 7), (12, 0), (12, 2), (12, 4), (13, 1),
            (13, 2), (13, 6), (16, 0), (16, 5), (16, 11), (3, 8),
            (3, 10), (8, 10), (3, 9), (9, 10), (6, 9), (3, 6),
            (1, 9), (0, 8), (1, 9), (1, 6), (1, 7), (1, 11),
            (0, 11), (5, 10), (3, 4), (4, 8), (1, 2), (2, 6),
            (7, 11), (5, 11), (2, 4), (0, 4), (7, 9), (7, 10),
            (0, 2), (0, 5), (4, 6), (5, 7), (5, 8), (2, 11)
        ]

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
            x = int(projected[0][0] * self.scale + self.center[0])
            y = int(projected[1][0] * self.scale + self.center[1])
            self.projected_points[i] = [x, y]
            pygame.draw.circle(self.screen, (255, 255, 255), (x, y), 1)

        for i, j in self.edges:
            pygame.draw.line(self.screen, (0, 0, 0), (self.projected_points[i][0], self.projected_points[i][1]), (self.projected_points[j][0], self.projected_points[j][1]))
