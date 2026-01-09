"""
authors: Japjot Singh Rajbans, Matteo Orlando, Aidan Dwyer, Jacksen Daniels Deakin
date finished: January 12, 2026
ICS4U CPT - PhysEd Workout App
"""

from rich.console import Console

console = Console()

current_user = None  # will hold the created user profile


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


def display_menu():
    console.print("\n[bold cyan]PhysEd Workout App[/bold cyan]")
    console.print("[yellow]Main Menu[/yellow]")
    console.print("1. Create User Profile")
    console.print("2. Get Workout Plans")
    console.print("3. Track Progress via Graph")
    console.print("4. Calculate BMI")
    console.print("5. Get Meal Plans")
    console.print("6. Exit")

    choice = console.input("\n[green]Select an option (1-6):[/green] ")
    return choice.strip()


def create_user_profile():
    global current_user
    console.print("\n[blue]Create User Profile[/blue]")
    gender = console.input("Gender ([green]M[/green]/[green]F[/green], leave blank for Other): ").strip().upper()

    age_in = console.input("Age in years [default 18]: ").strip()
    weight_in = console.input("Weight in kg [default 62]: ").strip()
    height_in = console.input("Height in cm (leave blank for gender default): ").strip()

    # parse with safe fallbacks
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


    

def calculate_bmr(use_profile: bool = True):
    weight = None
    height = None
    gender = None
    age = 0

    if use_profile and current_user is not None:
        weight = current_user.weight
        height = current_user.height
        age = current_user.age
        gender = current_user.gender
        
        create_user_profile()

    # Basic validation
    if weight is None or height is None or gender is None:
        console.print("[red]Missing data. Aborting.[/red]")
        return
    if weight <= 0:
        console.print("[red]Weight must be positive. Aborting.[/red]")
        return
    if height <= 0:
        console.print("[red]Height must be positive. Aborting.[/red]")
        return

    # Calculation
    if gender == "Male":
        bmr = (10 * weight) + (6.25 * height) - (5 * age) + 5
    else:
        bmr = (10 * weight) + (6.25 * height) - (5 * age) - 161
    

    # Simple WHO categories
    console.print(f"Your daily calories your should intake is {bmr}")

    goal = input("Is your goal to gain or lose weight (type gain or lose :")

    if bmr <= 1500 and goal == "lose":
        print ("test lsoer")
    elif bmr <= 1500 and goal == "gain":
        print ("test gain")
    else:
        print ("nonononono")


def main():
    while True:
        choice = display_menu()

        if choice == "1":
            create_user_profile()
        elif choice == "2":
            console.print("[blue]View Workout Plans[/blue] - Under Construction")
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
            calculate_bmr(use_profile=True)
        elif choice == "6":
            console.print("[red]Exiting application...[/red]")
            break
        else:
            console.print("[red]Invalid choice. Please try again.[/red]")


if __name__ == "__main__":
    main()