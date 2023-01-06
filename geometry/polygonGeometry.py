
"""
Extends the Geometry class to generate polygon geometry
"""

from math import sin, cos, pi

from geometry.geometry import Geometry

class PolygonGeometry(Geometry):

    def __init__(self, sides=3, radius=1):
        super().__init__()

        A = 2.0 * pi / sides
        positionData = list()
        colorData = []

        # Append position data of the polygon's "sides"
        # Each "side" of a polygon is a triangle
        for n in range(sides):
            # Origin point
            positionData.append([0.0, 0.0, 0.0])
            # Starting point
            positionData.append([radius*cos(n*A), radius*sin(n*A), 0.0])
            # Ending point
            positionData.append([radius*cos((n+1)*A), radius*sin((n+1)*A), 0.0])

            colorData.append([1.0, 1.0, 1.0])
            colorData.append([1.0, 0.0, 0.0])
            colorData.append([0.0, 0.0, 1.0])

        self.addAttribute("vec3", "vertexPosition", positionData)
        self.addAttribute("vec3", "vertexColor", colorData)
        self.countVertices()
