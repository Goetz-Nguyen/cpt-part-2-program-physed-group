"""
author: Japjot Singh Rajbans
date: January 12, 2026
stopwatch.py
"""

# Importing modules that are necessary
import time
from rich.console import Console
from rich.live import Live
from rich.table import Table
from rich.panel import Panel

def stopwatch() -> None:
    """
    This is a terminal-based stopwatch that displays elapsed time in real-time using Rich library.
    It runs until it is interrupted by the user, i.e., Ctrl+C. 
    At the end, it shows the total elapsed time in a formatted UI!

    Args:
        None

    Returns:
        None
    """
    console = Console() # We need this inside the function to avoid import issues!
    start_time = time.perf_counter() # Start!

    # And the time ticks...
    with Live(console=console, screen=True, auto_refresh=False) as live:
        # Try-except to handle exits
        try:
            while True:
                elapsed = time.perf_counter() - start_time
                
                # Time calculations
                mins, secs = divmod(elapsed, 60)
                hours, mins = divmod(mins, 60)
                time_str = f"{int(hours):02d}:{int(mins):02d}:{secs:05.2f}"

                # A table for the stopwatch display
                table = Table(show_header=True, header_style="bold magenta", expand=True)
                table.add_column("Metric", style="dim")
                table.add_column("Value", justify="right")
                table.add_row("Elapsed Time", f"[bold cyan]{time_str}[/bold cyan]")
                table.add_row("System Clock", f"{elapsed:.4f}s")

                # Let's create a Panel and put the stopwatch inside it!
                live.update(
                    Panel(
                        table, 
                        title="[bold green]Active Stopwatch[/bold green]", 
                        border_style="bright_blue",
                        subtitle="Press Ctrl+C to Stop"
                    ), 
                    refresh=True
                )
                time.sleep(0.05)
                
        # If the user interrupts...
        except KeyboardInterrupt:
            # We'll capture the exact end time immediately
            end_time = time.perf_counter() - start_time
            
            # Formatting final time for the closing message
            f_mins, f_secs = divmod(end_time, 60)
            f_hours, f_mins = divmod(f_mins, 60)
            final_str = f"{int(f_hours):02d}:{int(f_mins):02d}:{f_secs:05.2f}"
            
            # STOP!
            live.stop()
            time.sleep(1)

            # Finally, let's display, and we're done!
            console.print("\n")
            console.print(Panel(
                f"Total Duration: [bold yellow]{final_str}[/bold yellow]\nRaw Seconds: [dim]{end_time:.6f}[/dim]",
                title="[bold red]Stopwatch Stopped[/bold red]",
                border_style="yellow",
                expand=False
            ))
            time.sleep(1)

if __name__ == "__main__":
    stopwatch()
