import csv
from datetime import datetime
from matplotlib import pyplot as plt

filename_0 = 'sitka_weather_2014.csv'
filename_1 = 'death_valley_2014.csv'

with open(filename_0) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates_0, highs_0, lows_0, dates_1, highs_1, lows_1 = [], [], [], [], [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_date, "missing data")
        else:
            dates_0.append(current_date)
            highs_0.append(high)
            lows_0.append(low)
    with open(filename_1) as q:
        reader = csv.reader(q)
        header_row = next(reader)
        for row in reader:
            try:
                current_date = datetime.strptime(row[0], "%Y-%m-%d")
                high = int(row[1])
                low = int(row[3])
            except ValueError:
                print(current_date, "missing data")
            else:
                dates_1.append(current_date)
                highs_1.append(high)
                lows_1.append(low)


# Plot data.
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates_0, highs_0, c='red', alpha=0.3)
plt.plot(dates_0, lows_0, c='blue', alpha=0.3)
plt.fill_between(dates_0, highs_0, lows_0, facecolor='blue', alpha=0.1)
plt.plot(dates_1, highs_1, c='purple', alpha=0.3)
plt.plot(dates_1, lows_1, c='green', alpha=0.3)
plt.fill_between(dates_1, highs_1, lows_1, facecolor='red', alpha=0.1)

# Format plot.
plt.title("Daily high and low temperatures - 2014\nDeath Valley, CA and Sitka, AL", fontsize=20)
plt.xlabel("", fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
