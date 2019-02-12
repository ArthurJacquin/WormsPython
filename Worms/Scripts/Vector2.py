class Vector2:
    def __init__(self, x=0., y=0.):
        self.x = x
        self.y = y

    def __add__(self, vec):
        vec2 = Vector2(self.x + vec.x, self.y + vec.y)
        return vec2

    def __sub__(self, vec):
        vec2 = Vector2(self.x - vec.x, self.y - vec.y)
        return vec2

    def __mul__(self,a):
        vec2 = Vector2(self.x * a, self.y * a)
        return vec2