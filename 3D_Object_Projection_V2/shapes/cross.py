import pygame
import numpy as np
from math import cos, sin, sqrt

class Cross:
    def __init__(self, screen, width, height, scale=100):
        self.screen = screen
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.scale = scale
        self.position = [width // 2, height // 2]
        self.angle_x = self.angle_y = self.angle_z = 0
        self.speed = 0.04

        self.phi = (1 + sqrt(5)) / 2

        self.auto = False

        self.points = [
            np.array([2, 0.5, 1]), np.array([0.5, 0.5, 1]), np.array([0.5, 2, 1]),
            np.array([-1, 2, 1]), np.array([-1, 0.5, 1]), np.array([-2.5, 0.5, 1]),
            np.array([-2.5, -1, 1]), np.array([-1, -1, 1]), np.array([-1, -2.5, 1]),
            np.array([0.5, -2.5, 1]), np.array([0.5, -1, 1]), np.array([2, -1, 1]),
            np.array([2, 0.5, -1]), np.array([0.5, 0.5, -1]), np.array([0.5, 2, -1]),
            np.array([-1, 2, -1]), np.array([-1, 0.5, -1]), np.array([-2.5, 0.5, -1]),
            np.array([-2.5, -1, -1]), np.array([-1, -1, -1]), np.array([-1, -2.5, -1]),
            np.array([0.5, -2.5, -1]), np.array([0.5, -1, -1]), np.array([2, -1, -1])
        ]

        self.projected_points = [[0, 0] for _ in self.points]
        self.projection_matrix = np.array([
            [1, 0, 0],
            [0, 1, 0]
        ])

    def rotate_and_project(self):
        rotation_x = np.array([
            [1, 0, 0],
            [0, cos(self.angle_x), -sin(self.angle_x)],
            [0, sin(self.angle_x), cos(self.angle_x)]
        ])
        rotation_y = np.array([
            [cos(self.angle_y), 0, sin(self.angle_y)],
            [0, 1, 0],
            [-sin(self.angle_y), 0, cos(self.angle_y)]
        ])
        rotation_z = np.array([
            [cos(self.angle_z), -sin(self.angle_z), 0],
            [sin(self.angle_z), cos(self.angle_z), 0],
            [0, 0, 1]
        ])

        for i, point in enumerate(self.points):
            rotated = rotation_z @ point
            rotated = rotation_y @ rotated
            rotated = rotation_x @ rotated
            projected = self.projection_matrix @ rotated

            x = int(projected[0] * self.scale + self.position[0])
            y = int(projected[1] * self.scale + self.position[1])
            self.projected_points[i] = [x, y]

    def draw(self):
        self.rotate_and_project()

        def c(i, j):
            pygame.draw.line(self.screen, self.BLACK,
                             self.projected_points[i], self.projected_points[j])

        # All your connections (exactly as in your original code)
        c(11, 0); c(0, 1); c(1, 10); c(10, 11)
        c(11, 23); c(23, 22); c(22, 13); c(13, 12)
        c(12, 23); c(0, 12); c(1, 13); c(10, 22)
        c(1, 2); c(2, 14); c(14, 13); c(13, 16)
        c(16, 4); c(4, 3); c(3, 15); c(1, 4)
        c(2, 3); c(16, 15); c(15, 14)
        c(7, 4); c(4, 5); c(5, 6); c(6, 7)
        c(7, 19); c(19, 18); c(18, 17); c(17, 5)
        c(18, 6); c(16, 17); c(16, 19)
        c(19, 22); c(10, 7); c(10, 9); c(20, 21)
        c(21, 20); c(20, 8); c(7, 8); c(19, 20)
        c(21, 22); c(21, 9); c(9, 8)

        for x, y in self.projected_points:
            pygame.draw.circle(self.screen, (0, 0, 255), (x, y), 5)


    

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
            self.scale = max(1, self.scale + 2)
        if keys[pygame.K_q]:
            self.scale = max(1, self.scale - 2)
        if keys[pygame.K_f]:
            self.auto = not self.auto


