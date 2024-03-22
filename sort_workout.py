import tkinter as tk
from tkinter import ttk
import random

# WorkoutMove class definition
class WorkoutMove:
    def __init__(self, name_string, display_name_list, info_list):
        self.key_name = name_string
        self.display_name_list = display_name_list
        self.info_list = info_list

# Example workout moves
workout_moves = [
    WorkoutMove("single rock-and-box", ["L. rock-and-box", "R. rock-and-box"], ["Abs", "Mirrored", "Cardio", "Light"]),
    WorkoutMove("push-ups", ["Push-Ups"], ["Triceps", "Chest", "Ground", "Heavy"]),
    WorkoutMove("bicep curls", ["Bicep Curls"], ["Biceps", "Light"]),
    WorkoutMove("squats", ["Squats"], ["Quads", "Glutes", "Heavy"]),
    WorkoutMove("lunges", ["Lunges"], ["Quads", "Glutes", "Hamstrings"]),
    WorkoutMove("deadlifts", ["Deadlifts"], ["Back", "Glutes", "Hamstrings", "Heavy"]),
    WorkoutMove("leg press", ["Leg Press"], ["Quads", "Glutes", "Heavy"]),
    WorkoutMove("calf raises", ["Calf Raises"], ["Calves", "Light"]),
    WorkoutMove("bench press", ["Bench Press"], ["Chest", "Triceps", "Heavy"]),
    WorkoutMove("overhead press", ["Overhead Press"], ["Shoulders", "Triceps", "Heavy"]),
    WorkoutMove("tricep dips", ["Tricep Dips"], ["Triceps", "Chest", "Light"]),
    WorkoutMove("pull-ups", ["Pull-Ups"], ["Back", "Biceps", "Heavy"]),
    WorkoutMove("chin-ups", ["Chin-Ups"], ["Back", "Biceps", "Heavy"]),
    WorkoutMove("barbell rows", ["Barbell Rows"], ["Back", "Biceps", "Heavy"]),
    WorkoutMove("lat pull-downs", ["Lat Pull-Downs"], ["Back", "Light"]),
    WorkoutMove("seated rows", ["Seated Rows"], ["Back", "Light"]),
    WorkoutMove("overhead Tricep Ext.", ["Overhead Tricep Ext."], ["Triceps", "Back", "Light"]),
    WorkoutMove("shoulder flys", ["Shoulder Flys"], ["Shoulders", "Light"]),
    WorkoutMove("leg curls", ["Leg Curls"], ["Hamstrings", "Light"]),
    WorkoutMove("leg extensions", ["Leg Extensions"], ["Quads", "Light"]),
    WorkoutMove("plank", ["Plank"], ["Abs", "Core", "Ground"]),
    WorkoutMove("rev. plank", ["Rev.Plank"], ["Abs", "Core", "Ground"]),
    WorkoutMove("starfish crunch", ["Starfish Crunch"], ["Abs", "Core", "Ground"]),
    WorkoutMove("crab leg raise", ["L.Crab Leg Raise", "R.Crab Leg Raise"], ["Abs", "Core", "Ground"]),
    WorkoutMove("crunches", ["Crunches"], ["Abs", "Ground"]),
    WorkoutMove("mountain climbers", ["Mountain Climbers"], ["Abs", "Cardio", "Ground"]),
    WorkoutMove("burpees", ["Burpees"], ["Full body", "Cardio", "Ground", "Heavy"]),
    # Add more WorkoutMove objects here
]

# Function to filter and get the workout
def get_workout():
    included_muscles = [muscle for muscle, var in muscle_vars.items() if var.get()]
    excluded_muscles = [muscle for muscle, var in muscle_vars_exclude.items() if var.get()]
    included_traits = [trait for trait, var in trait_vars.items() if var.get()]
    excluded_traits = [trait for trait, var in trait_vars_exclude.items() if var.get()]
    
    # Filter moves based on inclusion/exclusion criteria
    filtered_moves = [
        move for move in workout_moves
        if all(muscle in move.info_list for muscle in included_muscles)
        and not any(muscle in move.info_list for muscle in excluded_muscles)
        and all(trait in move.info_list for trait in included_traits)
        and not any(trait in move.info_list for trait in excluded_traits)
    ]
    
    # Randomly select up to 3 moves
    selected_moves = random.sample(filtered_moves, min(3, len(filtered_moves)))
    
    # Update the combo box area with the selected moves
    combo_box_area.delete(0, tk.END)
    for move in selected_moves:
        for display_name in move.display_name_list:
            combo_box_area.insert(tk.END, display_name)

# Create the main window
root = tk.Tk()
root.title("Workout Generator")

# Define muscle groups and traits
muscle_groups = ["Traps", "Abs", "Triceps", "Forearms"]
traits = ["Mirrored", "Cardio", "Light", "Heavy", "Ground", "Adv"]

# Create dictionaries to hold the checkbox variables
muscle_vars = {muscle: tk.BooleanVar() for muscle in muscle_groups}
muscle_vars_exclude = {muscle: tk.BooleanVar() for muscle in muscle_groups}
trait_vars = {trait: tk.BooleanVar() for trait in traits}
trait_vars_exclude = {trait: tk.BooleanVar() for trait in traits}

label1 = tk.Label(root, text="Include")
label1.config(font=("times", 12), fg="#F9C22E", bg="#27133A", bd=2, relief="solid", padx=5, pady=5) 
label1.grid(row=0, column=0, padx=2, pady=5)
label2 = tk.Label(root, text="Exlude")
label2.config(font=("times", 12), fg="#F9C22E", bg="#27133A", bd=2, relief="solid", padx=5, pady=5) 
label2.grid(row=0, column=1, padx=2, pady=5)
label3 = tk.Label(root, text="Include")
label3.config(font=("times", 12), fg="#ff3", bg="#224", bd=2, relief="solid", padx=5, pady=5) 
label3.grid(row=0, column=2, padx=2, pady=5)
label4 = tk.Label(root, text="Exlude")
label4.config(font=("times", 12), fg="#ff3", bg="#224", bd=2, relief="solid", padx=5, pady=5) 
label4.grid(row=0, column=3, padx=2, pady=5)

# Create checkboxes for inclusion and exclusion
for i, muscle in enumerate(muscle_groups):
    tk.Checkbutton(root, text=muscle, variable=muscle_vars[muscle]).grid(row=i+1, column=0, sticky='w')
    tk.Checkbutton(root, text=muscle, variable=muscle_vars_exclude[muscle]).grid(row=i+1, column=1, sticky='w')
for i, trait in enumerate(traits):
    tk.Checkbutton(root, text=trait, variable=trait_vars[trait]).grid(row=i+1, column=2, sticky='w')
    tk.Checkbutton(root, text=trait, variable=trait_vars_exclude[trait]).grid(row=i+1, column=3, sticky='w')

# Create button to get workout
get_workout_button = tk.Button(root, text="Get Workout", command=get_workout)
get_workout_button.grid(row=len(traits)+1, column=0, columnspan=4)

# Create combo box area to display workouts
combo_box_area = tk.Listbox(root, height=10, width=50)
combo_box_area.grid(row=len(traits)+2, column=0, columnspan=4, pady=10)

# Start the Tkinter event loop
root.mainloop()
