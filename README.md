# Welcome!
This repository contains the PhysEd Workout App, created by Jacksen Daniels Daekin, Aidan Dwyer, Matteo Orlando, and Japjot Singh Rajbans. The compiled date is January 12, 2026. Each of the functions and files has documentation of the highest standard, including a header containing our names, the date the project was completed, and the project title, as well as IPO (Input, Processing, Output) comments, docstrings, and single-line comments. Feel free to try & test them out! But before that...

# A few things to note...
1) Before playing around with this app, please install all of the given modules. Failure to install the modules will result in program not working at all!

- Time
- Datetime
- Panel
- Table
- box
- Console
- numpy
- Matplotlib.pyplot

2) To install these modules, write the following command into the Command Prompt of your computer...
- "python -m pip install rich": The panel, table, box and console modules are bundled into the Rich library!
- "python -m pip install -U matplotlib": You need to install the entire 'matplotlib' library for it.
- "pip install numpy": This is used to install the 'numpy' module.

# Main features
1) User Profile!
  Before using the program, take some time to create a personalized profile with...
  - Gender (Male, Female, or custom)
  - Age (validated between 1-122 years)
  - Weight (in kilograms, validated 0-635 kg)
  - Height (in centimeters)

2) Personalized Workout Plans!
  Get customized workout recommendations based on...

   - Your fitness goals (weight loss, maintenance, or gain)
   - Current body measurements
   - Desired weight loss targets
   - Timeline for achieving goals
   - Strength training experience level (Beginner, Intermediate, Advanced)

The app then calculates...
  - Daily cardio requirements across multiple activities (walking, jogging, running, cycling, swimming)
  - Strength training routines tailored to your level
  - Estimated muscle gain projections

3) BMI Calculator
  Calculate your Body Mass Index with automatic categorization:
  
   - Underweight (BMI < 18.5)
   - Normal weight (BMI 18.5-24.9)
   - Overweight (BMI 25-29.9)
   - Obese (BMI ≥ 30)
  
4) Meal Plans & Nutrition
  Receive science-based meal recommendations with...
  
   - BMR (Basal Metabolic Rate) calculation using the Mifflin-St Jeor equation
   - Customized meal plans ranging from 1200-2500 calories
   - Detailed breakfast, lunch, and dinner suggestions with portion sizes
   - Macro-balanced meals featuring Greek yogurt, lean proteins, whole grains, and vegetables

5) Workout Tracking
  Record your workout sessions with...
  
   - Date tracking
   - Distance traveled (in kilometers)
   - Duration (in minutes)
   - Automatic session history storage

6) Progress Visualization
  View your fitness journey through interactive graphs...
  
   - Distance trends over time
   - Duration trends over time
   - Outlier detection using statistical analysis (1.5 standard deviations)
   - Visual markers for exceptional workout sessions

7) Integrated Stopwatch
  Built-in stopwatch for timing...
  
   - Exercises
   - Rest periods
   - Workout segments
  
  Insanely useful for our program and for accurate fitness data!

# Code structure
  Object-Oriented Design
  The application uses inheritance with three classes...
  
   - Human (base class) - Common attributes for all users
   - Male (subclass) - Male-specific defaults (height: 171 cm)
   - Female (subclass) - Female-specific defaults (height: 159 cm)
  
  Data Validation
  All user inputs are validated with try-except blocks to ensure...
  
   - Numeric values are properly formatted
   - Ages are within realistic bounds (1-122 years)
   - Weights are within human limits (0-635 kg)
   - Heights and distances are positive values
  
  Visual Design
    The app uses the Rich library for...
    
   - Colorful, organized panels
   - Formatted tables for meal plans
   - Clear visual hierarchy
   - Enhanced user experience
  
# Key Calculations
  BMR (Basal Metabolic Rate)
   - Male: (10 × weight_kg) + (6.25 × height_cm) - (5 × age) + 5
   - Female: (10 × weight_kg) + (6.25 × height_cm) - (5 × age) - 161
  
  BMI (Body Mass Index)
   - BMI = weight_kg / (height_m²)
  
  Calorie Deficit for Weight Loss
   - Total deficit = weight_to_lose_kg × 7,700 calories
   - Daily deficit = total_deficit / days_to_goal
  
  Cardio Requirements
   - Calories per minute = (MET × 3.5 × weight_kg) / 200
   - Minutes needed = daily_deficit / calories_per_minute

# That's it!
Enjoy using the program, and get closer to your fitness goals! :)
