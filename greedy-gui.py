import re
from collections import defaultdict
import PySimpleGUI as sg

# Function to check if a battle has started based on predefined patterns
def has_battle_started(line):
    possible_starts = ["You intercepted the", "You have been intercepted by the"]
    return any(start in line for start in possible_starts)

# Function to check if a battle has ended based on a predefined pattern
def has_battle_ended(line):
    possible_end = "The victors plundered"
    return possible_end in line

# Function to extract the name of individual who made a greedy hit using regex pattern (if none, return nothing)
def get_individual_greedy_hit(line):
    # The regex pattern is looking for a timestamp (in square brackets), followed by
    # some text (the individual's name), followed by either "swings", "performs", "executes" or "delivers".
    pattern = r'\[\d{2}:\d{2}:\d{2}\]\s(.*?)\s(swing|perform|execute|deliver)s a'
    match = re.search(pattern, line)
    return match and match.group(1)

# Function to count greedy hits from battle logs
def pull_greedy_hits_from_battle_log(latest_battle):
    hits = defaultdict(int)
    total_hits = 0 
    
    # Iterate over each line in the battle log
    for line in latest_battle:
        # Try to extract the individual's name from the line
        name = get_individual_greedy_hit(line)
        # If a name was found, a greedy hit was made. Increment the hit count for that individual.
        if name:
            hits[name] += 1
            total_hits += 1
    return hits, total_hits


# Function to process the log file
def process_file(file_path):
    try:
        # Create an empty list to store the lines of the latest battle. It's reset every time a new battle starts.
        latest_battle = []
        # Flag variable to track whether a battle is currently being recorded. It's set to True when a battle starts and False when it ends.
        recording_battle = False
        with open(file_path, 'r') as file:
            # Iterate over each line in the file.
            for line in file:
                # If a battle is currently being recorded, add the line to the latest battle list.
                if recording_battle:
                    latest_battle.append(line.strip())
                # If the line indicates the start of a battle, reset the latest battle list and start recording.
                if has_battle_started(line):
                    latest_battle = []
                    recording_battle = True
                # If the line indicates the end of a battle, stop recording.
                elif has_battle_ended(line):
                    recording_battle = False

        # After all lines in the file have been processed, pull the greedy hits from the latest battle.
        greedy_results, total_hits = pull_greedy_hits_from_battle_log(latest_battle)
        return greedy_results, total_hits
    except Exception as e:
        # If any error occurs during file processing, show a popup with the error message.
        sg.popup('Error processing file: ', e)


# GUI layout definition
layout = [[sg.Text("Greedy Finder"), sg.Input(), sg.FileBrowse(key='-FILE-')],
          [sg.Button('Find Greedy Hits', key='Process File')],
          [sg.Multiline(size=(40,5), key='-OUTPUT-', expand_x=True, expand_y=True)],
          [sg.Button('Copy to Clipboard', key='Copy')]]

# Create GUI window
window = sg.Window('Greedy Finder', layout, resizable=True)

# Main event loop
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED: 
        break
    if event == 'Process File':
        if values['-FILE-'] != '':
            hits, total_hits = process_file(values['-FILE-'])  # Get hit results
            if hits:
                hits_string = 'Total Hits: ' + str(total_hits) + '!\n'
                hits_string += ', '.join([f'{name}: {hit}' for name, hit in hits.items()])
                window['-OUTPUT-'].update(hits_string)  # Update the text field with hit results
            else:
                window['-OUTPUT-'].update('No greedy hits found')
        else:
            sg.popup('No file selected')
    if event == 'Copy':
        sg.clipboard_set(values['-OUTPUT-'])

window.close()
