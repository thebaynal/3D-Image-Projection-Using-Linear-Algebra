import button
import pygame

class Buttons:
    def __init__(self, screen):
        #load images
        self.legend_img = pygame.image.load("images\legend.png").convert_alpha()

        self.cube_img = pygame.image.load("images\cube.png").convert_alpha() #1
        self.cube_within_img = pygame.image.load("images\cubew.png").convert_alpha() #2
        self.dodeca_img = pygame.image.load("images\dodeca.png").convert_alpha() #3
        self.sphere_img = pygame.image.load("images/sphere.png").convert_alpha() #4
        self.great_img = pygame.image.load("images\great.png").convert_alpha() #5
        self.tetrahedron_img = pygame.image.load("images/tetra.png").convert_alpha() #6
        self.octahedron_img = pygame.image.load("images/octahedron.png").convert_alpha() #7
        self.cross_img = pygame.image.load("images/cross.png").convert_alpha()  #9
        self.rhombic_img = pygame.image.load("images/rhombicuboctahedron.png").convert_alpha()
        self.tria = pygame.image.load("images/tria.png").convert_alpha()

        #pressed buttons
        self.pcube_img = pygame.image.load("images/18.png").convert_alpha()
        self.pcube_within_img = pygame.image.load("images/19.png").convert_alpha()
        self.pdodeca_img = pygame.image.load("images/22.png").convert_alpha()
        self.prectangular_img = pygame.image.load("images/25.png").convert_alpha()
        self.pgreat_img = pygame.image.load("images/24.png").convert_alpha() #5
        self.ptetrahedron_img = pygame.image.load("images/21.png").convert_alpha()
        self.poctahedron_img = pygame.image.load("images/23.png").convert_alpha()
        self.pcross_img = pygame.image.load("images/pcross.png").convert_alpha()
        self.psphere_img = pygame.image.load("images/psphere.png").convert_alpha()
        self.prhombic_img = pygame.image.load("images/prhombi.png").convert_alpha()
        self.ptria = pygame.image.load("images/ptria.png").convert_alpha()

        # Create Buttons
        self.legend_button = button.Button(1040, -130, self.legend_img, 0.07)

        self.buttons = {
            "cube": {
                "normal": button.Button(10, 600, self.cube_img, 0.058),
                "pressed": button.Button(10, 600, self.pcube_img, 0.058),
            },
            "cube-within-a-cube": {
                "normal": button.Button(280, 600, self.cube_within_img, 0.058),
                "pressed": button.Button(280, 600, self.pcube_within_img, 0.058),
            },
            "pyramid": {
                "normal": button.Button(550, 600, self.tetrahedron_img, 0.058),
                "pressed": button.Button(550, 600, self.ptetrahedron_img, 0.058),
            },
            "octahedron": {
                "normal": button.Button(820, 600, self.octahedron_img, 0.058),
                "pressed": button.Button(820, 600, self.poctahedron_img, 0.058),
            },
            "dodecahedron": {
                "normal": button.Button(1090, 600, self.dodeca_img, 0.058),
                "pressed": button.Button(1090, 600, self.pdodeca_img, 0.058),
            },
            "great": {
                "normal": button.Button(280, 690, self.great_img, 0.0577),
                "pressed": button.Button(280, 690, self.pgreat_img, 0.058),
            },
            "cross": {
                "normal": button.Button(820, 690, self.cross_img, 0.45),
                "pressed": button.Button(820, 690, self.pcross_img, 0.058),
            },
            "rhombicuboctahedron": {
                "normal": button.Button(10, 510, self.rhombic_img, 0.455),
                "pressed": button.Button(10, 510, self.prhombic_img, 0.455),
            },
            "Rhombic-Triacontahedron": {
                "normal": button.Button(1090, 510, self.tria, 0.455),
                "pressed": button.Button(1090, 510, self.ptria, 0.455),
            },
        }

    def draw(self, screen, current_mode):
        mode = None
        # Always draw the legend
        self.legend_button.draw(screen)

        # Draw all the shape buttons
        for name, states in self.buttons.items():
            if current_mode == name:
                if states["pressed"].draw(screen):
                    mode = name
                    print(f"Button {name} pressed")
            else:
                if states["normal"].draw(screen):
                    mode = name
                    print(f"Button {name} pressed")
        return mode