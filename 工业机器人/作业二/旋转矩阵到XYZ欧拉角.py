from math import pi
import numpy as np 

def rotationMatrixToXYZRPY(R):
    """
    R = [[x1,x2,x3],
         [y1,y2,y3],
         [z1,z2,z3]]
    """
    if np.abs(R[2][2])<np.finfo(float).eps:
        gema = 0
        beta = pi/2
        alpha = np.arctan2(R[1][0],R[1,1])
    else:
        gema = np.arctan2(-R[1][2],R[2][2])
        s= np.sin(gema)
        c = np.cos(gema)
        beta = np.arctan2(R[0][2],c*R[2][2]-s*R[1][2])
        alpha = np.arctan2(-R[0][1],R[0][0])
    return [gema,beta,alpha]
