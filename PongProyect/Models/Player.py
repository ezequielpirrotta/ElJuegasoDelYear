class Player():
    
    width = 0
    height = 0
    colour = (0,0,0)
    default_pos = (0,0)
    pos_x = 0
    pos_y = 0
    points = 0
    
    def __init__(self, width, height, colour, default_pos):
        self.width = width
        self.height = height
        self.colour = colour
        self.default_pos = default_pos
        self.pos_x = self.default_pos[0]
        self.pos_y = self.default_pos[1]

    def move(self, speed):
        self.pos_y += speed
    
    def point(self):
        self.points += 1 
    
    def set_default(self):
        self.pos_x = self.default_pos[0]
        self.pos_y = self.default_pos[1]
        self.points = 0 
