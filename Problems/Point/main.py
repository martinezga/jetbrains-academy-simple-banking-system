class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist(self, p2):
        return ((self.x - p2.x) ** 2 + (self.y - p2.y) ** 2) ** 0.5


"""
Point
Create a class Point that will represent a point in space. 
Its constructor needs two parameters \(x\) and \(y\), the coordinates of a point on the plane. 
The class should have a method dist that takes another instance of Point and returns the Euclidean 
distance between these two points. For Point(x1, y1) and Point(x2, y2), calculate the distance 
according to the formula:

\[d = \sqrt{(x_1 - x_2)^2 + (y_1 - y_2)^2}\]Have a look at the following example:

p1 = Point(1.5, 1)
p2 = Point(1.5, 2)

print(p1.dist(p2))  # 1.0
Just create the class, you won't need anything else.

Caution
You may see errors in your code or execution results due to missing context. 
Don’t worry about it, just write the solution and press Check.
"""