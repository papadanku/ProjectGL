
"""
Module for generating the following transformation matricies:
- Identity
- Translation
- Rotation
- Scale
- Perspective
"""

from math import sin, cos, tan, pi

import numpy

class Matrix(object):

    @staticmethod
    def makeIdentity():
        return numpy.array([
            [1.0, 0.0, 0.0, 0.0],
            [0.0, 1.0, 0.0, 0.0],
            [0.0, 0.0, 1.0, 0.0],
            [0.0, 0.0, 0.0, 1.0]
        ])

    @staticmethod
    def makeTranslation(x, y, z):
        return numpy.array([
            [1.0, 0.0, 0.0, x],
            [0.0, 1.0, 0.0, y],
            [0.0, 0.0, 1.0, z],
            [0.0, 0.0, 0.0, 1.0]
        ])

    @staticmethod
    def makeRotationX(angle):
        c = cos(angle)
        s = sin(angle)
        return numpy.array([
            [1.0, 0.0, 0.0, 0.0],
            [0.0,   c,  -s, 0.0],
            [0.0,   s,   c, 0.0],
            [0.0, 0.0, 0.0, 1.0]
        ])

    @staticmethod
    def makeRotationY(angle):
        c = cos(angle)
        s = sin(angle)
        return numpy.array([
            [   c, 0.0,   s, 0.0],
            [ 0.0, 1.0, 0.0, 0.0],
            [  -s, 0.0,   c, 0.0],
            [ 0.0, 0.0, 0.0, 1.0]
        ])

    @staticmethod
    def makeRotationZ(angle):
        c = cos(angle)
        s = sin(angle)
        return numpy.array([
            [  c,  -s, 0.0, 0.0],
            [  s,   c, 0.0, 0.0],
            [0.0, 0.0, 1.0, 0.0],
            [0.0, 0.0, 0.0, 1.0]
        ])

    @staticmethod
    def makeScale(s):
        return numpy.array([
            [  s, 0.0, 0.0, 0.0],
            [0.0,   s, 0.0, 0.0],
            [0.0, 0.0,   s, 0.0],
            [0.0, 0.0, 0.0, 1.0]
        ])

    @staticmethod
    def makePerspective(angleOfView=60.0, aspectRatio=1.0, near=0.1, far=1000.0):
        a = angleOfView * pi / 180.0
        d = 1.0 / tan(a / 2.0)
        r = aspectRatio
        b = (far + near) / (near - far)
        c = (2.0 * far * near)/ (near - far)
        return numpy.array([
            [d/r, 0.0,  0.0, 0.0],
            [0.0,   d,  0.0, 0.0],
            [0.0, 0.0,    b,   c],
            [0.0, 0.0, -1.0, 0.0]
        ])
