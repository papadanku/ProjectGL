
"""
Extends the EllipsoidGeometry class to generate a spherical geometry
"""

from geometry.ellipsoidGeometry import EllipsoidGeometry

class SphereGeometry(EllipsoidGeometry):

    def __init__(self, radius=1.0, radiusSegments=32, heightSegments=16):
        super().__init__(radius, radius, radius, radiusSegments, heightSegments)
