
"""
Extension of the basicMaterial.py module for creating a surface material's shaders, uniforms, and render settings
"""

from OpenGL.GL import *

from material.basicMaterial import BasicMaterial

class SurfaceMaterial(BasicMaterial):

    def __init__(self, properties=dict()):

        # Setup BasicMaterial properties
        super().__init__()

        ### Setup default surfaceMaterial settings ###

        # Render verticies as surface
        self.settings["drawStyle"] = GL_TRIANGLES
        # Render both sides? default: front-side only
        # NOTE: verticies ordered counterclockwise
        self.settings["doubleSide"] = False
        # Render triangles as wireframe?
        self.settings["wireframe"] = False
        # Line thickness for wireframe rendering
        self.settings["lineWidth"] = 1

        # Setup properties
        self.setProperties(properties)

    def updateRenderSettings(self):
        
        if self.settings["doubleSide"]:
            glDisable(GL_CULL_FACE)
        else:
            glEnable(GL_CULL_FACE)
        
        if self.settings["wireframe"]:
            glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
        else:
            glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)

        glLineWidth(self.settings["lineWidth"])