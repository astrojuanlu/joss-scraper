import seaborn
seaborn.set_style('whitegrid')
import matplotlib.pyplot as plt

 # 13 circle-ci
 # 50 github-actions
 # 72 github-folder
# 110 travis

# 845 False
 # 55 not-github

levels = [13, 50+72, 110, 845]
labels = ["CircleCI", "Github Actions", "Travis", "No obvious CI"]

total = sum(levels)
pc = [level/total*100 for level in levels]

PHI= 1.61803398875
fig_height=4
fig, ax = plt.subplots(figsize=(fig_height*PHI, fig_height))
# ax.spines['right'].set_color((1, 1, 1))
# ax.spines['top'].set_color((1, 1, 1))
plt.bar(labels, pc, color='#ffffff', edgecolor='#222222')
plt.ylabel('Prevalence (%)')
# plt.bar(labels, pc)
plt.tight_layout()
seaborn.despine()
plt.savefig("occurances.png")
# plt.show()
