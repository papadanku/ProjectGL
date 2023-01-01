
"""
Extends the CylindricalGeometry class to generate prism geometry
"""

from geometry.cylindricalGeometry import CylindricalGeometry

class PrismGeometry(CylindricalGeometry):

    def __init__(self, radius=1, height=1, radialSegments=32, heightSegments=4, closed=True):
        super().__init__(0, radius, height, radialSegments, heightSegments, False, closed)
