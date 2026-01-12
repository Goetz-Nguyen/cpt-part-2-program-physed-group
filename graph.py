"""
author: Japjot Singh Rajbans
date: January 12, 2026
graph.py
"""

# A fully working graphing program for workout distances and durations with outlier detection
import matplotlib.pyplot
import numpy

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

# Used `pass` here because this file is intended to be imported as a module
if __name__ == "__main__":
    pass
