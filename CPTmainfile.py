"""
authors: Japjot Singh Rajbans, Matteo Orlando, Aidan Dwyer, Jacksen Daniels Daekin
date finished: --
ICS4U CPT - PhysEd Workout App
"""

# First off, we'll import modules that will certainly be used throughout the program
from rich.console import Console

console = Console() # This is a Console class constructor (belongs to `rich` library); acts as a high-level interface

class Human:
    """
    The start of it all: a human with common attributes, regardless of gender, age, or body measurements.
    The weight is measured in kilograms, not pounds, to align with the Canadian and the global weight standards.
    """
    def __init__(self, age: int, weight: int | float):
        """
        Initializes attributes for this class.

        Invariants:
            - Age must be typed in, else, age will be assumed as 18.
            - Age must be greater than zero and lesser than hundred.
            - Weight must be typed in, else, weight will be assumed as 62 kgs.
            - Weight must be greater than zero and lesser than 635 kgs. The upper bound is specific, as the heaviest human in the world was recorded to be 635 kgs.

        Args:
            age (int): The age of the user.
            weight (int): The weight of the user.

        Returns:
            None
        """
        # Implementations with invariants
        if not age:
            self.age = 18

        if age < 0 and age > 100:
            return False

        if not weight:
            self.weight = 62 # This is the average human weight globally (Source: https://www.livescience.com/36470-human-population-weight.html)

        if weight < 0 and weight > 635:
            return False 

        self.age = age
        self.weight = weight

    def get_age(self):
        """Returns the user's age."""
        return self.age

    def get_weight(self):
        """Returns the user's weight."""
        return self.weight

    def set_age(self, new_age: int):
        """
        Sets a new age for the user.

        Args:
            new_age: The new age of the user.

        Returns:
            None
        """
        self.age = new_age

    def set_weight(self, new_weight: int | float):
        """
        Sets a new weight for the user.

        Args:
            new_weight: The new weight of the user.

        Returns:
            None
        """
        self.weight = new_weight

    def __repr__(self) -> str:
        """Returns a developer-friendly string representation."""
        return f"Character(age='{self.age}', weight={self.weight})"

class Male(Human):
    def __init__(self, age: int, weight: int | float, height: int | float):
        super().__init__(age, weight)
        
        if not height:
            self.height = 171 # This is the average male height globally (Source: https://ourworldindata.org/human-height#:~:text=Here%2C%20we%20examine%20variations%20in,every%20country%20in%20the%20world.)
        else:
            self.height = height

class Female(Human):
    def __init__(self, age: int, weight: int | float, height: int | float):
        super().__init__(age, weight)
        
        if not height:
            self.height = 159 # This is the average female height globally (Source: https://ourworldindata.org/human-height#:~:text=Here%2C%20we%20examine%20variations%20in,every%20country%20in%20the%20world.)
        else:
            self.height = height


def display_menu():
    """Displays the main menu and returns the user's choice."""
    console.print("\n[bold cyan]PhysEd Workout App[/bold cyan]")
    console.print("[yellow]Main Menu[/yellow]")
    console.print("1. Create User Profile")
    console.print("2. View Workout Plans")
    console.print("3. Track Progress")
    console.print("4. Calculate BMI")
    console.print("5. Get Nutrition Advice")
    console.print("6. Exit")
    
    choice = console.input("\n[green]Select an option (1-6):[/green] ")
    return choice


def main():
    """Main function to run the application."""
    while True:
        choice = display_menu()
        
        if choice == "1":
            console.print("[blue]Create User Profile[/blue] - Under Construction")
        elif choice == "2":
            console.print("[blue]View Workout Plans[/blue] - Under Construction")
        elif choice == "3":
            console.print("[blue]Track Progress[/blue] - Under Construction")
        elif choice == "4":
            console.print("[blue]Calculate BMI[/blue] - Under Construction")
        elif choice == "5":
            console.print("[blue]Get Nutrition Advice[/blue] - Under Construction")
        elif choice == "6":
            console.print("[red]Exiting application...[/red]")
            break
        else:
            console.print("[red]Invalid choice. Please try again.[/red]")


if __name__ == "__main__":
    main()