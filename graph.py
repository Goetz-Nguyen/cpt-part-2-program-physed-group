# A fully working graphing program for workout distances and durations with outlier detection
import matplotlib.pyplot
import numpy

# We'll replace this part with actual data collection from user input in the main program
# This piece of code is just a placeholder
#for i in range(num_workouts):
#    date_val = input("Date: ")
#    dist_val = float(input("Distance: "))
#    dur_val = float(input("Duration: "))
#    
#    dates.append(date_val)
#    distances.append(dist_val)
#    durations.append(dur_val)

def plotting(dates: list[str], distances: list[int | float], durations: list[int | float]) -> None:
    """
    This function takes in lists of dates, distances, and durations, and plots them on two separate graphs.
    It also detects outliers based on standard deviation and marks them with a star shape.

    Args:
        dates (list[str]): A list of date strings.
        distances (list[int | float]): A list of distances corresponding to the dates.
        durations (list[int | float]): A list of durations corresponding to the dates.

    Returns:
        None
    """
    # Setting up the window to view the graph on
    matplotlib.pyplot.figure(figsize=(10, 8))

    # We'll calculate mean and deviation to check for outliers
    # This one is for distances
    dist_mean = numpy.mean(distances)
    dist_std = numpy.std(distances)
    
    # This one is for durations
    dur_mean = numpy.mean(durations)
    dur_std = numpy.std(durations)

    # For distance graph
    matplotlib.pyplot.subplot(2, 1, 1)
    # This connects the points with a dashed line 
    matplotlib.pyplot.plot(dates, distances, color='b', linestyle='--', alpha=0.3)
    
    # Now we'll iterate through data to apply the star shape for outliers
    for i in range(len(distances)):
        current_val = distances[i]
        # This checks if the point is an outlier
        if abs(current_val - dist_mean) > (1.5 * dist_std):
            matplotlib.pyplot.plot(dates[i], current_val, marker='*', color='gold', markersize=12)
        # If it's NOT an outlier, it'll plot normally
        else:
            matplotlib.pyplot.plot(dates[i], current_val, marker='o', color='b')

    matplotlib.pyplot.title('Workout Distances Over Time')
    matplotlib.pyplot.ylabel('Distance (km)')
    matplotlib.pyplot.grid(True)

    # This is for duration graph
    matplotlib.pyplot.subplot(2, 1, 2)
    # This connects the points with a dashed line 
    matplotlib.pyplot.plot(dates, durations, color='r', linestyle='--', alpha=0.3)

    # Now we'll iterate through data to apply the star shape for outliers
    for i in range(len(durations)):
        current_val = durations[i]
        # This checks if the point is an outlier
        if abs(current_val - dur_mean) > (1.5 * dur_std):
            matplotlib.pyplot.plot(dates[i], current_val, marker='*', color='orange', markersize=12)
        # If it's NOT an outlier, it'll plot normally
        else:
            matplotlib.pyplot.plot(dates[i], current_val, marker='o', color='r')

    matplotlib.pyplot.title('Workout Durations Over Time')
    matplotlib.pyplot.xlabel('Date')
    matplotlib.pyplot.ylabel('Duration (minutes)')
    matplotlib.pyplot.grid(True)

    matplotlib.pyplot.tight_layout()
    matplotlib.pyplot.show()

# TESTING...
# An example of dates, distances, and durations
dates = ['January 5, 2026', 'January 6, 2026', 'January 7, 2026', 'January 8, 2026', 'January 9, 2026', 'January 10, 2026']

# Distances and durations (I added an outlier here to test)
distances = [float(x) for x in [1, 3, 2, 4, 7, 12]]
durations = [float(x) for x in [30, 50, 40, 60, 20, 90]]

# And now we run the program!
plotting(dates, distances, durations)