
"""
Extends the ParametricGeometry class to generate cylindrical geometry
"""

from math import sin, cos, pi

from core.matrix import Matrix

from geometry.parametricGeometry import ParametricGeometry
from geometry.polygonGeometry import PolygonGeometry

def lerp(x, y, z):
    """
    Basic linear interpolation
    -> (x * (1.0 - z)) + (y * z)
    """
    return (x * (1.0 - z)) + (y * z)

class CylindricalGeometry(ParametricGeometry):

    def __init__(self, radiusTop=1, radiusBottom=1, height=1, radialSegments=32, heightSegments=4, closedTop=True, closedBottom=True):

        # Cylindrical surface function
        def S(u,v):
            closedCap = lerp(radiusBottom, radiusTop, v)
            return [
                closedCap * sin(u),
                height * (v - 0.5),
                closedCap * cos(u)
            ]

        # Generate base parametric geometry without the closed top and bottom
        super().__init__(0, 2 * pi, radialSegments, 0, 1, heightSegments, S)

        # Merge the base parametric geometry with the closed top
        if closedTop:
            topGeometry = PolygonGeometry(radialSegments, radiusTop)
            transform = Matrix.makeTranslation(0, height / 2, 0)
            topGeometry.applyMatrix(transform)
            self.merge(topGeometry)
        
        # Merge the base parametric geometry with the closed bottom
        if closedBottom:
            bottomGeometry = PolygonGeometry(radialSegments, radiusBottom)
            transform = Matrix.makeTranslation(0, -height / 2, 0) @ Matrix.makeRotationY(pi / 2)
            bottomGeometry.applyMatrix(transform)
            self.merge(bottomGeometry)
