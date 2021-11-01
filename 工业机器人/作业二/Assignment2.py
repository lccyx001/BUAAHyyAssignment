import numpy as np
from math import pi


def make_matrix(func):
    # 将list转换成matrix
    def resolve_parameters(arg1):
        return np.mat(func(arg1))
    return resolve_parameters


class G(object):

    eps = np.finfo(float).eps

# 等效转轴到旋转矩阵


@make_matrix
def ITF1(rpy):
    """
    rpy = (γ，β，α,theta)
    """
    R = []
    Q = np.sqrt(rpy[0]**2+rpy[1]**2+rpy[2]**2)
    if Q > G.eps:
        k = [rpy[0]/Q, rpy[1]/Q, rpy[2]/Q]
        sx = np.sin(Q)
        cx = np.cos(Q)
        v = 1-cx
        R.append([k[0]**2*v+cx, k[0]*k[1]*v-k[2]*sx, k[0]*k[2]*v+k[1]*sx])
        R.append([k[0]*k[1]*v+k[2]*sx, k[1]**2*v+cx, k[1]*k[2]*v-k[0]*sx])
        R.append([k[0]*k[2]*v-k[1]*sx, k[1]*k[2]*v+k[0]*sx, k[2]**2*v+cx])
    else:
        R.append([1, 0, 0])
        R.append([0, 1, 0])
        R.append([0, 0, 1])
    return R

# 四元素到旋转矩阵


@make_matrix
def ITF(rpy):
    """
    rpy = (γ，β，α,theta)
    """
    R = []
    R.append([1-2*rpy[1]**2-2*rpy[2]**2, 2*(rpy[0]*rpy[1] -
             rpy[2]*rpy[3]), 2*(rpy[0]*rpy[2]+rpy[1]*rpy[3])])
    R.append([2*rpy[0]*rpy[1]+rpy[2]*rpy[3], 1-2*rpy[0]**2 -
             2*rpy[2]**2, 2*(rpy[1]*rpy[2]-rpy[0]*rpy[3])])
    R.append([2*(rpy[0]*rpy[2]-rpy[1]*rpy[3]), 2 *
             (rpy[1]*rpy[2]+rpy[0]*rpy[3]), 1-2*(rpy[0]**2-2*rpy[1]**2)])
    return R


# 旋转矩阵到等效转轴
def TF(R):
    """
    R = [[x1,x2,x3],
         [y1,y2,y3],
         [z1,z2,z3]]
    """
    Q = np.arccos((R[0][0]+R[1][1]+R[2][2]-1)/2)
    gema = 0 if (np.abs(Q) < G.eps or np.abs(np.abs(Q)-pi) <
                 G.eps) else Q*0.5*(R[2][1]-R[1][2])/np.sin(Q)
    beta = 0 if (np.abs(Q) < G.eps or np.abs(np.abs(Q)-pi) <
                 G.eps) else Q*0.5*(R[0][2]-R[2][0])/np.sin(Q)
    alpha = 0 if (np.abs(Q) < G.eps or np.abs(np.abs(Q)-pi) <
                  G.eps) else Q*0.5*(R[1][0]-R[0][1])/np.sin(Q)
    return [gema, beta, alpha]

# 旋转矩阵到四元素


def rotationMatrixToQuaternion(R):
    """
    R = [[x1,x2,x3],
         [y1,y2,y3],
         [z1,z2,z3]]
    """
    m = 0.5*np.sqrt(1+R[0][0]+R[1][1]+R[2][2])
    gema = 0 if np.abs(m) < G.eps else (R[2][1]-R[1][2])/(4*m)
    beta = 0 if np.abs(m) < G.eps else (R[1][2]-R[2][0])/(4*m)
    alpha = 0 if np.abs(m) < G.eps else (R[1][0]-R[0][1])/(4*m)
    theta = 0 if np.abs(m) < G.eps else m

    return [gema, beta, alpha, theta]

# 旋转矩阵到XYZ固定角


def rotationMatrixToXYZ(R):
    """
    R = [[x1,x2,x3],
         [y1,y2,y3],
         [z1,z2,z3]]
    """
    beta = np.arctan2(-R[2][0], np.sqrt(R[0][0]**2+R[1][0]**2))
    if np.abs(np.abs(beta)-pi/2) < G.eps:
        gema = np.arctan2(R[0][1], R[1][1]) if beta > 0 else - \
            np.arctan2(R[0][1], R[1][1])
        beta = pi/2 if beta > 0 else -pi/2
        alpha = 0
    else:
        gema = -np.arctan2(R[0][1], R[1][1])
        beta = -pi/2
        alpha = 0
    return [gema, beta, alpha]


