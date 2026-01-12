"""
author: Japjot Singh Rajbans
date: January 12, 2026
stopwatch.py
"""

# Importing modules that are necessary
import time
from rich.console import Console

console = Console()

def stopwatch():
    """
    Opens a simple stopwatch that starts when the user presses Enter and stops when pressed again.
    """
    console.print("[bold green]Stopwatch started. Press Enter to stop.[/]")
    start = time.perf_counter()
    input()
    end = time.perf_counter()
    console.print(f"[bold cyan]Elapsed time: {end - start:.2f} seconds[/]")
    console.input("Press Enter to return...")
