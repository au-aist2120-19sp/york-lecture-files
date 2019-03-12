class point:
    '''A simple class representing a two dimensional point'''
    x = 0
    y = 0

    # "CONSTRUCTOR" method...MUST set the x & y
    # when creating a point
    def __init__(self, x, y):
        self.set(x,y)

    def set(self, x, y):
        '''set a new x and y coordinate'''
        self.x = x
        self.y = y
    
    def add(self,otherpoint):
        '''add "otherpoint" to this point'''
        self.x += otherpoint.x
        self.y += otherpoint.y
    
    def subtract(self,otherpoint):
        '''subtract "otherpoint" from this point'''
        self.x -= otherpoint.x
        self.y -= otherpoint.y
    
    def distance(self,otherpoint):
        '''get the absolute distance from this point to "otherpoint"'''
        from math import sqrt

        xdif = abs(self.x - otherpoint.x)
        ydif = abs(self.y - otherpoint.y)
        dist = sqrt(xdif**2 + ydif**2)
        return dist
