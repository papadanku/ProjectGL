
"""
Extension of the basicMaterial.py module for creating a point material's shaders, uniforms, and render settings
"""

from OpenGL.GL import *

from material.basicMaterial import BasicMaterial

class PointMaterial(BasicMaterial):

    def __init__(self, properties=dict()):

        # Setup BasicMaterial properties
        super().__init__()
        
        ### Setup default pointMaterial settings ###

        # Render verticies as points
        self.settings["drawStyle"] = GL_POINTS
        # Width and height of points, in pixels
        self.settings["pointSize"] = 8
        # Draw points as rounded
        self.settings["roundedPoints"] = False

        # Setup properties
        self.setProperties(properties)
    
    def updateRenderSettings(self):
        
        glPointSize(self.settings["pointSize"])

        if self.settings["roundedPoints"]:
            glEnable(GL_POINT_SMOOTH)
        else:
            glDisable(GL_POINT_SMOOTH)
