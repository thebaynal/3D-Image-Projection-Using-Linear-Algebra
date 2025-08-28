import pygame
import numpy as np
from math import cos, sin

class CubeWithinCube:
    def __init__(self, screen, width, height):
        self.screen = screen
        self.center = [width // 2, height // 2]
        self.scale = 100
        self.scale_inner = 100
        self.angle_x = self.angle_y = self.angle_z = 0
        self.angle_x_inner = self.angle_y_inner = self.angle_z_inner = 0
        self.speed = 0.04

        self.cube_points_outer = [
            np.array([-1, -1, 1]), np.array([1, -1, 1]), np.array([1, 1, 1]), np.array([-1, 1, 1]),
            np.array([-1, -1, -1]), np.array([1, -1, -1]), np.array([1, 1, -1]), np.array([-1, 1, -1])
        ]

        self.cube_points_inner = [
            np.array([-0.5, -0.5, 0.5]), np.array([0.5, -0.5, 0.5]), np.array([0.5, 0.5, 0.5]), np.array([-0.5, 0.5, 0.5]),
            np.array([-0.5, -0.5, -0.5]), np.array([0.5, -0.5, -0.5]), np.array([0.5, 0.5, -0.5]), np.array([-0.5, 0.5, -0.5])
        ]

        self.projected_cube_points_outer = [[0, 0] for _ in self.cube_points_outer]
        self.projected_cube_points_inner = [[0, 0] for _ in self.cube_points_inner]

        self.projection_matrix = np.array([
            [1, 0, 0],
            [0, 1, 0]
        ])

    def handle_keys(self, keys):
        if keys[pygame.K_r]:
            self.angle_x = self.angle_y = self.angle_z = 0
            self.angle_x_inner = self.angle_y_inner = self.angle_z_inner = 0
        if keys[pygame.K_a]:
            self.angle_y += self.speed
            self.angle_y_inner -= self.speed
        if keys[pygame.K_d]:
            self.angle_y -= self.speed
            self.angle_y_inner += self.speed
        if keys[pygame.K_w]:
            self.angle_x += self.speed
            self.angle_x_inner -= self.speed
        if keys[pygame.K_s]:
            self.angle_x -= self.speed
            self.angle_x_inner += self.speed
        if keys[pygame.K_e]:
            self.scale -= 2
            self.scale_inner += 2
            self.scale = max(-1, self.scale)
            self.scale_inner = max(1, self.scale_inner)
        if keys[pygame.K_q]:
            self.scale += 2
            self.scale_inner -= 2
            self.scale = max(1, self.scale)
            self.scale_inner = max(-1, self.scale_inner)

    def connect_cube_points(self, i, j, cube_points):
        pygame.draw.line(self.screen, (0, 0, 0), (cube_points[i][0], cube_points[i][1]), (cube_points[j][0], cube_points[j][1]))

    def draw(self):
        rotation_z_outer = np.array([
            [cos(self.angle_z), -sin(self.angle_z), 0],
            [sin(self.angle_z), cos(self.angle_z), 0],
            [0, 0, 1]
        ])
        rotation_y_outer = np.array([
            [cos(self.angle_y), 0, sin(self.angle_y)],
            [0, 1, 0],
            [-sin(self.angle_y), 0, cos(self.angle_y)]
        ])
        rotation_x_outer = np.array([
            [1, 0, 0],
            [0, cos(self.angle_x), -sin(self.angle_x)],
            [0, sin(self.angle_x), cos(self.angle_x)]
        ])

        rotation_z_inner = np.array([
            [cos(self.angle_z_inner), -sin(self.angle_z_inner), 0],
            [sin(self.angle_z_inner), cos(self.angle_z_inner), 0],
            [0, 0, 1]
        ])
        rotation_y_inner = np.array([
            [cos(self.angle_y_inner), 0, sin(self.angle_y_inner)],
            [0, 1, 0],
            [-sin(self.angle_y_inner), 0, cos(self.angle_y_inner)]
        ])
        rotation_x_inner = np.array([
            [1, 0, 0],
            [0, cos(self.angle_x_inner), -sin(self.angle_x_inner)],
            [0, sin(self.angle_x_inner), cos(self.angle_x_inner)]
        ])

        for i, point in enumerate(self.cube_points_outer):
            rotated = rotation_z_outer @ point.reshape((3, 1))
            rotated = rotation_y_outer @ rotated
            rotated = rotation_x_outer @ rotated
            projected = self.projection_matrix @ rotated
            x = int(projected[0][0] * self.scale + self.center[0])
            y = int(projected[1][0] * self.scale + self.center[1])
            self.projected_cube_points_outer[i] = [x, y]
            pygame.draw.circle(self.screen, (255, 255, 255), (x, y), 1)

        for i, point in enumerate(self.cube_points_inner):
            rotated = rotation_z_inner @ point.reshape((3, 1))
            rotated = rotation_y_inner @ rotated
            rotated = rotation_x_inner @ rotated
            projected = self.projection_matrix @ rotated
            x = int(projected[0][0] * self.scale_inner + self.center[0])
            y = int(projected[1][0] * self.scale_inner + self.center[1])
            self.projected_cube_points_inner[i] = [x, y]
            pygame.draw.circle(self.screen, (255, 255, 255), (x, y), 1)

        for p in range(4):
            self.connect_cube_points(p, (p + 1) % 4, self.projected_cube_points_outer)
            self.connect_cube_points(p + 4, ((p + 1) % 4) + 4, self.projected_cube_points_outer)
            self.connect_cube_points(p, p + 4, self.projected_cube_points_outer)
            self.connect_cube_points(p, (p + 1) % 4, self.projected_cube_points_inner)
            self.connect_cube_points(p + 4, ((p + 1) % 4) + 4, self.projected_cube_points_inner)
            self.connect_cube_points(p, p, self.projected_cube_points_inner)
            self.connect_cube_points((p + 1) % 4, (p + 1) % 4, self.projected_cube_points_inner)
            self.connect_cube_points(p, (p + 1) % 4, self.projected_cube_points_inner)
            self.connect_cube_points(p + 4, ((p + 1) % 4) + 4, self.projected_cube_points_inner)
            self.connect_cube_points(p, p + 4, self.projected_cube_points_outer)
            self.connect_cube_points((p + 1) % 4, (p + 1) % 4 + 4, self.projected_cube_points_outer)
            self.connect_cube_points(p + 4, (p + 4) % 8, self.projected_cube_points_outer)
            self.connect_cube_points((p + 1) % 4 + 4, ((p + 1) % 4 + 1) % 4 + 4, self.projected_cube_points_inner)
            self.connect_cube_points(p, p + 4, self.projected_cube_points_inner)
