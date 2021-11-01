import numpy as np 
from math import pi

def ITF(rpy):
    """
    rpy = (γ，β，α,theta)
    """
    R=[]
    R.append([1-2*rpy[1]**2-2*rpy[2]**2, 2*(rpy[0]*rpy[1]-rpy[2]*rpy[3]), 2*(rpy[0]*rpy[2]+rpy[1][3])])
    R.append([2*rpy[0]*rpy[1]+rpy[2]*rpy[3], 1-2*rpy[0]**2-2*rpy[2]**2, 2*(rpy[1]*rpy[2]-rpy[0]*rpy[3])])
    R.append([2*(rpy[0]*rpy[2]-rpy[1]*rpy[3]), 2*(rpy[1]*rpy[2]+rpy[0]*rpy[3]), 1-2*(rpy[0]**2-2*rpy[1]**2)])
    return R
