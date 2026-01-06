"""
authors: Japjot Singh Rajbans, Matteo Orlando, Aidan Dwyer, Jacksen Daniels Deakin
date finished: January 12, 2026
ICS4U CPT - PhysEd Workout App
"""

# Importing modules we'll use for the entirety of this program
import time
from rich.panel import Panel
from rich import box
from rich.console import Console
console = Console()
current_user = None  # An empty variable to hold different credentials

class Human:
    """
    The start of it all: a human with common attributes, regardless of gender, age, or body measurements.
    The weight is measured in kilograms, not pounds, to align with the Canadian and the global weight standards.
    """
    def __init__(self, age: int | None, weight: int | float | None):
        """
        Initializes attributes for this class.

        Invariants:
            - Age must be typed in, else, age will be assumed as 18.
            - Age must be greater than zero and lesser than hundred.
            - Weight must be typed in, else, weight will be assumed as 62 kgs.
            - Weight must be greater than zero and lesser than 635 kgs. The upper bound is specific, as the heaviest human in the world was recorded to be 635 kgs.

        Args:
            age (int | None): The age of the user.
            weight (int | float | None): The weight of the user.

        Returns:
            None
        """
        if age is None:
            age = 18
        try:
            age = int(age)
        except Exception:
            age = 18
        if age <= 0 or age > 100:
            age = 18

        if weight is None:
            weight = 62.0
        try:
            weight = float(weight)
        except Exception:
            weight = 62.0
        if weight <= 0 or weight > 635:
            weight = 62.0

        self.age = age
        self.weight = weight
        # height is optional and may be set by subclasses or externally (in cm)
        self.height = None

    def get_age(self):
        return self.age

    def get_weight(self):
        return self.weight

    def set_age(self, new_age: int):
        self.age = new_age

    def set_weight(self, new_weight: int | float):
        self.weight = new_weight

    def get_height(self):
        return self.height

    def set_height(self, new_height: int | float):
        try:
            self.height = float(new_height)
        except Exception:
            self.height = None

    def __repr__(self) -> str:
        return f"Human(age={self.age}, weight={self.weight}, height={self.height})"

class Male(Human):
    def __init__(self, age: int | None = None, weight: int | float | None = None, height: int | float | None = None):
        super().__init__(age, weight)
        if height is None:
            self.height = 171.0
        else:
            try:
                self.height = float(height)
            except Exception:
                self.height = 171.0

class Female(Human):
    def __init__(self, age: int | None = None, weight: int | float | None = None, height: int | float | None = None):
        super().__init__(age, weight)
        if height is None:
            self.height = 159.0
        else:
            try:
                self.height = float(height)
            except Exception:
                self.height = 159.0

def display_menu() -> str:
    """
    A beautiful main menu display & choice selector, made using the Rich library!
    
    Args:
        None

    Returns:
        str: It returns '1', '2', '3', '4', '5', or '6' based on the user's choice. Exits the program if invalid choice is detected!
    """
    # The welcome screen!
    console.print(Panel(
        "[bold cyan]Welcome![/]\n\n"
        "This is a PhysEd workout app, made to [bold yellow]promote PhysEd[/] to explore maths (and also physics)!\n\n"
        "Made by: Jacksen Daniels Daekin, Aidan Dwyer, Matteo Orlando, Japjot Singh Rajbans"
        "[bold green]Let's begin, shall we? :)[/]",
        title="[bold white]PhysEd Workout App[/]",
        border_style="bright_magenta",
        padding=(1, 2),
        highlight=True
    ))

    # Main Menu
    console.print(Panel(
        "[bold green]1[/] --> [white]Create user profile[/]\n",
        "[bold green]2[/] --> [white]Get workout plans[/]\n"
        "[bold green]3[/] --> [white]Track progress via graph[/]\n"
        "[bold green]4[/] --> [white]Calculate your BMI![/]\n"
        "[bold green]5[/] --> [white]Get meal plans[/]\n"
        "[bold green]6[/] --> [white]Exit[/]\n",
        title="[bold yellow]Main Menu[/]",
        border_style="bright_blue",
        box=box.ROUNDED,
        padding=(1, 3)
    ))

    # A clean prompt at the bottom
    choice = console.print(" [bold cyan]Enter your choice here! [/]")
    return choice

