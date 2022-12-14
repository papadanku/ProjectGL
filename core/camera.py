
from numpy.linalg import inv

from core.object3D import Object3D
from core.matrix import Matrix

class Camera(Object3D):

    def __init__(self, angleOfView=60.0, aspectRatio=1.0, near=0.1, far=1000.0):
        super().__init__()

        self.projectionMatrix = Matrix.makePerspective(angleOfView, aspectRatio, near, far)
        self.viewMatrix = Matrix.makeIdentity()

    def updateViewMatrix(self):
        self.viewMatrix = inv(self.getWorldMatrix())
