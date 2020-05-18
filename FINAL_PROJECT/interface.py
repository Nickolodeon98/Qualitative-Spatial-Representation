class interface:
    def __init__(self):
        self.x = None
        self.y = None
        self.width = None
        self.height = None

    def show(self):
        self.x = input('Enter the coordinates of the region you want to start with.\nx: ')
        while (int(self.x) < 1 or int(self.x) > 18):
            print('Wrong input!')
            self.x = input('x: ')
        self.y = input('y: ')
        while (int(self.y) < 1 or int(self.y) > 18):
            print('Wrong input!')
            self.y = input('y: ')

        self.width = input('Enter the width and height of the region you want to start with.\nwidth: ')
        while (self.width.isnumeric() == False):
            print('Wrong input!')
            self.width = input('width: ')
        while (int(self.width) < 2 or int(self.width) > 20):
            print('Wrong input!')
            self.width = input('width: ')

        self.height = input('height: ')
        while (self.height.isnumeric() == False):
            print('Wrong input!')
            self.height = input('height: ')
        while (int(self.height) < 2 or int(self.height) > 20):
            print('Wrong input!')
            self.height = input('height: ')