class Circle:
    def draw(self):
        print("Drawing Circle")

class Square:
    def draw(self):
        print("Drawing Square")

def draw_shape(shape):
    shape.draw()

draw_shape(Circle())
draw_shape(Square())
