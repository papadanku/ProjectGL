
"""
Module to create and update a geometry's material
- Shaders
- Uniform data
- Render settings
"""

from OpenGL.GL import *

from core.openGLUtils import OpenGLUtils
from core.uniform import Uniform

class Material(object):

    def __init__(self, vertexShaderCode, fragmentShaderCode):
        
        # Create program using a vertex and fragment shader
        self.programReference = OpenGLUtils.initializeProgram(vertexShaderCode, fragmentShaderCode)

        # Store uniform object, indexed by name of associated variable in shader
        # NOTE: Additional uniforms added by extending the class.
        self.uniforms = dict()

        # Each shader typically contains these uniforms
        # NOTE: Values will be set during render process from mesh or camera.
        # NOTE: Add additional uniforms by extending classes
        self.uniforms["modelMatrix"] = Uniform("mat4", None)
        self.uniforms["viewMatrix"] = Uniform("mat4", None)
        self.uniforms["projectionMatrix"] = Uniform("mat4", None)

        # Store OpenGL render settings, indexed by variable name.
        # NOTE: Additional settings added by extending the class.
        self.settings = dict()
        self.settings["drawStyle"] = GL_TRIANGLES

    def addUniform(self, dataType, variableName, data):
        self.uniforms[variableName] = Uniform(dataType, data)

    def locateUniforms(self):
        """
        Locates all of the shader program's uniforms
        """

        for variableName, uniformObject in self.uniforms.items():
            uniformObject.locateVariable(self.programReference, variableName)

    # Configure OpenGL with render settings
    def updateRenderSettings(self):
        pass


    def setProperties(self, properties):
        """
        # Convenience method for setting multiple material "properties" (uniform and render settings values) from a dictionary
        """
        
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
