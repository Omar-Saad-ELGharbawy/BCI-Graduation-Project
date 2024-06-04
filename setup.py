import random

tasks = ['Right Grasp', 'Right Release', 'Baseline']
repetitions = 20

# Generate a list with each name repeated 20 times
task_repeated = [task for task in tasks for _ in range(repetitions)]

# Shuffle the list to randomize the order
random.shuffle(task_repeated)

# Print the trial number and then one name at a time, waiting for spacebar press before printing the next one
for i, task in enumerate(task_repeated, 1):
    # user_input = input(f"Trial {i}: Press Enter to see the next Trial, or 'q' to quit: ")
    user_input = input("_"*30)
    if user_input == 'q':
        break
    elif user_input != '':
        print("Invalid input. Please press Enter or 'q' to quit.")
        continue
    print(f"Baseline (1 sec) Trial {i}: {task}.")
    print(f"Trial {i}: {task}.")
    sub_name = "sherif"
    session_num= 1
    run = i
    # pre_task = f"sub-{sub_name}_ses-{session_num}_task-{task}_run-{run}_eeg"
    # print(pre_task)
    # file_name = f"sub-{sub_name}_ses-{session_num}_task-{task}_run-{run}_eeg"
    # print(file_name)

# file_name = f" {}_{}  "
