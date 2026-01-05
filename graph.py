# This is a graphing system to plot workout data
# Based on different durations & distances, users can see varying graphs
# STATUS: 60% complete; dynamic graphs not yet implemented

# TODO: Modify it such that it adapts based on how many workouts the user has done (use iterations & lists)
# TODO: Also, add outliers using stars or different shapes
import matplotlib.pyplot as plt
def plotting(dates: list[str], distances: list[int | float], durations: list[int | float]) -> None: # Partly sourced from https://www.analyticsvidhya.com/blog/2020/10/headstart-to-plotting-graphs-using-matplotlib-library/
    """
    This function plots two graphs, one for distances and another for durations over given dates.
    It will dynamically adjust based on user input for workouts using iterations and lists.

    Args:
        dates (list): List of dates for the x-axis.
        distances (list): List of distances for the first graph.
        durations (list): List of durations for the second graph.

    Returns:    
        None: It just shows the graphs.
    """
    plt.figure(figsize=(10, 5))

    # Graph #1: Plot distances
    plt.subplot(2, 1, 1)
    plt.plot(dates, distances, marker='o', color='b')
    plt.title('Workout Distances Over Time')
    plt.xlabel('Date')
    plt.ylabel('Distance (km)')
    plt.grid(True)

    # Graph #2: Plot durations
    plt.subplot(2, 1, 2)
    plt.plot(dates, durations, marker='o', color='r')
    plt.title('Workout Durations Over Time')
    plt.xlabel('Date')
    plt.ylabel('Duration (minutes)')
    plt.grid(True)

    plt.tight_layout()
    plt.show()

# TODO: Using iterations & lists, update the dates (including years & months) accordingly
dates = ['January 5, 2026', 'January 6, 2026', 'January 7, 2026', 'January 8, 2026' , 'January 9, 2026']

# Distances and durations
distances = [1, 3, 2, 4, 7]
durations = [30, 50, 40, 90, 20]
plotting(dates, distances, durations)