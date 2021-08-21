import math
from GameObject import GameObject
from Camera import Camera

class Player(GameObject):
    def __init__(self, camera: Camera, pos: list = [0,0,0]):
        self.hitbox = [1,2,1]
        self.rel_campos = [0.5, 1.5, 0.5]
        self.position = pos
        self.camera = camera

    def tick(self):
        self.camera.position = [self.position[0] + self.rel_campos[0], self.position[1] + self.rel_campos[1], self.position[2] + self.rel_campos[2]]