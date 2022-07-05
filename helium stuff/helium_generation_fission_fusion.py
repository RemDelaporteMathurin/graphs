# reproduced from 'Materials research for fusion' J. Knaster et al
# DOI: 10.1038/NPHYS3735
# https://www.nature.com/articles/nphys3735


import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse

color_cycle = plt.rcParams['axes.prop_cycle'].by_key()['color']

ells = [
    # fission
    Ellipse((np.log10(1.2), np.log10(0.1)), 5, 0.6, 45),
    # ITER
    Ellipse((np.log10(1.5), np.log10(11)), 1, 0.15, 45),
    # Fusion reactor
    Ellipse((np.log10(90), np.log10(900)), 1.25, 0.15, 45),
    ]

labels = [
    ("Fission \n reactors", (np.log10(1e-2), np.log10(0.1))),
    ("ITER", (np.log10(0.2), np.log10(11))),
    ("Fusion \n reactors", (np.log10(50), np.log10(150))),
]

fig = plt.subplot(111, aspect="equal")
for (i, (e, s)) in enumerate(zip(ells, labels)):
    color = color_cycle[i]
    e.set_clip_box(fig.bbox)
    e.set_alpha(0.5)
    e.set_facecolor(color)
    fig.add_artist(e)

    plt.text(*s[1], s[0], color=color)


plt.xlim(np.log10(1e-4), np.log10(1e3))
plt.ylim(np.log10(1e-3), np.log10(1e4))
ax = plt.gca()
xtickslocs = ax.get_xticks()
plt.xticks(xtickslocs, labels=["$10^{" + '{:.0f}'.format(tick) + '}$' for tick in xtickslocs])
ytickslocs = ax.get_yticks()
plt.yticks(ytickslocs, labels=["$10^{" + '{:.0f}'.format(tick) + '}$' for tick in ytickslocs])

plt.grid(True)
plt.xlabel("Displacement damage (dpa)")
plt.ylabel("He generation (appm)")

plt.show()
