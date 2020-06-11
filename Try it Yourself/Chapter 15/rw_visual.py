import pygal

from random_walk import RandomWalk

# Make a random walk and plot the points.
while True:
    rw = RandomWalk(5000)
    rw.fill_walk()
    hist = pygal.Bar()
    frequencies = []
    for value in range(0, 17):
        frequency = rw.steps.count(value)
        frequencies.append(frequency)

    hist.title = "Random Walk"
    hist.x_title = "Number of Steps"
    hist.x_labels = list(number for number in range(0, 17))
    hist.y_title = "Number of Times"
    hist.add("Pixels", frequencies)
    hist.render_to_file("dice_visual.svg")
    # Set the size of the plotting window.
    # plt.figure(figsize=(10, 6))

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break
