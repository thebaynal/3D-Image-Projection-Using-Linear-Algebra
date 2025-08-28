import pygame
import numpy as np
from math import cos, sin, sqrt

class GreatDodecahedron:
    def __init__(self, screen, width, height):
        self.screen = screen
        self.width = width
        self.height = height
        self.center = [width // 2, height // 2]
        self.scale = 100
        self.angle_x = self.angle_y = self.angle_z = 0
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

        self.edges = [
            [12, 0], [13, 0], [16, 0], [17, 0], [12, 1], [13, 1], [16, 1], [17, 1], [12, 2], [13, 2], [16, 2], [17, 2],
            [12, 11], [13, 11], [16, 11], [17, 11], [14, 8], [15, 8], [18, 8], [19, 8], [14, 9], [15, 9], [18, 9], [19, 9],
            [14, 3], [15, 3], [18, 3], [19, 3], [14, 10], [15, 10], [18, 10], [19, 10], [12, 0], [15, 0], [16, 0], [19, 0],
            [12, 8], [15, 8], [16, 8], [19, 8], [12, 4], [13, 4], [14, 4], [15, 4], [12, 6], [13, 6], [14, 6], [15, 6],
            [16, 5], [17, 5], [18, 5], [19, 5], [16, 7], [17, 7], [18, 7], [19, 7], [13, 1], [14, 1], [16, 1], [17, 1],
            [13, 9], [14, 9], [17, 9], [1, 18]
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

    def connect_points(self, i, j):
        pygame.draw.line(
            self.screen, (0, 0, 0),
            (int(self.projected_points[i][0]), int(self.projected_points[i][1])),
            (int(self.projected_points[j][0]), int(self.projected_points[j][1]))
        )

    def draw(self):
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
            rotated = rotation_y @ point.reshape(3, 1)
            rotated = rotation_x @ rotated

            projected = self.projection_matrix @ rotated
            x = int(projected[0][0] * self.scale + self.center[0])
            y = int(projected[1][0] * self.scale + self.center[1])
            self.projected_points[i] = [x, y]
            pygame.draw.circle(self.screen, (255, 255, 255), (x, y), 1)

        for edge in self.edges:
            self.connect_points(edge[0], edge[1])
