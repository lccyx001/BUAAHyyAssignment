from math import pi
import numpy as np 

def rotationMatrixToXYZ(R):
    """
    R = [[x1,x2,x3],
         [y1,y2,y3],
         [z1,z2,z3]]
    """
    beta = np.arctan2(-R[2][0],np.sqrt(R[0][0]**2+R[1][0]**2))
    if np.abs(np.abs(beta)-pi/2)<np.finfo(float).eps:
        gema = np.arctan2(R[0][1],R[1][1])
        beta = pi/2
        alpha = 0
    else:
        gema = -np.arctan2(R[0][1],R[1][1])
        beta = -pi/2
        alpha = 0
    return [gema,beta,alpha]
