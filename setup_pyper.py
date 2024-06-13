import random
import pyperclip
import keyboard
import time


def on_paste(trial):
    text = f"{trial-1}"
    time.sleep(0.5)
    pyperclip.copy(text.strip())


tasks = ["Right_Grasp", "Right_Release", "Baseline"]
repetitions = 45


# Generate a list with each name repeated 20 times
task_repeated = [task for task in tasks for _ in range(repetitions)]

# Shuffle the list to randomize the order
random.shuffle(task_repeated)

# Register the hotkey once
keyboard.add_hotkey("ctrl+v", lambda: on_paste(current_trial))

try:
    for i, task in enumerate(task_repeated, 1):
        current_trial = i  # Update the current trial number
        current_task = task  # Update the current trial number

        # user_input = input(f"Trial {i}: Press Enter to see the next Trial, or 'q' to quit: ")
        user_input = input("_" * 30)
        if user_input == "q":
            break
        elif user_input != "":
            print("Invalid input. Please press Enter or 'q' to quit.")
            continue
        # print(f"Baseline (1 sec) Trial {i}: {task}.")
        print(f"Trial {i}: {task}.")
        try:
            print(task.strip())
            pyperclip.copy(task.strip())
        except Exception as e:
            print(f"Error copying to clipboard: {e}")

        sub_name = "sherif"
        session_num = 1
        run = i
        # pre_task = f"sub-{sub_name}_ses-{session_num}_task-{task}_run-{run}_eeg"
        # print(pre_task)
        # file_name = f"sub-{sub_name}_ses-{session_num}_task-{task}_run-{run}_eeg"
        # print(file_name)
except KeyboardInterrupt:
    print("Process interrupted by user.")

# file_name = f" {}_{}  "
