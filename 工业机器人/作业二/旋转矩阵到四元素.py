import numpy as np 

def rotationMatrixToQuaternion(R):
    """
    R = [[x1,x2,x3],
         [y1,y2,y3],
         [z1,z2,z3]]
    """
    m = 0.5*np.sqrt(1+R[0][0]+R[1][1]+R[2][2])
    gema = 0 if np.abs(m)<np.finfo(float).eps else (R[2][1]-R[1][2])/(4*m)
    beta = 0 if np.abs(m)<np.finfo(float).eps else (R[1][2]-R[2][0])/(4*m)
    alpha = 0 if np.abs(m)<np.finfo(float).eps else (R[1][0]-R[0][1])/(4*m)
    theta = 0 if np.abs(m)<np.finfo(float).eps else m 
    
    return [gema,beta,alpha,theta]
