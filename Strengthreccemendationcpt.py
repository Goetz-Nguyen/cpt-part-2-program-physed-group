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