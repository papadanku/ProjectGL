
from OpenGL.GL import *

class Uniform(object):

    def __init__(self, dataType, data):
        """
        Initialize the variable's attributes
        """

        # Type of data
        # int | bool | float | vec2 | vec3 | vec4
        self.dataType = dataType

        # Data to be sent to the uniform variable
        self.data = data

        # Location for variable location in the program
        self.variableReference = None

    def locateVariable(self, programLocation, variableName):
        """
        Get and store the variable's name and location within the program
        """
        self.variableReference = glGetUniformLocation(programLocation, variableName)

    def uploadData(self):
        """
        Store the data in the located uniform variable
        """

        # Exit if the program does not reference the variable
        if self.variableReference == -1:
            return
        
        if self.dataType == "int":
            glUniform1i(self.variableReference, self.data)
        elif self.dataType == "bool":
            glUniform1i(self.variableReference, self.data)
        elif self.dataType == "float":
            glUniform1f(self.variableReference, self.data)
        elif self.dataType == "vec2":
            glUniform2f(self.variableReference, self.data[0], self.data[1])
        elif self.dataType == "vec3":
            glUniform3f(self.variableReference, self.data[0], self.data[1], self.data[2])
        elif self.dataType == "vec4":
            glUniform4f(self.variableReference, self.data[0], self.data[1], self.data[2], self.data[3])
