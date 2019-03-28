class player:
    def __init__(self):
        self.__name__ = 'anonymous'
        self.__wins__ = 0
    
    def get_name(self):
        return self.__name__
    
    def set_name(self, name):
        self.__name__ = name

    def get_wins(self):
        return self.__wins__
    
    def set_wins(self, wins):
        self.__wins__ = wins

