import numpy as np 
from math import pi

def TF(R):
    """
    R = [[x1,x2,x3],
         [y1,y2,y3],
         [z1,z2,z3]]
    """
    Q = np.arccos((R[0][0]+R[1][1]+R[2][2]-1)/2)
    gema = 0 if (np.abs(Q)<np.finfo(float).eps or np.abs(np.abs(Q)-pi)<np.finfo(float).eps) else Q*0.5*(R[2][1]-R[1][2])/np.sin(Q)
    beta = 0 if (np.abs(Q)<np.finfo(float).eps or np.abs(np.abs(Q)-pi)<np.finfo(float).eps) else Q*0.5*(R[0][2]-R[2][0])/np.sin(Q)
    alpha = 0 if (np.abs(Q)<np.finfo(float).eps or np.abs(np.abs(Q)-pi)<np.finfo(float).eps) else Q*0.5*(R[1][0]-R[0][1])/np.sin(Q)
    return [gema,beta,alpha]
