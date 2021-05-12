class Rectangle:
    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height
        print(f'Length: {length}\n'
              f'Width: {width}\n'
              f'Height: {height}')

        if type(length) and type(width) and type(height) not in [int, float] or length < 0 or width < 0 or height < 0:
            raise ValueError
    
    def calculate_volume(self):
        return self.length * self.width * self.height
