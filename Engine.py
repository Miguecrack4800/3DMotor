import pygame
import math
import numpy as np
from skimage import transform
from Camera import Camera

class Engine():
    def __init__(self, screen: pygame.Surface, screensize: tuple, camera: Camera, default_border_color: tuple = (0,0,0), field_of_view : list = [90, 90]):
       self.screen = screen
       self.dft_col = default_border_color
       self.width = 3 # Stroke default width
       self.screensize = screensize
       self.camera = camera
       self.field_of_view = [field_of_view[0] * math.pi / 180, field_of_view[1] * math.pi / 180]

    def normalize(self, angle): # Normalize angle to 0 - 360 = [0, PI*2)
        return angle % (2*math.pi)

    def normalize180(self, angle): # Normalize angle to -180 - +180 = (-PI, PI]
        angle = self.normalize(angle)
        if(angle > math.pi):
            angle -= 2 * math.pi
        return angle

    def get_screen_point(self, Ingame_point): # 3D point -> Screen point (2D, at the screen in 3D)
        x = Ingame_point[0] * self.screensize[0] / self.field_of_view[0] + self.screensize[0] / 2   # Map angles to the screen
        y = Ingame_point[1] * self.screensize[1] / self.field_of_view[1] + self.screensize[1] / 2
        return [x, y]

    def rotate_point(self, Ingame_point):
        campos = self.camera.position
        dz = Ingame_point[2] - campos[2]                    # Get distance from point to camera (dx, dy, dz)
        dx = Ingame_point[0] - campos[0]
        dy = Ingame_point[1] - campos[1]

        angx = math.atan2(dx, dz)                 # Get x angle of the object in respect to the player
        #dz = math.sqrt(dz**2 + dx**2)            # ( Uncomment this line for original problem ) sol: sets the same y angle regardless of x angle.
        angy = math.atan2(-dy, dz)                # Get y angle of the object in respect to the player (-dy because pygame screen cordinates)
        dist = dx**2 + dz**2 + dy**2                 # Get distance ^ 2

        look = self.camera.looking_dir                                   # Get player looking direction (radians)
        nangx = self.normalize180(angx - look[0])                             # Rotate acording to looking direction
        nangy = self.normalize180(angy - look[1])
        return (nangx, nangy, dist)

    def get_plane(self, corners: list): # Get angles from 3D plane
        angles = [] # 3D points -> Angles
        for point in corners:
            angles.append(self.rotate_point(point))
        return angles

    def draw_plane(self, angles, plane_color, image): # Draw plane from angles
        corners = []
        for point in angles:            # convert the angles into points in the screen
            corners.append(self.get_screen_point(point))
        if(plane_color != None):
            pygame.draw.polygon(self.screen, plane_color, corners, 0) # Draw plane 
        else:
            pass # TODO
        #zone = pygame.draw.polygon(self.screen, self.dft_col, corners, self.width) # Draw borders
        return None
    
    def draw_point(self, point, color): # Draw a point
        point = self.get_screen_point(self.rotate_point(point))
        pygame.draw.circle(self.screen, color, point, self.width)
