
"""
Module for static methods to load and compile OpenGL shaders and link to create programs
"""

from OpenGL.GL import *

class OpenGLUtils(object):

    @staticmethod
    def initializeShader(shaderCode, shaderType):
        """
        Compiles shader and checks to see if compilation was successful
        Returns the shader's information plus its reference number
        """
        
        # Specify required OpenGL/GLSL version
        shaderCode = '#version 330\n' + shaderCode

        # Create an empty shader object and its return reference value
        # NOTE: OpenGL uses glCreateShader() to supply the correct built-in variables when compiling a shader
        shaderReference = glCreateShader(shaderType)

        # Store the source code in the shader object
        glShaderSource(shaderReference, shaderCode)

        # Compile the shader object
        # NOTE: glCompileShader() also stores the compilation status into the shader object
        glCompileShader(shaderReference)

        # Queries whether shader compilation was successful
        compileSuccess = glGetShaderiv(shaderReference, GL_COMPILE_STATUS)

        if not compileSuccess:
            # Retrieve error message
            errorMessage = glGetShaderInfoLog(shaderReference)

            # Free memory used to store shader program
            glDeleteShader(shaderReference)

            # Convert byte string to character string
            errorMessage = '\n' + errorMessage.decode('utf-8')

            # Raise exception: halt program and print error message
            raise Exception(errorMessage)
        
        # Compilation was successful; return shader's reference value and its compiled code
        # NOTE: The shaderReference value is the shader object's ID
        return shaderReference

    @staticmethod
    def initializeProgram(vertexShaderCode, fragmentShaderCode):
        """
        Creates a program by linking the vertex and fragment shaders together
        Returns the program's information plus its reference number
        """

        # Create an empty program object and store reference to it
        programReference = glCreateProgram()

        # NOTE: Compile the vertex and fragment shaders, and get their reference value
        vertexShaderReference = OpenGLUtils.initializeShader(vertexShaderCode, GL_VERTEX_SHADER)
        fragmentShaderReference = OpenGLUtils.initializeShader(fragmentShaderCode, GL_FRAGMENT_SHADER)

        # Attach the vertex and fragment shaders to the program
        glAttachShader(programReference, vertexShaderReference)
        glAttachShader(programReference, fragmentShaderReference)

        # Link the vertex shader to the fragment shader
        glLinkProgram(programReference)

        # Queries whether program link was successful
        linkSuccess = glGetProgramiv(programReference, GL_LINK_STATUS)

        if not linkSuccess:
            # Retrieve error message
            errorMessage = glGetProgramInfoLog(programReference)

            # Free memory used to store the program
            glDeleteProgram(programReference)

            # Convert byte string into character string
            errorMessage = '\n' + errorMessage.decode('utf-8')

            # Raise exception: halt application and print error message
            raise Exception(errorMessage)
        
        # Linking was successful, return program's reference value
        # NOTE: The programReference value is the program object's ID
        return programReference

    @staticmethod
    def printSystemInfo():
        print("Vendor: " + glGetString(GL_VENDOR).decode('utf-8'))
        print("Renderer: " + glGetString(GL_RENDERER).decode('utf-8'))
        print("Supported OpenGL version: " + glGetString(GL_VERSION).decode('utf-8'))
        print("Supported GLSL version: " + glGetString(GL_SHADING_LANGUAGE_VERSION).decode('utf-8'))
