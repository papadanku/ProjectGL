
"""
Module that extends the Object3D class to generate an object's geometry and matrial information
"""

from OpenGL.GL import *

from core.object3D import Object3D

class Mesh(Object3D):

    def __init__(self, geometry, material):

        # Create Object3D object for expansion
        super().__init__()

        self.geometry = geometry
        self.material = material

        # Should this object be rendered?
        self.visible = True

        """
        Setup associations between adttributes stored
        in geometry and shader program stored in material
        """
        self.vaoReference = glGenVertexArrays(1)
        glBindVertexArray(self.vaoReference)

        for variableName, attributeObject in geometry.attributes.items():
            attributeObject.associateVariable(material.programReference, variableName)

        # Unbind this vertex array object
        glBindVertexArray(0)
