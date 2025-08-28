import pygame
import numpy as np
from math import cos, sin

class Cube:
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

        self.points = [
            np.matrix([-1, -1, 1]), np.matrix([1, -1, 1]), np.matrix([1, 1, 1]), np.matrix([-1, 1, 1]),
            np.matrix([-1, -1, -1]), np.matrix([1, -1, -1]), np.matrix([1, 1, -1]), np.matrix([-1, 1, -1])
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
            self.angle_x += self.speed
        if keys[pygame.K_s]:
            self.angle_x -= self.speed
        if keys[pygame.K_e]:
            self.scale += 2
        if keys[pygame.K_q]:
            self.scale = max(1, self.scale - 1)

    def connect_points(self, i, j):
        pygame.draw.line(self.screen, (0, 0, 0),
                         (self.projected_points[i][0], self.projected_points[i][1]),
                         (self.projected_points[j][0], self.projected_points[j][1]))

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

        for p in range(4):
            self.connect_points(p, (p + 1) % 4)
            self.connect_points(p + 4, ((p + 1) % 4) + 4)
            self.connect_points(p, p + 4)
