import matplotlib.pyplot as plt
import numpy as np


try:
    plt.rc('text', usetex=True)
    plt.rc('font', family='serif', size=12)
except:
    pass


size = 10
c_0 = 1
phi_imp = 1
R_p = 2
D = 1

Rds = [5, 6, 7]

cmax = c_0 + phi_imp*R_p/D


def make_profile(R_d):
    x = [0, R_p, R_d, size]
    y = [c_0, cmax, 0, 0]
    return x, y


for i, Rd in enumerate(Rds):
    x, y = make_profile(Rd)
    if i == 0:
        linestyle = "solid"
    else:
        linestyle = "dashed"
    plt.plot(x, y, c="black", linestyle=linestyle)


plt.hlines(cmax, 0, size*0.25, linestyle="dashed", color="grey")
plt.vlines(R_p, 0, cmax*1.05, linestyle="dashed", color="grey")

plt.ylim(bottom=0, top=cmax*1.2)
plt.xlim(left=0)
plt.xticks([0, R_p, Rds[0]], [0, "$R_p$", "$R_d$"])
plt.yticks([0, c_0, cmax], [0, "$c_0$", r"$c_\mathrm{max}$"])

plt.xlabel("$x$")

length_arrow = 1
pos_x_arrow = R_p + 0.5
plt.annotate("", xy=(pos_x_arrow + length_arrow, cmax*1.1), xytext=(pos_x_arrow, cmax*1.1),
             arrowprops=dict(arrowstyle="->"))
plt.annotate(r"$\varphi_\mathrm{bulk}$", xy=(R_p + 0.65, cmax*1.15))


pos_x_arrow = R_p - 0.5
plt.annotate("", xy=(pos_x_arrow - length_arrow, cmax*1.1), xytext=(pos_x_arrow, cmax*1.1),
             arrowprops=dict(arrowstyle="->"))
plt.annotate(r"$\varphi_\mathrm{recomb}$", xy=(R_p - 1.5, cmax*1.15))


plt.gca().spines['right'].set_visible(False)
plt.gca().spines['top'].set_visible(False)

plt.show()
