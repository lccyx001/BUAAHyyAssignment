import numpy as np 
from math import pi

def ITF(rpy):
    """
    rpy = (γ，β，α,theta)
    """
    R = []
    Q = np.sqrt(rpy[0]**2+rpy[1]**2+rpy[2]**2)
    if Q > np.finfo(float).eps:
         k = [rpy[0]/Q,rpy[1]/Q,rpy[2]/Q]
         sx = np.sin(Q)
         cx = np.cos(Q)
         v = 1-cx
         R.append([k[0]**2*v+cx,k[0]*k[1]*v-k[2]*sx,k[0]*k[2]*v+k[1]*sx])
         R.append([k[0]*k[1]*v+k[2]*sx,k[1]**2+cx,k[1]*k[2]*v-k[0]*sx])
         R.append([k[0]*k[2]*v+k[1]*sx,k[1]*k[2]*v+k[0]*sx,k[2]**2*v+cx])
    else:
         R.append([1,0,0])
         R.append([0,1,0])
         R.append([0,0,1])
    return R
