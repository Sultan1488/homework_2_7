class Rectangle:
    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height
        print(f'Length: {length}\n'
              f'Width: {width}\n'
              f'Height: {height}')

        if type(length) != int:
            raise ValueError
        if type(width) != int:
            raise ValueError
        if type(height) != int:
            raise ValueError
        if length < 0:
            raise ValueError
        if width < 0:
            raise ValueError
        if height < 0:
            raise ValueError
    
    def calculate_volume(self):
        volume_rectangle = self.length * self.width * self.height
        print(volume_rectangle)
