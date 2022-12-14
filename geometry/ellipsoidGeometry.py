
"""
Extends the ParametricGeometry class to generate ellipsoid geometry
"""

from math import sin, cos, pi

from geometry.parametricGeometry import ParametricGeometry

class EllipsoidGeometry(ParametricGeometry):

    def __init__(self, width=1, height=1, depth=1, radiusSegments=32, heightSegments=16):

        # Ellipsoid surface function
        def S(u,v):
            return [
                 width * sin(u) * cos(v),
                height * sin(v),
                 depth * cos(u) * cos(v)
            ]

        super().__init__(0, 2.0 * pi, radiusSegments, -pi / 2.0, pi / 2.0, heightSegments, S)
