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

    def __init__(self, _age: int | None, _weight: int | float | None):
        """
        Initializes attributes for this class.

        Invariants:
            - Age must be typed in, else, age will be assumed as 18.
            - Age must be greater than zero and lesser than 122 years. The upper bound is specific, as the oldest living human in the world was 122 years old.
            - Weight must be typed in, else, weight will be assumed as 62 kgs.
            - Weight must be greater than zero and lesser than 635 kgs. The upper bound is specific, as the heaviest human in the world was recorded to be 635 kgs.

        Args:
            _age (int | None): The age of the user. This is a private attribute because it has been sensitively handled.
            _weight (int | float | None): The weight of the user. Also a private attribute for the same reason.

        Returns:
            None
        """
        # Age and weight invariants with try-except
        if _age is None:
            _age = 18
        try:
            _age = int(_age)
        except (ValueError, TypeError): # This is more specific than something like Exception
            _age = 18
        if _age <= 0 or _age > 122:
            _age = 18

        if _weight is None:
            _weight = 62.0
        try:
            _weight = float(_weight)
        except (ValueError, TypeError):
            _weight = 62.0
        if _weight <= 0 or _weight > 635:
            _weight = 62.0

        self._age = _age
        self._weight = _weight
        # Height is optional and will be set by subclasses or externally (in cm, of course)
        self._height = None

    def get_age(self):
        """
        Returns the age of the user.

        Args:
            None

        Returns:
            int: The age of the user.
        """
        return self._age

    def get_weight(self) -> int | float:
        """
        Returns the weight of the user.

        Args:
            None
    
        Returns:
            int | float: The weight of the user.
        """
        return self._weight

    def set_age(self, new_age: int) -> None:
        """
        Sets the age of the user with validation!

        Args:
            new_age (int): The new age of the user.

        Returns:
            None
        """
        try:
            new_age = int(new_age)
        except (ValueError, TypeError):
            new_age = 18
        if new_age <= 0 or new_age > 122:
            new_age = 18
        self._age = new_age

    def set_weight(self, new_weight: int | float):
        """
        Sets the weight of the user with validation!

        Args:
            new_weight (int | float): The new weight of the user.

        Returns:
            None
        """
        try:
            new_weight = float(new_weight)
        except (ValueError, TypeError):
            new_weight = 62.0
        if new_weight <= 0 or new_weight > 635:
            new_weight = 62.0
        self._weight = new_weight

    def get_height(self) -> int | float:
        """
        Returns the height of the user.

        Args:
            None

        Returns:
            int | float: The height of the user.
        """
        return self._height

    def set_height(self, new_height: int | float) -> None:
        """
        Sets the height of the user through try-except.

        Args:
            new_height (int | float): The new height of the user.

        Returns:
            None
        """
        try:
            self._height = float(new_height)
        except (ValueError, TypeError):
            self._height = None

    def __repr__(self) -> str:
        """
        This returns a detailed representation of the Human object for debugging.
        
        Args:
            None

        Returns:
            str: A string that looks like valid Python code to recreate the object
        """
        return f"Human(age={self._age}, weight={self._weight}, height={self._height})"
    
    def __str__(self) -> str:
        """
        Returns a user-friendly string representation.

        Args:
            None

        Returns:
            str: A formatted string showing user attributes.
        """
        if self._height:
            height_str = f"{self._height} cm"
        else:
            height_str = "Not set"

        return f"Age: {self._age} years | Weight: {self._weight} kg | Height: {height_str}"

class Male(Human):
    """
    This is the Male subclass. It inherits everything from Human, but with a gender-specific default height!
    """
    def __init__(self, age: int | None = None, weight: int | float | None = None, height: int | float | None = None):
        """
        Initializes a Male object.

        Args:
            age (int | None): Age in years (defaults to 18 if invalid).
            weight (int | float | None): Weight in kg (defaults to 62 if invalid).
            height (int | float | None): Height in cm (defaults to 171 if not provided).

        Returns:
            None
        """
        super().__init__(age, weight)
        if height is None:
            self._height = 171.0 # Average male height around the world
        else:
            try:
                self._height = float(height)
            except (ValueError, TypeError):
                self._height = 171.0

    def __repr__(self) -> str:
        """
        This returns a detailed representation of the Male object for debugging.

        Args:
            None

        Returns:
            str: A string that looks like valid Python code to recreate the object
        """
        return f"Male(age={self._age}, weight={self._weight}, height={self._height})"

