
"""
Expands the BasicMaterial class to create a line material's shaders, uniforms, and render settings
"""

from OpenGL.GL import *

from material.basicMaterial import BasicMaterial

class LineMaterial(BasicMaterial):

    def __init__(self, properties=dict()):

        # Setup BasicMaterial properties
        super().__init__()

        ### Setup default lineMaterial settings ###

        # Render verticies as continuous line by default
        self.settings["drawStyle"] = GL_LINE_STRIP
        # Line thickness
        self.settings["lineWidth"] = 1
        # Line type: "connected" | "loop" | "segments"
        self.settings["lineType"] = "connected"

        # Setup properties
        self.setProperties(properties)

    def updateRenderSettings(self):

        glLineWidth(self.settings["lineWidth"])

        if self.settings["lineType"] == "connected":
            self.settings["drawStyle"] = GL_LINE_STRIP
        elif self.settings["lineType"] == "loop":
            self.settings["drawStyle"] = GL_LINE_LOOP
        elif self.settings["lineType"] == "segments":
            self.settings["drawStyle"] = GL_LINES
        else:
            raise Exception("Unknown LineMaterial draw style.")
