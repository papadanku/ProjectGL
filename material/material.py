
"""
Module for creating and updating a geometry's material
- Shaders
- Uniform data
- Render settings
"""

from OpenGL.GL import *

from core.openGLUtils import OpenGLUtils
from core.uniform import Uniform

class Material(object):

    def __init__(self, vertexShaderCode, fragmentShaderCode):

        self.programReference= OpenGLUtils.initializeProgram(vertexShaderCode, fragmentShaderCode)

        # Store uniform object, indexed by name of associated variable in shader
        self.uniforms = dict()

        # Each shader typically contains these uniforms
        # Values will be set during render process from mesh or camera.
        # Add additional uniforms by extending classes
        self.uniforms["modelMatrix"] = Uniform("mat4", None)
        self.uniforms["viewMatrix"] = Uniform("mat4", None)
        self.uniforms["projectionMatrix"] = Uniform("mat4", None)

        # Store OpenGL render settings, indexed by variable name.
        # Additional settings added by extending classes.
        self.settings = dict()
        self.settings["drawStyle"] = GL_TRIANGLES

    def addUniform(self, dataType, variableName, data):
        self.uniforms[variableName] = Uniform(dataType, data)

    # Initialize all uniform variable references
    def locateUniforms(self):
        for variableName, uniformObject in self.uniforms.items():
            uniformObject.locateVariable(self.programReference, variableName)

    # Configure OpenGL with render settings
    def updateRenderSettings(self):
        pass

    # Convenience method for setting multiple material "properties"
    # (uniform and render settings values) from a dictionary
    def setProperties(self, properties):
        for name, data in properties.items():
            # Update uniforms
            if name in self.uniforms.keys():
                self.uniforms[name].data = data
            # Update render settings
            elif name in self.settings.keys():
                self.settings[name] = data
            # Unknown property type
            else:
                raise Exception("Material has no property named: " + name)