# 旋转矩阵到XYZ欧拉角
def rotationMatrixToXYZRPY(R):
    """
    R = [[x1,x2,x3],
         [y1,y2,y3],
         [z1,z2,z3]]
    """
    if np.abs(R[2][2]) < G.eps:
        gema = 0
        beta = pi/2
        alpha = np.arctan2(R[1][0], R[1][1])
    else:
        gema = np.arctan2(-R[1][2], R[2][2])
        s = np.sin(gema)
        c = np.cos(gema)
        beta = np.arctan2(R[0][2], c*R[2][2]-s*R[1][2])
        alpha = np.arctan2(-R[0][1], R[0][0])
    return [gema, beta, alpha]

# 旋转矩阵到ZYX欧拉角


def rotationMatrixToZYXRPY(R):
    """
    R = [[x1,x2,x3],
         [y1,y2,y3],
         [z1,z2,z3]]
    """
    beta_tmp = np.arctan2(-R[2][0], np.sqrt(R[0][0]*R[0][0]+R[1][0]*R[1][0]))
    if np.abs(np.abs(beta_tmp) - np.pi/2) < G.eps:
        alpha = 0
        beta = pi/2 if beta_tmp > 0 else -pi/2
        gema = np.arctan2(R[0][1], R[1][1]) if beta_tmp > 0 else - \
            np.arctan2(R[0][1], R[1][1])
    else:
        cp = np.cos(beta_tmp)
        beta = beta_tmp
        gema = np.arctan2(R[2][1]/cp, R[2][2]/cp)
        alpha = np.arctan2(R[1][0]/cp, R[0][0]/cp)
    return [gema, beta, alpha]

# XYZ固定角到旋转矩阵


@make_matrix
def xyzToRotationMatrix(rpy):
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
    R.append([cy*cz, cz*sx*sy - cx*sz, sx*sz + cx*cz*sy])
    R.append([cy*sz, cx*cz + sx*sy*sz, cx*sy*sz - cz*sx])
    R.append([-sy, cy*sx, cx*cy])

    return R

# XYZ欧拉角至旋转矩阵


@make_matrix
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
    R.append([cy*cz, -cy*sz, sy])
    R.append([cx*sz + cz*sx*sy, cx*cz - sx*sy*sz, -cy*sx])
    R.append([sx*sz - cx*cz*sy, cz*sx + cx*sy*sz, cx*cy])

    return R

# ZYX欧拉角到旋转矩阵


@make_matrix
def zyxRpyToRotationMatrix(rpy):
    R = []
    sx = np.sin(rpy[0])
    cx = np.cos(rpy[0])
    sy = np.sin(rpy[1])
    cy = np.cos(rpy[1])
    sz = np.sin(rpy[2])
    cz = np.cos(rpy[2])
    R.append([cy*cz, cz*sx*sy - cx*sz, sx*sz + cx*cz*sy])
    R.append([cy*sz, cx*cz + sx*sy*sz, cx*sy*sz - cz*sx])
    R.append([-sy, cy*sx, cx*cy])
    return R


def main():
    print("等效转轴到旋转矩阵")
    print(ITF1([90, 90, 90]))
    print("四元素到旋转矩阵")
    print(ITF([90, 90, 90, 90]))
    print("旋转矩阵到等效转轴")
    print(TF([[0, 0, 1], [0, -1, 0], [1, 0, 0]]))
    print("旋转矩阵到四元素")
    print(rotationMatrixToQuaternion([[0, 0, 1], [0, -1, 0], [1, 0, 0]]))
    print("旋转矩阵到XYZ固定角")
    print(rotationMatrixToXYZ([[0, 0, 1], [0, -1, 0], [1, 0, 0]]))
    print("旋转矩阵到XYZ欧拉角")
    print(rotationMatrixToXYZRPY([[0, 0, 1], [0, -1, 0], [1, 0, 0]]))
    print("旋转矩阵到ZYX欧拉角")
    print(rotationMatrixToZYXRPY([[0, 0, 1], [0, -1, 0], [1, 0, 0]]))
    print("XYZ固定角到旋转矩阵")
    print(xyzToRotationMatrix([90,90,90]))
    print("XYZ欧拉角至旋转矩阵")
    print(xyzRpyToRotationMatrix([90,90,90]))
    print("ZYX欧拉角到旋转矩阵")
    print(zyxRpyToRotationMatrix([90, 90, 90]))


if __name__ == "__main__":
    main()
