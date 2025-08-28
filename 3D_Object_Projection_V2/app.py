import pygame
import button
from buttons import Buttons

from shapes.cross import Cross
from shapes.rhombic_triacontehedron import RhombicTriacontahedron
from shapes.tetrahedron import Tetrahedron
from shapes.dodecahedron import Dodecahedron
from shapes.great_dodecahedron import GreatDodecahedron
from shapes.cube import Cube
from shapes.cube_within_cube import CubeWithinCube
from shapes.rhombic_octahedron import Rhombicuboctahedron
from shapes.octahedron import Octahedron


class App:
    def __init__(self, width=1290, height=740, title="3D Shape Projection"):
        pygame.init()
        self.width = width
        self.height = height
        self.title = title
        self.screen = pygame.display.set_mode((self.width, self.height), pygame.FULLSCREEN)
        pygame.display.set_caption(self.title)

        self.clock = pygame.time.Clock()
        self.mode = ""
        self.speed = 0.04
        self.running = True

        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.RED = (255, 0, 0)
        self.BLUE = (0, 0, 255)
        self.current_color = self.RED

        self.auto = False

        # ✅ IMPORTANT: Store the Buttons instance as self.buttons
        self.buttons = Buttons(self.screen)

        # Angle placeholders
        self.angle_x = 0.0
        self.angle_y = 0.0
        self.angle_z = 0.0
        
        self.angle_x_inner = 0.0
        self.angle_y_inner = 0.0
        self.angle_z_inner = 0.0

        #Shape instances
        self.cross = Cross(self.screen, self.width, self.height)
        self.rhombic = RhombicTriacontahedron(self.screen, self.width, self.height)
        self.tetrahedron = Tetrahedron(self.screen, self.width, self.height)
        self.dodecahedron = Dodecahedron(self.screen, self.width, self.height)
        self.great_dodecahedron = GreatDodecahedron(self.screen, self.width, self.height)
        self.cube = Cube(self.screen, self.width, self.height)
        self.cube_within_cube = CubeWithinCube(self.screen, self.width, self.height)
        self.rhombic_octahedron = Rhombicuboctahedron(self.screen, self.width, self.height)
        self.octahedron = Octahedron(self.screen, self.width, self.height)


    def run(self):
        while self.running:
            self.clock.tick(60)
            self.screen.fill(self.WHITE)

            # Call draw() on the instance
            selected_mode = self.buttons.draw(self.screen, self.mode)

            self.draw_shape(self.mode)

            # If the user clicked a new mode, update the current mode
            if selected_mode:
                self.mode = selected_mode

            self.handle_events()

            pygame.display.flip()

    def draw_shape(self, mode):
        match mode:
            case "cross":
                keys = pygame.key.get_pressed()
                self.cross.handle_keys(keys)
                if self.auto:
                    self.cross.angle_x += self.cross.speed
                    self.cross.angle_y += self.cross.speed
                    self.cross.angle_z += self.cross.speed
                self.cross.draw()
            case "Rhombic-Triacontahedron":
                keys = pygame.key.get_pressed()
                self.rhombic.handle_keys(keys)
                if self.auto:
                    self.rhombic.angle_x += self.rhombic.speed
                    self.rhombic.angle_y += self.rhombic.speed
                    self.rhombic.angle_z += self.rhombic.speed
                self.rhombic.draw()
            case "pyramid":
                keys = pygame.key.get_pressed()
                self.tetrahedron.handle_keys(keys)
                if self.auto:
                    self.tetrahedron.angle_x += self.tetrahedron.speed
                    self.tetrahedron.angle_y += self.tetrahedron.speed
                    self.tetrahedron.angle_z += self.tetrahedron.speed
                self.tetrahedron.draw()
            case "dodecahedron":
                keys = pygame.key.get_pressed()
                self.dodecahedron.handle_keys(keys)
                if self.auto:
                    self.dodecahedron.angle_x += self.dodecahedron.speed
                    self.dodecahedron.angle_y += self.dodecahedron.speed
                    self.dodecahedron.angle_z += self.dodecahedron.speed
                self.dodecahedron.draw()
            case "great":
                keys = pygame.key.get_pressed()
                self.great_dodecahedron.handle_keys(keys)
                if self.auto:
                    self.great_dodecahedron.angle_x += self.great_dodecahedron.speed
                    self.great_dodecahedron.angle_y += self.great_dodecahedron.speed
                    self.great_dodecahedron.angle_z += self.great_dodecahedron.speed
                self.great_dodecahedron.draw()
            case "christmas lantern":
                pass
            case "cube":
                keys = pygame.key.get_pressed()
                self.cube.handle_keys(keys)
                if self.auto:
                    self.cube.angle_x += self.cube.speed
                    self.cube.angle_y += self.cube.speed
                    self.cube.angle_z += self.cube.speed
                self.cube.draw()
            case "cube-within-a-cube":
                keys = pygame.key.get_pressed()
                self.cube_within_cube.handle_keys(keys)
                if self.auto:
                    self.cube_within_cube.angle_x += self.cube_within_cube.speed
                    self.cube_within_cube.angle_y += self.cube_within_cube.speed
                    self.cube_within_cube.angle_z += self.cube_within_cube.speed
                self.cube_within_cube.draw()
            case "rhombicuboctahedron":
                keys = pygame.key.get_pressed()
                self.rhombic_octahedron.handle_keys(keys)
                if self.auto:
                    self.rhombic_octahedron.angle_x += self.rhombic_octahedron.speed
                    self.rhombic_octahedron.angle_y += self.rhombic_octahedron.speed
                    self.rhombic_octahedron.angle_z += self.rhombic_octahedron.speed
                self.rhombic_octahedron.draw()
            case "octahedron":
                keys = pygame.key.get_pressed()
                self.octahedron.handle_keys(keys)
                if self.auto:
                    self.octahedron.angle_x += self.octahedron.speed
                    self.octahedron.angle_y += self.octahedron.speed
                    self.octahedron.angle_z += self.octahedron.speed
                self.octahedron.draw()
            case "sphere":
                keys = pygame.key.get_pressed()
                self.sphere.handle_keys(keys)
                if self.auto:
                    self.sphere.angle_x += self.sphere.speed
                    self.sphere.angle_y += self.sphere.speed
                    self.sphere.angle_z += self.sphere.speed
                self.sphere.draw()



    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()
                if event.key == pygame.K_f:
                    self.auto = not self.auto

if __name__ == "__main__":
    app = App()
    app.run()
