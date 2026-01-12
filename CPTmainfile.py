"""
authors: Japjot Singh Rajbans, Matteo Orlando, Aidan Dwyer, Jacksen Daniels Deakin
date finished: January 12, 2026
ICS4U CPT - PhysEd Workout App
"""

# Importing modules we'll use for the entirety of this program
import time
from datetime import datetime
from rich.panel import Panel
from rich.table import Table
from rich import box
from rich.console import Console
from stopwatch import stopwatch
from graph import plotting
console = Console()
current_user = None  # An empty variable to hold different credentials
workout_history = [] # A list to hold workout history records as dictionaries

class Human:
    """
    The start of it all: a human with common attributes, regardless of gender, age, or body measurements.
    The weight is measured in kilograms, not pounds, to align with the Canadian and the global weight standards.
    """

    def __init__(self, _age: int | None, _weight: int | float | None, gender: str | None = None):
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
        if gender is None:
            gender = "Not specified"
        if _weight is None:
            _weight = 62.0
        try:
            _weight = float(_weight)
        except (ValueError, TypeError):
            _weight = 62.0
        if _weight <= 0 or _weight > 635:
            _weight = 62.0
        self._gender = gender
        self._age = _age
        self._weight = _weight
        # Height is optional and will be set by subclasses or externally (in cm, of course)
        self._height = None

    def get_gender(self) -> str:
        """
        Returns the gender of the user.

        Args:
            None

        Returns:
            str: The gender of the user.
        """
        return self._gender

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

    def set_gender(self, new_gender: str) -> None:
        """
        Sets the gender of the user.

        Args:
            new_gender (str): The new gender of the user.

        Returns:
            None
        """
        self._gender = new_gender

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

    def get_height(self) -> int | float | None:
        """
        Returns the height of the user.

        Args:
            None

        Returns:
            int | float | None: The height of the user.
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
    def __init__(self, age: int | None = None, weight: int | float | None = None, height: int | float | None = None, gender: str | None = None):
        """
        Initializes a Male object.

        Args:
            age (int | None): Age in years (defaults to 18 if invalid).
            weight (int | float | None): Weight in kg (defaults to 62 if invalid).
            height (int | float | None): Height in cm (defaults to 171 if not provided).

        Returns:
            None
        """
        super().__init__(age, weight, gender)
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
    def __init__(self, age: int | None = None, weight: int | float | None = None, height: int | float | None = None, gender: str | None = None):
        """
        Initializes a Female object.

        Args:
            age (int | None): Age in years (defaults to 18 if invalid).
            weight (int | float | None): Weight in kg (defaults to 62 if invalid).
            height (int | float | None): Height in cm (defaults to 159 if not provided).

        Returns:
            None
        """
        super().__init__(age, weight, gender)
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
        "[bold bright_red]1[/] --> [white]Create user profile[/]\n"
        "[bold #ff991c]2[/] --> [white]Get workout plans[/]\n"
        "[bold bright_yellow]3[/] --> [white]Track progress via graph[/]\n"
        "[bold bright_green]4[/] --> [white]Calculate your BMI![/]\n"
        "[bold #305cde]5[/] --> [white]Get meal plans[/]\n"
        "[bold #6e00ff]6[/] --> [white]Start workout[/]\n"
        "[bold #8a00c4]7[/] --> [white]Open Stopwatch[/]\n"
        "[bold #666666]8[/] --> [white]Exit[/]",
        title="[bold dark_blue]Main Menu[/]",
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

    # Keep the raw input so we can store user's exact entry, but compare an uppercase copy
    gender_input = console.input(" [bold cyan]Enter your gender here! --> [/]").strip()
    gender = gender_input.upper()

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

    # Same error handling for gender and pass the user's gender into the constructed object
    if gender in ("M", "MALE"):
        user = Male(age, weight, height, gender="Male")
    elif gender in ("F", "FEMALE"):
        user = Female(age, weight, height, gender="Female")
    else:
        # If user provided some custom text (e.g., "Non-binary"), pass it through; otherwise let Human default "Not specified"
        user_gender_arg = gender_input if gender_input else None
        user = Human(age, weight, gender=user_gender_arg)
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
    height_value = current_user.get_height()
    if height_value is None:
        height_str = "Not set"
    else:
        height_str = f"{height_value} cm"

    # A success message with profile summary!
    console.print(Panel(
        "[bold green]Guess what? Your profile has been successfully created! WOOHOO! Here's a summary:[/]\n"
        f"[bright_green] - Gender: {current_user.get_gender()}[/]\n"
        f"[bright_green] - Age: {current_user.get_age()}[/]\n"
        f"[bright_green] - Weight: {current_user.get_weight()} kg[/]\n"
        f"[bright_green] - Height: {height_str}[/]",
        title="[bold green]Success![/]",
        border_style="#16e860",
        box=box.ROUNDED,
        padding=(1, 3)
    ))

    # A wait before returning to main menu
    time.sleep(2)
    console.input("[bold cyan]Press Enter to return...[/] ")
    time.sleep(1)
    console.print("\n")

def calculate_workout_plan() -> None:
    """
    Generates a personalized cardio, weight-loss, and strength-training plan.
    Uses the current user profile and displays results using the Rich UI.

    The function:
        - Calculates BMR and TDEE
        - Determines daily calorie deficit needed
        - Estimates required daily cardio time
        - Recommends a strength training plan based on experience level

    Args:
        None

    Returns:
        None
    """
    # Error message if no profile exists
    if current_user is None:
        console.print(Panel(
            "[red]Your profile does not exist! Please create a profile first to get a personalized workout plan.[/red]",
            title="[bold yellow]Error![/]",
            border_style="#fe3c30",
            box=box.ROUNDED,
            padding=(1, 3)
        ))
        console.input("Press Enter to return to the menu...")
        return

    # Retrieve profile data
    weight_kg = current_user.get_weight()
    height_cm = current_user.get_height()
    age = current_user.get_age()
    gender = (current_user.get_gender() or "").lower()

    # Ensure height exists
    if height_cm is None:
        h_in = console.input("Profile missing height. Enter height in cm: ").strip()
        try:
            height_cm = float(h_in)
            current_user.set_height(height_cm)
        except (ValueError, TypeError):
            console.print("[red]Whoops; invalid height! Returning back to main menu...[/red]")
            return

    # Goal input panel
    console.print(Panel(
        "[bold cyan]Set Your Weight-Loss Goal[/]\n"
        "Enter the information below to generate your plan.",
        title="[bold yellow]Workout Plan Setup[/]",
        border_style="bright_blue",
        box=box.ROUNDED,
        padding=(1, 3)
    ))

    try:
        weight_to_lose = float(console.input("Kg you want to lose: "))
        days_to_goal = int(console.input("Days to reach your goal: "))
    except (ValueError, TypeError):
        console.print("[red]Invalid input. Returning to menu.[/red]")
        return

    if weight_to_lose <= 0 or days_to_goal <= 0:
        console.print("[red]Values must be positive! Returning to menu...[/red]")
        return

    time.sleep(1)
    # Strength level selection
    console.print(Panel(
        "[bold cyan]1[/][white] --> Beginner[/]\n"
        "[bold cyan]2[/][white] --> Intermediate[/]\n"
        "[bold cyan]3[/][white] --> Advanced[/]\n"
        "Enter the choice below to generate your plan!",
        title="[bold yellow]Select Strength Training Level[/]",
        border_style="bright_blue",
        box=box.ROUNDED,
        padding=(1, 3)
    ))
    level_choice = console.input(" [bold cyan]Enter your choice here! --> [/]").strip()
    console.print("[bold #ff64ab]\n Just a second...")
    time.sleep(1.25)
    console.print("\n")

    # Decision structure for strength training plan
    if level_choice == "1":
        level = "Beginner"
        muscle_gain_rate = 0.75
        strength_plan = [
            "Full-body workout (3x per week)",
            "3 sets, 8-12 reps",
            "Rest 60-90 seconds"]
        
    elif level_choice == "2":
        level = "Intermediate"
        muscle_gain_rate = 0.40
        strength_plan = [
            "Upper / Lower split (4x per week)",
            "4 sets, 6-10 reps",
            "Rest 90-120 seconds"]
        
    else:
        level = "Advanced"
        muscle_gain_rate = 0.20
        strength_plan = [
            "Push / Pull / Legs split (5-6x per week)",
            "4-5 sets, 5-8 reps",
            "Rest 2-3 minutes"]

    # BMR calculation
    if gender.startswith("m"):
        bmr = (10 * weight_kg) + (6.25 * height_cm) - (5 * age) + 5
    else:
        bmr = (10 * weight_kg) + (6.25 * height_cm) - (5 * age) - 161

    # Energy calculations
    total_calorie_deficit = weight_to_lose * 7700
    daily_deficit = total_calorie_deficit / days_to_goal

    # Cardio MET values
    cardio_options = {
        "Walking (brisk)": 4.3,
        "Jogging": 7.0,
        "Running (10 km/h)": 9.8,
        "Cycling (moderate)": 8.0,
        "Swimming": 7.0}

    # Muscle gain estimate
    estimated_muscle_gain = muscle_gain_rate * (days_to_goal / 30)

    # Build cardio output
    cardio_output = ""
    for activity, met in cardio_options.items():
        calories_per_min = (met * 3.5 * weight_kg) / 200
        minutes_needed = daily_deficit / calories_per_min
        cardio_output += f"- {activity}: {minutes_needed:.0f} min/day\n"

    # Final output panel
    console.print(Panel(
        "[bold cyan]Recommended Daily Cardio (Choose One)[/]\n"
        f"{cardio_output}\n"
        f"[bold magenta]Estimated Muscle Gain ({level}):[/] {estimated_muscle_gain:.2f} kg\n\n"
        "[bold yellow]Strength Training Plan[/]\n" +
        "\n".join(f"- {line}" for line in strength_plan) +
        "\n\n[bold red]Note: [/][red]Make sure to consult your doctor before starting any new exercise program![/]",
        title="[bold green]Your Personalized Workout Plan![/]",
        border_style="green1",
        box=box.ROUNDED,
        padding=(1, 3)))
    time.sleep(3)
    
    # A wait before returning to main menu
    time.sleep(2)
    console.input("[bold cyan]Press Enter to return to the main menu...[/] ")
    time.sleep(1)
    console.print("\n")

def calculate_bmr(use_profile: bool = True) -> None:
    """
    This is the BMR calculator!
    If use_profile and a profile exists, it uses its weight/height/age (or ask for missing height).
    Otherwise, it prompts for weight, height, and age.
    It also validates inputs, compute BMR, and print target calories based on goal.

    Args:
        use_profile (bool): Whether to use the current_user profile for weight/height/age.

    Returns:
        None
    """
    # Initializing variables
    weight = None
    height = None
    age = 0

    # Get weight, height, age, gender
    if use_profile and current_user is not None:
        weight = current_user.get_weight()
        height = current_user.get_height()
        age = current_user.get_age()
        gender = current_user.get_gender()

    else:
        create_user_profile()
        if current_user is not None:
            weight = current_user.get_weight()
            height = current_user.get_height()
            age = current_user.get_age()
            gender = current_user.get_gender()
        else:
            console.print("[red]Failed to create user profile. Aborting.[/red]")
            return

    # Error handling
    if weight is None or height is None:
        console.print("[red]Missing data. Aborting.[/red]")
        return
    if weight <= 0:
        console.print("[red]Weight must be positive. Aborting.[/red]")
        return
    if height <= 0:
        console.print("[red]Height must be positive. Aborting.[/red]")
        return
    
    # BMR Calculation using Mifflin-St Jeor Equation
    if gender == "Male":
        bmr = (10 * weight) + (6.25 * height) - (5 * age) + 5
    else:
        bmr = (10 * weight) + (6.25 * height) - (5 * age) - 161
   
    console.print(Panel(
        f"[bold cyan]Your daily calories you should intake is {bmr}![/]\n\n"
        "What would you like to do next?\n"
        "[bold green]Lose[/] --> Lose weight!\n"
        "[bold yellow]Maintain[/] --> Maintain weight!\n"
        "[bold red]Gain[/] --> Gain weight!",
        title="[bold yellow]Calculate BMR: Daily Calories & Goal[/]",
        border_style="bright_blue",
        box=box.ROUNDED,
        padding=(1, 3)
    ))

    goal = console.input(" [bold cyan]Enter your choice here! --> [/]").strip().lower()
    time.sleep(1)

    if goal == "lose":
        target = bmr - 300
        console.print(f"[bold green]Target calories for weight loss: {target:.0f}[/]")
    elif goal == "gain":
        target = bmr + 300
        console.print(f"[bold red]Target calories for weight gain: {target:.0f}[/]")
    else:
        target = bmr
        console.print(f"[bold yellow]Target calories for maintenance: {target:.0f}[/]")

    # Meal plan recommendations based on target calories, and yes, this is a HUGE dictionary!
    meal_plans = {
        1200: [
            "Breakfast: Greek yogurt (170 g, nonfat), Blueberries (100 g), Almonds (15 g)",
            "Lunch: Grilled chicken breast (120 g), Quinoa (100 g cooked), Steamed broccoli (150 g), Olive oil (1 tsp)",
            "Dinner: Baked salmon (120 g), Sweet potato (200 g baked), Mixed vegetables (150 g), Olive oil (1 tsp)"
        ],
        1500: [
            "Breakfast: Greek yogurt (200 g, nonfat), Banana (1 medium), Almonds (20 g)",
            "Lunch: Grilled chicken breast (150 g), Brown rice (150 g cooked), Steamed broccoli (150 g), Olive oil (2 tsp)",
            "Dinner: Baked salmon (150 g), Sweet potato (250 g baked), Mixed vegetables (200 g), Olive oil (2 tsp)"
        ],
        1800: [
            "Breakfast: Greek yogurt (250 g, nonfat), Banana (1 large), Almonds (25 g) ,Honey (1 tbsp)",
            "Lunch: Grilled chicken breast (180 g), Brown rice (180 g cooked), Steamed broccoli (150 g), Olive oil (1 tbsp) ",
            "Dinner: Baked salmon (180 g), Sweet potato (300 g baked), Mixed vegetables (200 g), Olive oil (1 tbsp)"
        ],
        2000: [
            "Breakfast: Greek yogurt (300 g, nonfat), Banana (1 large), Almonds (30 g), Honey (1 tbsp)",
            "Lunch: Grilled chicken breast (200 g), Brown rice (200 g cooked), Steamed broccoli (150 g), Olive oil (1.5 tbsp)",
            "Dinner: Baked salmon (200 g), Sweet potato (350 g baked), Mixed vegetables (200 g), Olive oil (1.5 tbsp)"
        ],
        2200: [
            "Breakfast: Greek yogurt (350 g, nonfat), Banana (1 large), Almonds (35 g), Honey (1.5 tbsp)",
            "Lunch: Grilled chicken breast (230 g), Brown rice (230 g cooked), Steamed broccoli (150 g), Olive oil (2 tbsp)",
            "Dinner: Baked salmon (220 g), Sweet potato (400 g baked), Mixed vegetables (200 g), Olive oil (2 tbsp)"

        ],
        2500: [
            "Breakfast: Greek yogurt (400 g, nonfat), Banana (1 large), Almonds (45 g), Honey (2 tbsp)",
            "Lunch: Grilled chicken breast (260 g), Brown rice (260 g cooked), Steamed broccoli (150 g), Olive oil (2.5 tbsp)",
            "Dinner: Baked salmon (260 g), Sweet potato (450 g baked), Mixed vegetables (200 g), Olive oil (2.5 tbsp)"
        ]
    }

    # Find the closest meal plan to the target calories
    closest = min(meal_plans.keys(), key=lambda x: abs(x - target))

    # Prints the recommended meal plan in a table format
    table = Table(
        title=f"[bold green1]Recommended Meal Plan[/] [white]({closest} Calories)[/]",
        box=box.ROUNDED,
        border_style="bright_blue",
        show_lines=True
    )

    # Adding columns
    table.add_column("Meal", style="bold cyan", no_wrap=True)
    table.add_column("What to eat", style="white")

    # Adding rows
    for entry in meal_plans[closest]:
        meal_name, meal_text = entry.split(":", 1)
        table.add_row(meal_name.strip(), meal_text.strip())

    # Finally, displaying the table!
    console.print(Panel(table, title="[bold magenta]Your Meal Plan![/]", border_style="bright_magenta", box=box.ROUNDED, padding=(1, 2)))

    # A wait before returning to main menu
    time.sleep(2)
    console.input("[bold cyan]Press Enter to return to the main menu...[/] ")
    time.sleep(1)
    console.print("\n")

def calculate_bmi(use_profile: bool = True) -> None:
    """
    This is the BMI calculator! If use_profile and a profile exists, it uses its weight/height (or ask for missing height).
    Otherwise, it prompts for weight and height. It also validates inputs, compute BMI, and print category.

    Args:
        use_profile (bool): Whether to use the current_user profile for weight/height.

    Returns:
        None
    """
    # Get weight and height (cm)
    weight = None
    height_cm = None

    # Uses profile data if available
    if use_profile and current_user is not None:
        weight = current_user.get_weight()
        height_cm = current_user.get_height()
        if height_cm is None:
            h_in = console.input("Oops! Profile has no height. Enter height in cm: ").strip()
            try:
                height_cm = float(h_in)
            except (ValueError, TypeError):
                console.print("[red] Oops, Invalid height! Aborting BMI calculation... :([/red]")
                return
    else:
        # For Weight
        console.print(Panel(
            "[bold green]Enter your weight in kilograms![/]\n"
            "[white]Oh, and please make sure that weight is positive and a numeric (with decimals, if specific).[/]",
            title="[bold yellow]Calculate BMI: Weight[/]",
            border_style="bright_green",
            box=box.ROUNDED,
            padding=(1, 3)
        ))
        w_in = console.input(" [bold cyan]Enter your weight here! --> [/]").strip()

        # For Height
        console.print(Panel(
            "[bold green]Enter your height in centimeters![/]\n"
            "[white]Oh, and please make sure that height is positive and a numeric (with decimals, if specific).[/]",
            title="[bold yellow]Calculate BMI: Height[/]",
            border_style="bright_green",
            box=box.ROUNDED,
            padding=(1, 3)
        ))
        h_in = console.input(" [bold cyan]Enter your height here! --> [/]").strip()
        
        try:
            weight = float(w_in)
            height_cm = float(h_in)
        except (ValueError, TypeError):
            console.print("[red] Aw hell nah, that's invalid input! Aborting BMI calculation...[/red]")
            return

    # Basic validation
    if weight is None or height_cm is None:
        console.print("[red] Missing data. Aborting.[/red]")
        return
    if weight <= 0:
        console.print("[red] Weight must be positive. Aborting.[/red]")
        return
    if height_cm <= 0:
        console.print("[red] Height must be positive. Aborting.[/red]")
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

    console.print(Panel(
        "[bold green]Your BMI has been successfully calculated! WOOHOO! Here's a summary:[/]\n"
        f"[bright_green] - BMI: {bmi_rounded} kg/m²[/]\n"
        f"[bright_green] - Category: {category}[/]\n",
        title="[bold green]Success![/]",
        border_style="green1",
        box=box.ROUNDED,
        padding=(1, 3)
    ))

    # A wait before returning to main menu
    time.sleep(2)
    console.input("[bold cyan]Press Enter to return to the main menu...[/] ")
    time.sleep(1)
    console.print("\n")

def start_workout() -> None:
    """
    Starts a new workout session and records distance, duration, and date.
    This data is stored in the workout_history list for graphing later.

    Args:
        None

    Returns:
        None
    """
    console.print(Panel(
        "[bold cyan]Start Your Workout![/]\n"
        "Record your workout details below.\n"
        "Enter workout date (e.g., 'January 12, 2026') or leave blank for today!",
        title="[bold yellow]Workout Session[/]",
        border_style="bright_cyan",
        box=box.ROUNDED,
        padding=(1, 3)
    ))

    # Get workout date
    date_input = console.input(" [bold cyan]Write the date here! --> [/]").strip()
    if not date_input:
        # We'll use today's date!
        date_input = datetime.now().strftime("%B %d, %Y")
    time.sleep(1)
    console.print("\n")

    # Now we get distance traveled
    console.print(Panel(
        "[bold green]Enter your distance in kilometers![/]\n"
        "[white]Oh, and please make sure that distance is positive and a numeric (with decimals, if specific).[/]",
        title="[bold yellow]Start Workout: Distance[/]",
        border_style="bright_green",
        box=box.ROUNDED,
        padding=(1, 3)
    ))
    
    distance_input = console.input(" [bold cyan]Write the distance here! --> [/]").strip()
    time.sleep(1)
    try:
        distance = float(distance_input)
        if distance <= 0:
            console.print(Panel(
                "[red]Whoa, distance must be positive! Workout is NOT recorded.[/red]",
                title="[bold yellow]Error![/]",
                border_style="#fe3c30",
                box=box.ROUNDED,
                padding=(1, 3)
            ))
            time.sleep(2)
            return
    except (ValueError, TypeError):
        console.print(Panel(
            "[red]Hey, invalid distance! Workout is NOT recorded.[/red]",
            title="[bold yellow]Error![/]",
            border_style="#fe3c30",
            box=box.ROUNDED,
            padding=(1, 3)
        ))
        time.sleep(2)
        return

    # Same goes for durations!
    console.print(Panel(
        "[bold green]Enter your duration in minutes![/]\n"
        "[white]Oh, and please make sure that duration is positive and a numeric (with decimals, if specific).[/]",
        title="[bold yellow]Start Workout: Duration[/]",
        border_style="bright_green",
        box=box.ROUNDED,
        padding=(1, 3)
    ))

    duration_input = console.input(" [bold cyan]Write the duration here! --> [/]").strip()
    time.sleep(1)
    try:
        duration = float(duration_input)
        if duration <= 0:
            console.print(Panel(
                "[red]Whoa, duration must be positive! Workout is NOT recorded.[/red]",
                title="[bold yellow]Error![/]",
                border_style="#fe3c30",
                box=box.ROUNDED,
                padding=(1, 3)
            ))
            time.sleep(2)
            return
    except (ValueError, TypeError):
        console.print(Panel(
            "[red]Hey, invalid duration! Workout is NOT recorded.[/red]",
            title="[bold yellow]Error![/]",
            border_style="#fe3c30",
            box=box.ROUNDED,
            padding=(1, 3)
        ))
        time.sleep(2)
        return
    
    # Now we'll store this precious work data
    workout_data = {"date": date_input, "distance": distance, "duration": duration}
    workout_history.append(workout_data)

    # And a success message!
    console.print(Panel(
        "[bold green]Your workout has been successfully recorded! WOOHOO! Here's a summary:[/]\n"
        f"[bright_green] - Date: {date_input}[/]\n"
        f"[bright_green] - Distance: {distance} km[/]\n"
        f"[bright_green] - Duration: {duration} minutes\n\n[/]"
        f"[yellow]Total workouts recorded: [/][bold yellow]{len(workout_history)}[/]\n\n"
        "[bold green]Keep it up! :D[/]",
        title="[bold green]Success![/]",
        border_style="green1",
        box=box.ROUNDED,
        padding=(1, 3)
    ))

    time.sleep(2)
    console.input("[bold cyan]Press Enter to return to the main menu...[/] ")
    time.sleep(1)
    console.print("\n")

def track_progress() -> None:
    """
    This function displays workout progress using a graph.
    Also shows dates, distances, and durations over time with outlier detection.
    Uses the plotting function from graph.py to generate the graph.

    Args:
        None

    Returns:
        None
    """
    # We'll check if there's workout data to display in the first place
    if len(workout_history) == 0:
        console.print(Panel(
            "[red]You look lost, don't you? No workout data found![/]\n\n"
            "[white]Please record some workouts first using option 6 to see your progress graph![/]",
            title="[bold yellow]Data Not Found![/]",
            border_style="bright_yellow",
            box=box.ROUNDED,
            padding=(1, 3)
        ))
        time.sleep(2)
        console.input("[bold cyan]Press Enter to return to the main menu...[/] ")
        time.sleep(1)
        console.print("\n")
        return

    # We'll check if there's enough data for meaningful graphing
    if len(workout_history) < 2:
        console.print(Panel(
            "[yellow]You need at least 2 workouts to see a progress graph![/]\n\n"
            f"[white]Current workouts recorded: {len(workout_history)}[/]\n"
            "[white]You know what helps when you don't have enough workouts? Working out more! Keep working out and come back later![/]",
            title="[bold yellow]Not Enough Data.[/]",
            border_style="bright_yellow",
            box=box.ROUNDED,
            padding=(1, 3)
        ))
        time.sleep(2)
        console.input("[bold cyan]Press Enter to return to the main menu...[/] ")
        time.sleep(1)
        console.print("\n")
        return

    # Now we'll extract data for graphing
    dates = []
    distances = []
    durations = []

    # For each workout, we'll extract date, distance, and duration
    for workout in workout_history:
        dates.append(workout["date"])
        distances.append(workout["distance"])
        durations.append(workout["duration"])

    # In the meantime, why not display a loading message?
    console.print(Panel(
        "[bold cyan] Generating your progress graph...[/]\n"
        f"[green] Analyzing {len(workout_history)} workout sessions...[/]",
        title="[bold yellow]Track Progress[/]",
        border_style="bright_blue",
        box=box.ROUNDED,
        padding=(1, 3)
    ))
    time.sleep(1)

    # Let's call the star of this function now, the plotting function from graph.py!
    try:
        plotting(dates, distances, durations)
    except Exception as error:
        console.print(f"[red]Error generating graph: {error}[/red]")
        time.sleep(2)

    # After graph is closed
    console.print("\n[green]Graph closed successfully![/green]")
    time.sleep(1)
    console.input("[bold cyan]Press Enter to return to the main menu...[/] ")
    time.sleep(1)
    console.print("\n")

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
        title="[bold #7edfe8]PhysEd[/][bold #bfc4cc] Workout[/][bold #ffa8b0] App[/]",
        border_style="#ff64ab",
        padding=(1, 2),
        highlight=True
    ))
    time.sleep(3)

    while True:
        # Displaying the menu
        choice = display_menu()

        if choice == "1":
            # This is what the user should do first!
            console.print("\n [bold green]You have chosen option 1... 'Create user profile'[/]\n")
            time.sleep(2)
            create_user_profile()
        elif choice == "2":
            # Workout plans
            console.print("\n [bold magenta]You have chosen option 2... 'Get workout plans'[/]\n")
            time.sleep(1)
            calculate_workout_plan()
        elif choice == "3":
            # Track progress
            console.print("\n [bold blue]You have chosen option 3... 'Track Progress'[/]\n")
            time.sleep(2)
            track_progress()
        elif choice == "4":
            # BMI Calculator
            console.print("\n [bold blue]You have chosen option 4... 'Calculate your BMI!'[/]\n")
            time.sleep(2)
            if current_user is not None:
                calculate_bmi(use_profile=True)
            else:
                console.print(Panel(
                    "[white]Hey there! We're lost on this one. We couldn't find any profile. Would you like to calculate BMI by entering values?[/]\n"
                    "[#16e860]Y[/][white] --> Calculate BMI by entering values manually[/]\n"
                    "[#fe3c30]N[/][white] --> Cancel BMI calculation[/]",
                    title="[bold red]Error: Profile Not Found![/]",
                    border_style="#fe3c30",
                    box=box.ROUNDED,
                    padding=(1, 3)
                ))

                use = console.input(" [bold cyan]Enter your choice here! --> [/]").strip().lower()
                if use in ("y", "yes", "yeah", "yep"):
                    time.sleep(1)
                    calculate_bmi(use_profile=False)
                if use in ("n", "no", "nope"):
                    console.print("[#8a9248]Alright! Cancelled BMI calculation.[/]")
                    time.sleep(1)
                else:
                    console.print("[red] Whoops, invalid choice! Returning to main menu...[/red]")
                    time.sleep(1)
        elif choice == "5":
            console.print("\n [bold blue]You have chosen option 5... 'Meal Plan and Nutrition'[/]\n")
            time.sleep(2)
            calculate_bmr(use_profile=True)
        elif choice == "6":
            console.print("\n [bold blue]You have chosen option 6... 'Start Workout'[/]\n")
            time.sleep(2)
            start_workout()

        elif choice == "7":
            console.print("\n [bold blue]You have chosen option 7... 'Open Stopwatch'[/]\n")
            time.sleep(1)
            stopwatch()

        elif choice == "8":
            console.print("\n [bold blue]You have chosen option 8... 'Exit'[/]\n")
            time.sleep(2)
            console.print(Panel(
                "[bold dark_blue]Thank you for using the PhysEd Workout App! Stay active and healthy! :)[/]",
                title="[bold dark_blue]Goodbye![/]",
                border_style="bright_blue",
                box=box.ROUNDED,
                padding=(1, 3)
            ))
            break
        else:
            console.print(Panel(
                "[red]Hey, invalid choice! Try again...[/red]",
                title="[bold red]Error![/]",
                border_style="#fe3c30",
                box=box.ROUNDED,
                padding=(1, 3)
            ))
            time.sleep(2)

# Let's run this thing to life!
if __name__ == "__main__":
    main()
