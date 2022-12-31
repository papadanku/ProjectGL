
"""
Module to create an geometry information
"""

from core.attribute import Attribute

class Geometry(object):

    def __init__(self):
        """
        Stores attribute objects, indexed by name of the associated variable in shader.

        Shader variable associations setup later and store in the mesh's vertex array object
        """

        self.attributes = dict()

        # Number of verticies
        self.vertexCount = None

    def addAttribute(self, dataType, variableName, data):
        """
        Adds an attribute and its information into a vertex buffer
        """

        self.attributes[variableName] = Attribute(dataType, data)

    def countVertices(self):
        """
        Returns a number of vertices may be calculated from the length of any attribute object's data array
        """

        attrib = list(self.attributes.values())[0]
        self.vertexCount = len(attrib.data)

    def applyMatrix(self, matrix, variableName = "variablePosition"):
        """
        Applies a matrix transformation to a list of attributes (mainly vertex positions)

        This is useful for if you want to create a closed top and bottom of a Cylinder
        """

        oldPositionData = self.attributes[variableName].data
        newPositionData = list()

        for oldPosition in oldPositionData:
            # Avoid changing list referneces
            newPosition = oldPosition.copy()
            # Add homogeneous fourth coordinate
            newPosition.append(1.0)
            # Matrix multiply
            newPosition = matrix @ newPosition
            # Remove homogeneous coordinate
            newPosition = list(newPosition[0:3])
            # Add to a new data list
            newPositionData.append(newPosition)

        self.attributes[variableName].data = newPositionData
        # New data must be uploaded
        self.attributes[variableName].uploadData()

    def merge(self, otherGeometry):
        """
        Merge data from attribute of other geometry into this object

        NOTE: Requires both geometries to have attributes with same names
        """

        for variableName, attributeObject in self.attributes.items():
            attributeObject.data += otherGeometry.attributes[variableName].data
            # We must upload the new merged data to the vertex buffer object
            attributeObject.uploadData()

        # Update the number of verticies
        self.countVertices()
