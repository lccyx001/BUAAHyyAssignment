from math import pi
import numpy as np 

def rotationMatrixToZYXRPY(R):
    """
    R = [[x1,x2,x3],
         [y1,y2,y3],
         [z1,z2,z3]]
    """
    beta_tmp = np.arctan2(-R[2][0],np.sqrt(R[0][0]*R[0][0]+R[1][0]*R[1][0]))
    if np.abs(np.abs(beta_tmp) - np.pi/2) <  np.finfo(float).eps:
        alpha = 0
        beta = pi/2 if beta_tmp>0 else -pi/2
        gema =  np.arctan2(R[0][1],R[1][1]) if beta_tmp>0 else -np.arctan2(R[0][1],R[1][1])            
    else:
        cp = np.cos(beta_tmp)
        beta = beta_tmp
        gema = np.arctan2(R[2][1]/cp ,R[2][2]/cp) 
        alpha = np.arctan2(R[1][0]/cp,R[0][0]/cp)
    return [gema,beta,alpha]
