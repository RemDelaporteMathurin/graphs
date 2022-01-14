import matplotlib.pyplot as plt
import matplotlib.patches as patches
import sympy as sp


def solve_equations(law):
    Kr_f = sp.Symbol("Kr_f")
    D_f = sp.Symbol("D_f")
    D_s = sp.Symbol("D_s")

    K_H_s = sp.Symbol("K_H_s")
    K_S_s = sp.Symbol("K_S_s")
    K_S_f = sp.Symbol("K_S_f")

    c_0 = sp.Symbol("c_0")
    c_int_left = sp.Symbol("c_int_left")
    c_int_right = sp.Symbol("c_int_right")
    c_max = sp.Symbol("c_max")

    l_foil = sp.Symbol("l_foil")
    R_p = sp.Symbol("R_p")
    phi_imp = sp.Symbol("flux")

    list_of_equations = [
        phi_imp - Kr_f*c_0**2,
        phi_imp - (c_int_left - c_0)/l_foil*D_f,
        phi_imp - (c_max - c_int_right)/R_p*D_s,
    ]
    if law == "sieverts":
        list_of_equations.append(
            c_int_left/K_S_f - c_int_right/K_S_s
        )
    elif law == "henry":
        list_of_equations.append(
            c_int_left**2/K_S_f**2 - c_int_right/K_H_s
        )
    results = sp.solve(list_of_equations, [c_0, c_int_left, c_int_right, c_max])
    c_0 = sp.simplify(results[1][0])
    c_int_left = sp.simplify(results[1][1])
    c_int_right = sp.simplify(results[1][2])
    c_max = sp.simplify(results[1][3])
    print('c_max')
    print(c_max)
    return c_0, c_int_left, c_int_right, c_max

try:
    plt.rc('text', usetex=True)
    plt.rc('font', family='serif', size=12)
except:
    pass


c_0, c_int_left, c_int_right, c_max = solve_equations("henry")
l_foil = 3
l_salt = 10
size = l_foil + l_salt
phi_imp = 1
R_p = 2
D_foil = 1
D_salt = 1

K_S_f = 1

K_H_s = 2
K_S_s = 2

Kr_f = 1

Rds = [R_p + 4, R_p + 5, R_p + 6]

c_0 = c_0.subs("flux", phi_imp).subs("Kr_f", Kr_f)
c_int_left = c_int_left.subs("flux", phi_imp).subs("Kr_f", Kr_f).subs("l_foil", l_foil).subs("D_f", D_foil)
c_int_right = c_int_right.subs("flux", phi_imp).subs("Kr_f", Kr_f).subs("l_foil", l_foil).subs("D_f", D_foil).subs("K_S_f", K_S_f).subs("K_S_s", K_S_s).subs("K_H_s", K_H_s)
c_max = c_max.subs("flux", phi_imp).subs("Kr_f", Kr_f).subs("l_foil", l_foil).subs("D_f", D_foil).subs("K_S_f", K_S_f).subs("K_S_s", K_S_s).subs("K_H_s", K_H_s).subs("R_p", R_p).subs("D_s", D_salt)

c_max = float(c_max)  # don't really understand why but this is needed


def make_profile(R_d):
    x = [0, l_foil, l_foil, l_foil + R_p, l_foil + R_d, size]
    y = [c_0, c_int_left, c_int_right, c_max, 0, 0]
    return x, y


plt.figure(figsize=(6.4, 3))


for i, Rd in enumerate(Rds):
    x, y = make_profile(Rd)
    if i == 0:
        linestyle = "solid"
    else:
        linestyle = "dashed"
    plt.plot(x, y, c="black", linestyle=linestyle)


plt.hlines(c_max, 0,  l_foil + R_p + 1, linestyle="dashed", color="grey")
plt.vlines(l_foil + R_p, 0, c_max*1.05, linestyle="dashed", color="grey")

plt.ylim(bottom=0, top=c_max*1.2)
plt.xlim(left=0)
plt.xticks([0, l_foil + R_p, l_foil +  Rds[0]], [0, "$R_p$", "$R_d$"])
plt.yticks([0, c_0, c_max], [0, "$c_0$", r"$c_\mathrm{max}$"])

plt.xlabel("$x$")

length_arrow = 1
pos_x_arrow = l_foil + R_p + 0.5
plt.annotate("", xy=(pos_x_arrow + length_arrow, c_max*1.1), xytext=(pos_x_arrow, c_max*1.1),
             arrowprops=dict(arrowstyle="->"))
plt.annotate(r"$\varphi_\mathrm{bulk}$", xy=(l_foil + R_p + 0.65, c_max*1.15))


pos_x_arrow = l_foil + R_p - 0.5
plt.annotate("", xy=(pos_x_arrow - length_arrow, c_max*1.1), xytext=(pos_x_arrow, c_max*1.1),
             arrowprops=dict(arrowstyle="->"))
plt.annotate(r"$\varphi_\mathrm{recomb}$", xy=(l_foil + R_p - 1.5, c_max*1.15))


rect_salt = patches.Rectangle((l_foil, 0), l_salt, c_max*1.2, linewidth=1, edgecolor=None, facecolor="tab:green", alpha=0.2)
plt.gca().add_patch(rect_salt)
rect_foil = patches.Rectangle((0, 0), l_foil, c_max*1.2, linewidth=1, edgecolor=None, facecolor="tab:grey", alpha=0.2)
plt.gca().add_patch(rect_foil)

plt.gca().spines['right'].set_visible(False)
plt.gca().spines['top'].set_visible(False)
plt.tight_layout()
plt.show()
