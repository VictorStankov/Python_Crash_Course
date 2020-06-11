import matplotlib.pyplot as plt
from die import Die

# Create a D6
die_1 = Die()
die_2 = Die()

# Make some rolls and store resulst in a list.
die_1_results = []
die_2_results = []
for roll_num in range(1000):
    die_1_results.append(die_1.roll())
    die_2_results.append(die_2.roll())

plt.scatter(die_1_results, die_2_results, edgecolors='none', s=15)
plt.show()
