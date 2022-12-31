
"""
This module performs general rendering tasks such as
- Depth testing
- Antialiasing
- Color clearing
"""

from OpenGL.GL import *

from core.mesh import Mesh

class Renderer(object):

    def __init__(self, clearColor=[0,0,0]):

        # Enable depth testing
        glEnable(GL_DEPTH_TEST)
        # Required for antialiasing
        glEnable(GL_MULTISAMPLE)
        glClearColor(clearColor[0], clearColor[1], clearColor[2], 1)

    def render(self, scene, camera):
        # Clear color and depth buffers
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # Update camera view (calculate inverse)
        camera.updateViewMatrix()

        # Extract a list of the scene's mesh objects
        descendantList = scene.getDescendantList()
        meshFilter = lambda x : isinstance(x, Mesh)
        meshList = list(filter(meshFilter, descendantList))

        for mesh in meshList:

            # If this object is not visible, continue to next object in list
            if not mesh.visible:
                continue

            glUseProgram(mesh.material.programReference)

            # Bind VAO
            glBindVertexArray(mesh.vaoReference)

            # Update uniform values stored outside of material
            mesh.material.uniforms["modelMatrix"].data = mesh.getWorldMatrix()
            mesh.material.uniforms["viewMatrix"].data = camera.viewMatrix
            mesh.material.uniforms["projectionMatrix"].data = camera.projectionMatrix

            # Update uniforms stored in material
            for variableName, uniformObject in mesh.material.uniforms.items():
                uniformObject.uploadData()

            # Update render settings
            mesh.material.updateRenderSettings()

            glDrawArrays(mesh.material.settings["drawStyle"], 0, mesh.geometry.vertexCount)