class Female(Human):
    """
    This is the Female subclass. Just like the Male class, it inherits everything from Human, but with a gender-specific default height!
    """
    def __init__(self, age: int | None = None, weight: int | float | None = None, height: int | float | None = None):
        """
        Initializes a Female object.

        Args:
            age (int | None): Age in years (defaults to 18 if invalid).
            weight (int | float | None): Weight in kg (defaults to 62 if invalid).
            height (int | float | None): Height in cm (defaults to 159 if not provided).

        Returns:
            None
        """
        super().__init__(age, weight)
        if height is None:
            self._height = 159.0 # Average female height around the world
        else:
            try:
                self._height = float(height)
            except (ValueError, TypeError):
                self._height = 159.0

    def __repr__(self) -> str:
        """
        This returns a detailed representation of the Female object for debugging.

        Args:
            None

        Returns:
            str: A string that looks like valid Python code to recreate the object
        """
        return f"Female(age={self._age}, weight={self._weight}, height={self._height})"

def display_menu() -> str:
    """
    A beautiful main menu display & choice selector, made using the Rich library!
    
    Args:
        None

    Returns:
        str: It returns '1', '2', '3', '4', '5', or '6' based on the user's choice. Exits the program if invalid choice is detected!
    """
    console.print(Panel(
        "[bold green]1[/] --> [white]Create user profile[/]\n"
        "[bold green]2[/] --> [white]Get workout plans[/]\n"
        "[bold green]3[/] --> [white]Track progress via graph[/]\n"
        "[bold green]4[/] --> [white]Calculate your BMI![/]\n"
        "[bold green]5[/] --> [white]Get meal plans[/]\n"
        "[bold green]6[/] --> [white]Start workout[/]\n"
        "[bold green]7[/] --> [white]Exit[/]",
        title="[bold yellow]Main Menu[/]",
        border_style="bright_blue",
        box=box.ROUNDED,
        padding=(1, 3)
    ))

    # A clean prompt at the bottom
    choice = console.input(" [bold cyan]Enter your choice here! --> [/]")
    return choice

def create_user_profile() -> None:
    """
    This function creates a user profile by asking for gender, age, weight, and height. It uses the Rich library for a better user interface.

    Args:
        None

    Returns:
        None
    """
    # Retrieves the global variable to store user profile
    global current_user
    # User Profile Window for Gender
    console.print(Panel(
        "[bold blue]Enter your[/] [bold cyan]ge[/][bold white]nd[/][bold magenta]er[/][bold blue]![/]\n"
        "[bright_cyan]M[/] --> [white]Male[/]\n"
        "[bright_magenta]F[/] --> [white]Female[/]\n"
        "[white]For[/][bold white] Other[/],[white] leave blank![/]",
        title="[bold yellow]Create User Profile: Gender[/]",
        border_style="bright_blue",
        box=box.ROUNDED,
        padding=(1, 3)
    ))

    gender = console.input(" [bold cyan]Enter your gender here! --> [/]").strip().upper()

    time.sleep(1)
    console.print("\n")
    # User Profile Window for Age
    console.print(Panel(
        "[bold green]Enter your age in years![/]\n"
        "[white]Don't prefer sharing your AGE? No worries! Leave blank for default (18)[/]",
        title="[bold yellow]Create User Profile: Age[/]",
        border_style="bright_green",
        box=box.ROUNDED,
        padding=(1, 3)
    ))
    
    age_in = console.input(" [bold cyan]Enter your age here! --> [/]").strip()

    time.sleep(1)
    console.print("\n")
    # User Profile Window for Weight
    console.print(Panel(
        "[bold magenta]Enter your weight in kilograms![/]\n"
        "[white]Don't prefer sharing your WEIGHT? No worries! Leave blank for default (62 kg)[/]",
        title="[bold yellow]Create User Profile: Weight[/]",
        border_style="bright_magenta",
        box=box.ROUNDED,
        padding=(1, 3)
    ))

    weight_in = console.input(" [bold cyan]Enter your weight here! --> [/]").strip()

    time.sleep(1)
    console.print("\n")
    # User Profile Window for Height
    console.print(Panel(
        "[bold cyan]Enter your height in centimeters![/]\n"
        "[white]Don't prefer sharing your HEIGHT? No worries! Leave blank for gender default height![/]",
        title="[bold yellow]Create User Profile: Height[/]",
        border_style="bright_cyan",
        box=box.ROUNDED,
        padding=(1, 3)
    ))
    height_in = console.input(" [bold cyan]Enter your height here in cms! --> [/]").strip()

    # Try-except here for error handling!
    # Age
    age = None
    if age_in:
        try:
            age = int(age_in)
        except (ValueError, TypeError):
            age = None

    # Weight
    weight = None
    if weight_in:
        try:
            weight = float(weight_in)
        except (ValueError, TypeError):
            weight = None

    # Height
    height = None
    if height_in:
        try:
            height = float(height_in)
        except (ValueError, TypeError):
            height = None

    # Same error handling for gender
    if gender in ("M", "MALE"):
        user = Male(age, weight, height)
    elif gender in ("F", "FEMALE"):
        user = Female(age, weight, height)
    else:
        user = Human(age, weight)
        # We'll choose a 'neutral' default height if nothing's provided!
        if height is None:
            user.set_height(165.0)
        else:
            try:
                user.set_height(float(height))
            except (ValueError, TypeError):
                user.set_height(165.0)

    current_user = user
    time.sleep(2)
    console.print("\n")

    # Now we get the user's height for the summary, again, with error handling
    # Creating a temporary variable for height string
    temporary_height_str = current_user.get_height()
    if temporary_height_str is None:
        height_str = "Not set"
    else:
        height_str = f"{temporary_height_str} cm"

    # Success message with profile summary
    console.print(Panel(
        "[bold green]Guess what? Your profile has been successfully created! WOOHOO! Here's a summary:[/]\n"
        f"[bright_green] - Age: {current_user.get_age()}[/]\n"
        f"[bright_green] - Weight: {current_user.get_weight()} kg[/]\n"
        f"[bright_green] - Height: {height_str}[/]",
        title="[bold yellow]Success![/]",
        border_style="green1",
        box=box.ROUNDED,
        padding=(1, 3)
    ))

    # A wait before returning to main menu
    time.sleep(2)
    console.input("[bold cyan]Press Enter to return to the main menu...[/] ")
    time.sleep(1)
    console.print("\n")

