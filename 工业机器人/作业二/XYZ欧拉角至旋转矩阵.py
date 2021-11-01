import numpy as np
def xyzRpyToRotationMatrix(rpy):
    """
    rpy = (γ，β，α)
    """
    R = []
    sx = np.sin(rpy[0])
    cx = np.cos(rpy[0])
    sy = np.sin(rpy[1])
    cy = np.cos(rpy[1])
    sz = np.sin(rpy[2])
    cz = np.cos(rpy[2])
    R.append([cy*cz,-cy*sz ,sy])
    R.append([cx*sz + cz*sx*sy,cx*cz - sx*sy*sz,-cy*sx])
    R.append([sx*sz - cx*cz*sy,cz*sx + cx*sy*sz,cx*cy])
	
    return R