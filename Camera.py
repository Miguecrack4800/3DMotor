import math
from GameObject import GameObject

class Camera(GameObject):
    def __init__(self, position: list = [0,0,0]):
        self.position = position
        self.looking_dir = [0,0]