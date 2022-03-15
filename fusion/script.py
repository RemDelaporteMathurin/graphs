import numpy as np
import matplotlib.pyplot as plt
import matplotx

ratio = 4.94  # ratio Pfus/Palpha (=5 w/o relativistic effects; =4.94 w/ relativistic effects)
Meff = 2.55
C_loss = 0.086
C_fus = 1.38e-3
C_beta = 0.726
C_I = 13.144
C_SL = 0.0562
C_n = 3.183
q_a = 3
epsilon = 1/3.1
kappa = 1.75
n_N = 0.85
gamma_rad = 0.7
beta_N = 1.7

# n.T.tau_e and beta_N expressions
def nTtau_fromQ(Q=10, lambd=ratio):
    " n.T.tau_e from eq (2.18) "
    return C_loss/(C_fus*gamma_rad) * Q / (1 + Q/lambd)

def Q_from_nTtau(nTtau, lambd=ratio):
    Q = (C_loss/(C_fus*gamma_rad) * nTtau**-1 - 1/lambd)**-1
    return Q

def nTtau_from_RB(R, B):
    return (R**0.42*B**0.73*C_SL*C_n**0.41*C_I**0.96*C_beta**0.38*C_loss**(-0.69)*Meff**0.19*kappa**0.09*epsilon**0.68*q_a**(-0.96)*n_N**0.41*beta_N**(-0.38))**(1/0.31)

def Q_from_RB(R, B):
    return Q_from_nTtau(nTtau_from_RB(R, B))

print(Q_from_nTtau(nTtau_fromQ(10)))  # should return 10

R = np.linspace(0, 9, num=100)
B = np.linspace(0, 15, num=100)

BB, RR = np.meshgrid(B, R)
Q = Q_from_RB(RR, BB)
Q = np.ma.masked_where(Q < 0, Q)

with plt.style.context(matplotx.styles.dufte):
    # plt.scatter(5.3, 6.2)
    # plt.scatter(9, 3)
    CS = plt.contour(BB, RR, Q, levels=[0.2, 1, 5, 20], colors="tab:grey")
    plt.clabel(CS, levels=[0.2], fmt="Q = %1.1f")
    plt.clabel(CS, levels=[1, 5], fmt="Q = %1.0f")
    plt.clabel(CS, levels=[20], fmt="Q = %1.0f", manual=[(7, 5)])
    plt.gca().set_aspect('equal')
    plt.xlabel("B (T)")
    matplotx.ylabel_top("R (m)")
    plt.show()
