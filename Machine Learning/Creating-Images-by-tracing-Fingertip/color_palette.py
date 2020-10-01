from cv2 import rectangle

class ColorPalette:

    delta_x = 30
    delta_y = 30
    thickness = -1

    def __init__(self, image, color, pivot_point):
        self.color = color
        self.pivot_point = pivot_point
        self.image = image

    def create_color_palette(self):
        return rectangle(self.image, self.pivot_point, (self.pivot_point[0]+self.delta_x, self.pivot_point[1]+self.delta_y), self.color, self.thickness)