def calculate_cardio_plan():
    print("Cardio and weight loss program")

    # User Inputs
    gender = input("Enter gender (male/female): ").lower()
    weight_kg = float(input("Enter weight (kg): "))
    height_cm = float(input("Enter height (cm): "))
    age = int(input("Enter age (years): "))
    weight_to_lose_kg = float(input("How many kg do you want to lose total? "))
    days_to_reach_goal = int(input("In how many days? "))

    # Strength training experience level
    print("\nStrength Training Experience Levels:")
    print("1. Beginner")
    print("2. Intermediate")
    print("3. Advanced")
    level_choice = input("Choose your level (1/2/3): ")

    if level_choice == "1":
        level = "beginner"
        muscle_gain_per_month = 0.75
    elif level_choice == "2":
        level = "intermediate"
        muscle_gain_per_month = 0.40
    else:
        level = "advanced"
        muscle_gain_per_month = 0.20

    # 1. Calculate Basal Metabolic Rate (BMR)
    if gender == 'male':
        bmr = (10 * weight_kg) + (6.25 * height_cm) - (5 * age) + 5
    else:
        bmr = (10 * weight_kg) + (6.25 * height_cm) - (5 * age) - 161

    # 2. Calculate Total Daily Energy Expenditure (TDEE) - Sedentary
    tdee = bmr * 1.2

    # 3. Calculate Total Calorie Deficit Needed
    total_deficit_needed = weight_to_lose_kg * 7700
    daily_deficit_target = total_deficit_needed / days_to_reach_goal

    # 4. Cardio Options (MET values)
    cardio_types = {
        "Walking (brisk)": 4.3,
        "Jogging": 7.0,
        "Running (10km/h)": 9.8,
        "Cycling (moderate)": 8.0,
        "Swimming Laps": 7.0
    }

    # 5. Estimate muscle gain (general, non-medical)
    muscle_gain_kg = muscle_gain_per_month * (days_to_reach_goal / 30)

    print(f"\n--- Results ---")
    print(f"Daily Maintenance (TDEE): {tdee:.0f} calories")
    print(f"Daily deficit needed: {daily_deficit_target:.0f} calories")

    print("\nDaily Cardio Required (if diet remains at maintenance):")
    for activity, met in cardio_types.items():
        calories_per_min = (met * 3.5 * weight_kg) / 200
        minutes_needed = daily_deficit_target / calories_per_min
        print(f"- {activity}: {minutes_needed:.0f} minutes per day")

    print(f"\nEstimated Muscle Gain from Strength Training ({level}): {muscle_gain_kg:.2f} kg")

if __name__ == "__main__":
    calculate_cardio_plan()


