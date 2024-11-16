import csv
from datetime import datetime

# Function to format date strings
def format_date(date_str):
    try:
        return datetime.strptime(date_str, "%b. %d, %Y").strftime("%B %d, %Y")
    except ValueError:
        return date_str

# Read the CSV file
with open('plan.csv', 'r') as file:
    reader = csv.DictReader(file)

    # Initialize a dictionary to store weeks and their activities
    training_plan = []

    # Loop through each row in the CSV and organize data by weeks
    current_week_data = None
    current_week_number = None

    for row in reader:
        week = row['Week'].strip()
        date = row['Date'].strip()
        day = row['Day'].strip()
        training_phase = row['Training Phase'].strip()
        workout_type = row['Workout Type'].strip()
        miles = row['Miles'].strip()
        duration = row['Duration'].strip()
        pace = row['Pace'].strip()
        hr_zone = row['HR Zone'].strip()
        notes = row['Notes'].strip()
        total_mileage = row['Total Mileage'].strip()

        # If we encounter a new week, start a new week entry
        if week and week != current_week_number:
            if current_week_data:
                training_plan.append(current_week_data)
            current_week_number = week
            current_week_data = {
                "week": f"Week {week}",
                "dateRange": [],
                "activities": []
            }

        # Collect the date for the week
        if date:
            formatted_date = format_date(date)
            current_week_data["dateRange"].append(formatted_date)

        # Build the activity dictionary
        activity = {
            "day": day,
            "date": formatted_date if date else "",
            "trainingPhase": training_phase,
            "workoutType": workout_type,
            "miles": miles,
            "duration": duration,
            "pace": pace,
            "hrZone": hr_zone,
            "notes": notes,
            "totalMileage": total_mileage
        }

        # Add the activity to the current week's activities
        current_week_data["activities"].append(activity)

    # Append the last week's data
    if current_week_data:
        training_plan.append(current_week_data)

# Convert the training plan to a JavaScript object format
import json
training_plan_js = f"const trainingPlan = {json.dumps(training_plan, indent=4)};"

# Save the output to a JavaScript file
with open('training_plan.js', 'w') as file:
    file.write(training_plan_js)

print("JavaScript file created successfully!")
