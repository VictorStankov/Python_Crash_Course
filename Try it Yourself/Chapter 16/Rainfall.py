import csv
from matplotlib import pyplot as plt
from datetime import datetime

filename = 'sitka_weather_2014.csv'

# Get dates and high and low temperatures from file.
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, rainfall = [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            rain = row[-4]
        except ValueError:
            print(current_date, "missing data")
        else:
            dates.append(current_date)
            rainfall.append(rain)

# Plot data.
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, rainfall, c="blue", alpha=0.5)

# Format plot.
plt.title("Daily precipitation - 2014\nSitka, AL", fontsize=20)
plt.xlabel("", fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