def calculate_bmr(use_profile: bool = True):
    weight = None
    height_cm = None
    age = 0

    if use_profile and current_user is not None:
        weight = current_user._weight
        height_cm = current_user.height
        age = current_user._age
        if height_cm is None:
            h_in = console.input("Profile has no height. Enter height in cm: ").strip()
            try:
                height_cm = float(h_in)
            except (ValueError, TypeError):
                console.print("[red]Invalid height. Aborting BMI calculation.[/red]")
                return
    else:
        w_in = console.input("Enter weight in kg: ").strip()
        h_in = console.input("Enter height in cm: ").strip()
        a_in = console.input("Enter age:").strip()
        try:
            weight = float(w_in)
            height_cm = float(h_in)
            age = float(a_in)
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
    mens_bmr = (10 * weight) + (6.25 * height_cm) - (5 * age) + 5
    female_bmr = (10 * weight) + (6.25 * height_cm) - (5 * age) - 161
   
    # Simple WHO categories
    if current_user == Male:
        console.print(f"Your daily calories your should intake is {mens_bmr}")
    else:
        console.print(f"Your daily calories your should intake is {female_bmr}")

def calculate_bmi(use_profile: bool = True) -> None:
    """
    This is the BMI calculator! If use_profile and a profile exists, it uses its weight/height (or ask for missing height).
    Otherwise, it prompts for weight and height. It also validates inputs, compute BMI, and print category.

    Args:
        use_profile (bool): Whether to use the current_user profile for weight/height.

    Returns:
        None
    """
    console.print("\n[blue]BMI Calculator[/blue]")

    # Get weight and height (cm)
    weight = None
    height_cm = None

    if use_profile and current_user is not None:
        weight = current_user._weight
        height_cm = current_user._height
        if height_cm is None:
            h_in = console.input("Oops! Profile has no height. Enter height in cm: ").strip()
            try:
                height_cm = float(h_in)
            except (ValueError, TypeError):
                console.print("[red] Invalid height! Aborting BMI calculation... :([/red]")
                return
    else:
        w_in = console.input("Enter weight in kg: ").strip()
        h_in = console.input("Enter height in cm: ").strip()
        try:
            weight = float(w_in)
            height_cm = float(h_in)
        except (ValueError, TypeError):
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
    # The welcome screen, only shown once at the start
    console.print(Panel(
        "[bold cyan]Welcome![/]\n\n"
        "This is a PhysEd workout app, made to [bold yellow]promote PhysEd[/] with useful features!\n\n"
        "Made by: Jacksen Daniels Daekin, Aidan Dwyer, Matteo Orlando, Japjot Singh Rajbans\n\n"
        "[bold green]Let's begin, shall we? :)[/]",
        title="[bold white]PhysEd Workout App[/]",
        border_style="bright_magenta",
        padding=(1, 2),
        highlight=True
    ))
    time.sleep(3)

    while True:
        choice = display_menu()

        if choice == "1":
            console.print("\n [bold green]You have chosen option 1... 'Create user profile'[/]\n")
            # Created a delay here before showing the create user profile UI for better UX
            # Similarly, added delays in other options, too!
            time.sleep(2)
            create_user_profile()
        elif choice == "2":
            console.print("\n [bold magenta]You have chosen option 2... 'Get workout plans'[/]\n")
            time.sleep(2)
        elif choice == "3":
            console.print("[blue]Track Progress[/blue] - Under Construction")
            # Imported the graphing function here
            from graph import plotting
        elif choice == "4":
            # use profile if available, otherwise prompt
            if current_user is not None:
                calculate_bmi(use_profile=True)
            else:
                # ask whether to use ad-hoc inputs
                use = console.input("No profile found. Calculate BMI by entering values? (y/n): ").lower()
                if use in ("n", "no", "nope"):
                    console.print("[red]Cancelled BMI calculation.[/red]")
                else:
                    calculate_bmi(use_profile=False)
        elif choice == "5":
            console.print("\n [bold blue]You have chosen option 5... 'Meal Plan and Nutrittion'[/]\n")
            time.sleep(2)
            calculate_bmr(use_profile=True)
        elif choice == "6":
            console.print("\n [bold blue]You have chosen option 6... 'Start Workout'[/]\n")
            time.sleep(2)
            from Unemissionize import plotting
            console.print("[blue]Workout Module[/blue] - Under Construction")
        elif choice == "7":
            console.print("[red]Exiting application...[/red]")
            break
        else:
            console.print("[red]Invalid choice, buddy! Try again.[/red]")
            time.sleep(2)

# Let's run this thing to life!
if __name__ == "__main__":
    main()
