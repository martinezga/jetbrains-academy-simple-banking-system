import math


class Hexagon:
    def __init__(self, side_length):
        self.side_length = side_length

    def get_area(self):
        return '{:.3f}'.format((1 / 2) * 3 * math.sqrt(3) * (self.side_length ** 2))


"""
Hexagon
The class Hexagon represents the regular hexagons
(all sides are equal in length and all angles equal \(120 ^ \circ\)). 
The only parameter needed to create a regular hexagon is the length of its side \(t\) .

Create a method get_areathat calculates the area of the hexagon according to the formula:

\(S = \frac{3\sqrt{3} * t^2}{2}\).

The name of the method has to be get_area! 
The method doesn't receive any parameters and it doesn't print anything, 
just returns the calculated area (rounded to 3 decimals). 
You do NOT need to call the method in your program!

To calculate the square root use the math.sqrt(x) method. (The math module has already been imported.)

Nothing else is required (you do NOT need to work with the input).

Sample Input:
1
Sample Output:
2.598

Sample Input:
5.4
Sample Output:
75.760

Caution
You may see errors in your code or execution results due to missing context. 
Don’t worry about it, just write the solution and press Check.
"""