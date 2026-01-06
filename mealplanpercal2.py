

def calculate_bmr(use_profile: bool = True):

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
    mens_bmr = (10 * weight) + (6.25 * height) - (5 * age) + 5

    female_bmr = (10 * weight) + (6.25 * height) - (5 * age) - 161
    

    # Simple WHO categories
    if user_profile Male:
        mens_bmr
        console.print(f"{mens_bmr}")
    else:
        female_bmr
        console.print(f"{female_bmr}")



    console.print(f"{mens_bmr}")

    console.print(f"[yellow]BMI:[/yellow] {bmi_rounded} kg/m² — [bold]{category}[/bold]")