def create_user_profile():
    global current_user
    console.print("\n[blue]Create User Profile[/blue]")
    gender = console.input("Gender ([green]M[/green]/[green]F[/green], leave blank for Other): ").strip().upper()

    age_in = console.input("Age in years [default 18]: ").strip()
    weight_in = console.input("Weight in kg [default 62]: ").strip()
    height_in = console.input("Height in cm (leave blank for gender default): ").strip()

    # Try-except here for error handling!
    try:
        age = int(age_in) if age_in else None
    except Exception:
        age = None
    try:
        weight = float(weight_in) if weight_in else None
    except Exception:
        weight = None
    try:
        height = float(height_in) if height_in else None
    except Exception:
        height = None

    # Same error handling for gender
    if gender == "M":
        user = Male(age, weight, height)
    elif gender == "F":
        user = Female(age, weight, height)
    else:
        user = Human(age, weight)
        # choose a neutral default height if none provided
        if height is None:
            user.height = 165.0
        else:
            try:
                user.height = float(height)
            except Exception:
                user.height = 165.0

    current_user = user
    console.print("[green]Profile created successfully.[/green]")
    console.print(f" - Age: {current_user.age}")
    console.print(f" - Weight: {current_user.weight} kg")
    console.print(f" - Height: {getattr(current_user, 'height', 'Not set')} cm")

def calculate_bmi(use_profile: bool = True):
    """
    Simple, clear BMI calculator:
    - If use_profile and a profile exists, use its weight/height (or ask for missing height).
    - Otherwise prompt for weight and height.
    - Validate inputs, compute BMI, and print category.
    """
    console.print("\n[blue]BMI Calculator[/blue]")

    # Get weight and height (cm)
    weight = None
    height_cm = None

    if use_profile and current_user is not None:
        weight = current_user.weight
        height_cm = current_user.height
        if height_cm is None:
            h_in = console.input("Profile has no height. Enter height in cm: ").strip()
            try:
                height_cm = float(h_in)
            except Exception:
                console.print("[red]Invalid height. Aborting BMI calculation.[/red]")
                return
    else:
        w_in = console.input("Enter weight in kg: ").strip()
        h_in = console.input("Enter height in cm: ").strip()
        try:
            weight = float(w_in)
            height_cm = float(h_in)
        except Exception:
            console.print("[red]Invalid input. Aborting BMI calculation.[/red]")
            return

    # Basic validation
    if weight is None or height_cm is None:
        console.print("[red]Missing data. Aborting.[/red]")
        return
    if weight <= 0:
        console.print("[red]Weight must be positive. Aborting.[/red]")
        return
    if height_cm <= 0:
        console.print("[red]Height must be positive. Aborting.[/red]")
        return

    # Calculation
    height_m = height_cm / 100.0
    bmi = weight / (height_m * height_m)
    bmi_rounded = round(bmi, 2)

    # Simple WHO categories
    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 25.0:
        category = "Normal weight"
    elif bmi < 30.0:
        category = "Overweight"
    else:
        category = "Obese"

    console.print(f"[yellow]BMI:[/yellow] {bmi_rounded} kg/m² — [bold]{category}[/bold]")

def main() -> None:
    """
    This is the main function, where the program roars to life!

    Args:
        None

    Returns:
        None
    """
    while True:
        choice = display_menu()

        if choice == "1":
            console.print("\n [bold green]You have chosen option 1... 'Create user profile'[/]\n")
            # Created a delay here before showing the create user profile UI for better UX
            time.sleep(2)
            create_user_profile()
        elif choice == "2":
            console.print("\n [bold magenta]You have chosen option 2... 'Get workout plans'[/]\n")
            # Created a delay here before showing next UI for better UX
            time.sleep(2)
            # Keep redirecting to different functions with different choices!
        elif choice == "3":
            console.print("[blue]Track Progress[/blue] - Under Construction")
        elif choice == "4":
            # use profile if available, otherwise prompt
            if current_user is not None:
                calculate_bmi(use_profile=True)
            else:
                # ask whether to use ad-hoc inputs
                use = console.input("No profile found. Calculate BMI by entering values? (y/n): ").strip().lower()
                if use == "n":
                    console.print("[red]Cancelled BMI calculation.[/red]")
                else:
                    calculate_bmi(use_profile=False)
        elif choice == "5":
            console.print("[blue]Get Nutrition Advice[/blue] - Under Construction")
        elif choice == "6":
            console.print("[red]Exiting application...[/red]")
            break
        else:
            console.print("[red]Invalid choice, buddy! Try again.[/red]")
            time.sleep(2)

if __name__ == "__main__":
    main()



