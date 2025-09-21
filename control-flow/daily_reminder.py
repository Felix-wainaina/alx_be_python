# daily_reminder.py
# Program to remind user about their priority task for the day

# Prompt for user input
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Process with match-case
match priority:
    case "high":
        reminder = f"'{task}' is a high priority task."
    case "medium":
        reminder = f"'{task}' is a medium priority task."
    case "low":
        reminder = f"'{task}' is a low priority task."
    case _:
        reminder = f"'{task}' has an unknown priority level."

# Add condition for time sensitivity
if time_bound == "yes":
    reminder += " That requires immediate attention today!"
else:
    reminder += " Consider completing it when you have free time."

# Print final reminder
print("\nReminder:", reminder)
