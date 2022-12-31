
"""
Extends the EllipsoidGeometry class to generate a spherical geometry
"""

from math import sin, cos, pi

from geometry.ellipsoidGeometry import EllipsoidGeometry

class SphereGeometry(EllipsoidGeometry):
    def __init__(self, radius=1, radiusSegments=32, heightSegments=16):
        super().__init__(2*radius, 2*radius, 2*radius, radiusSegments, heightSegments)
