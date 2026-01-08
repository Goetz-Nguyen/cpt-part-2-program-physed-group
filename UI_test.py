import time
from rich.progress import Progress

def progress_bar(task1: str, task1time: float) -> str:
    """
    Creates a progress bar with custom names for custom times.
    This is a base program; 5 tasks max will be added soon.

    Args:
        task1 (str): Name of Task 1.
        task1time (int): Custom time to complete Task 1.

    Returns:
        str: The progress bar with a state-of-the-art user interface of any Python program.
    """
    
    with Progress() as progress:
        initialtask = "[red]" + task1
        print(initialtask)
        firsttask = progress.add_task(initialtask, total=task1time)

        while not progress.finished:
            progress.update(firsttask, advance=0.1)
            time.sleep(0.1)

progress_bar("Running", 101.0)