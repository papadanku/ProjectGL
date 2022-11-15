
"""
Processes application's vertex attibutes
"""

import numpy
from OpenGL.GL import *

class Attribute(object):

    def __init__(self, dataType, data):
        """
        - Initializes the object's attributes
        - Generates a buffer
        - Stores the data into the buffer
        """

        # Type of elements in a data array:
        # int | float | vec2 | vec3 | vec4
        self.dataType = dataType

        # Array of data to be stored in a buffer
        self.data = data

        # Reference of available buffer from the GPU
        self.bufferReference = glGenBuffers(1)

        # Immediately upload data
        self.uploadData()
    
    def uploadData(self):
        """
        - Converts the object's data
        - Uploads the object's data to the GPU buffer
        """

        # Converts data to numpy's array format; converts numbers to 32-bit floats
        data = numpy.array(self.data).astype(numpy.float32)

        # Create/select the vertex attribute buffer used by the following functions
        # NOTE: GL_ARRAY_BUFFER's purpose is to store vertex attributes
        glBindBuffer(GL_ARRAY_BUFFER, self.bufferReference)

        # Store the object's data in the currently bound buffer
        glBufferData(GL_ARRAY_BUFFER, data.ravel(), GL_STATIC_DRAW)

    def associateVariable(self, programReference, variableName):
        """
        Function that associates the variable with a GPU's vertex attribute buffer
        - Get the attribute's name and location within the program 
        - Activate the array buffer that Attribute() generated 
        - Provide the array buffer information on OpenGL should interpret this buffer's memory
        """

        # Get reference for program variable with given name
        variableReference = glGetAttribLocation(programReference, variableName)

        # If the program does not reference the variable, then exit
        if variableReference == -1:
            return
        
        # Select the buffer used by the following functions
        glBindBuffer(GL_ARRAY_BUFFER, self.bufferReference)

        # Specify how data will be read from the bound buffer to the specified variable
        if self.dataType == "int":
            glVertexAttribPointer(variableReference, 1, GL_INT, False, 0, None)
        elif self.dataType == "float":
            glVertexAttribPointer(variableReference, 1, GL_FLOAT, False, 0, None)
        elif self.dataType == "vec2":
            glVertexAttribPointer(variableReference, 2, GL_FLOAT, False, 0, None)
        elif self.dataType == "vec3":
            glVertexAttribPointer(variableReference, 3, GL_FLOAT, False, 0, None)
        elif self.dataType == "vec4":
            glVertexAttribPointer(variableReference, 4, GL_FLOAT, False, 0, None)
        else:
            raise Exception("Attribute " + variableName + " has unknown type " + self.dataType)

        # Indicate that data will be streamed to this variable
        # NOTE: Basically, we enable the vertex attribute array (variableReference)
        glEnableVertexAttribArray(variableReference)