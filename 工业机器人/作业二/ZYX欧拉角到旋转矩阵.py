import numpy as np

def zyxRpyToRotationMatrix(rpy):
    R = []
    sx = np.sin(rpy[0])
    cx = np.cos(rpy[0])
    sy = np.sin(rpy[1])
    cy = np.cos(rpy[1])
    sz = np.sin(rpy[2])
    cz = np.cos(rpy[2])
    R.append([cy*cz,cz*sx*sy - cx*sz ,sx*sz + cx*cz*sy])
    R.append([cy*sz,cx*cz + sx*sy*sz,cx*sy*sz - cz*sx])
    R.append([-sy,cy*sx,cx*cy])
    return R
