
"""
Extends the ParametricGeometry class to generate plane geometry
"""

from geometry.parametricGeometry import ParametricGeometry

class PlaneGeometry(ParametricGeometry):

    def __init__(self, width=1, height=1, widthSegments=8, heightSegments=8):

        # Plane surface function
        def S(u, v):
            return [u, v, 0]

        super().__init__(-width, width, widthSegments, -height, height, heightSegments, S)
