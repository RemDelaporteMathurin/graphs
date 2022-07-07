import numpy as np
import matplotlib.pyplot as plt
import matplotx

exponent = 1 / 3


def gaussian(x, mu, sigma):
    return (
        1 / (sigma * np.sqrt(2 * np.pi)) * np.exp(-((x - mu) ** 2) / (2 * sigma**2))
    )


def sum_of_powers(i, ci, exponent=2):
    return np.sum(ci * ((i / 4) ** exponent)) / np.sum(ci)


def power_of_sum(i, ci, exponent=2):
    return (np.sum(ci * (i / 4)) / np.sum(ci)) ** exponent


def plot_sum(exponent, fun, **kwargs):
    mu = 500
    i = np.arange(0, 2 * mu, step=1)
    sigmas = np.linspace(1e1, 1e4, num=1000)
    y = []
    for sigma in sigmas:
        ci = gaussian(i, mu, sigma)
        y.append(fun(i, ci=ci, exponent=exponent))
    y = np.array(y)
    plt.plot(sigmas / mu, y / ((mu / 4) ** exponent), **kwargs)


plt.figure(figsize=(6.4, 3))

# plot_sum(exponent=2, fun=sum_of_powers, label="$\sum c_i i^b / \sum c_i $  b = {}".format(2))
plot_sum(
    exponent=1 / 3,
    fun=sum_of_powers,
    label=r"$\frac{\sum c_i (i/4)^{1/3} }{ \sum c_i }$",
)


plot_sum(
    exponent=1 / 3,
    fun=power_of_sum,
    label=r"$\left(\frac{\sum c_i (i/4)}{\sum c_i} \right) ^{1/3}$",
)


plt.xlabel("$\sigma / \mu$")
plt.ylabel("value normalised by $(\mu/4)^{1/3}$")
plt.xscale("log")

plt.ylim(bottom=0.8)
matplotx.line_labels(fontsize=14)

plt.tight_layout()
plt.gca().spines.right.set_visible(False)
plt.gca().spines.top.set_visible(False)

plt.figure(figsize=(3, 2.5))

mu, sigma = 50, 5
x = np.arange(mu - 3 * sigma, mu + 3 * sigma, step=1)
y = gaussian(x, mu, sigma)
plt.bar(x, height=y, alpha=0.5)

plt.hlines(gaussian(mu - sigma, mu, sigma), mu - sigma, mu + sigma, color="black")
plt.annotate(
    "$2 \sigma$", (mu, gaussian(mu - sigma, mu, sigma)), va="bottom", ha="center"
)

plt.xticks([mu], ["$\mu$"])
plt.yticks([])
matplotx.ylabel_top("$c_i$")
plt.gca().yaxis.get_label().set_fontsize(16)
plt.xlabel("$i$", loc="right", fontsize=16)

plt.tight_layout()
plt.gca().spines.right.set_visible(False)
plt.gca().spines.top.set_visible(False)
plt.show()
