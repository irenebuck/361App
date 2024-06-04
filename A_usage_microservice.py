# This is Microservice A - Usage Tracker
# It logs the date the game is played into the usage.txt file and provides a count of the 
# number of times the player has played the game.

import datetime


def log():
    """Logs the date in MM/DD/YY format to the end of the usage.txt file"""
    now = datetime.datetime.now()
    day = now.strftime("%x")
    with open("usage.txt", "a") as file:
        file.write(day + '\n')


def count_usage():
    """Counts the number of unique log entries and prints them to the console."""
    with open("usage.txt", "r") as file:
        line_count = len(file.readlines())
    if line_count is None:
        line_count = 0
    return line_count


def delete_last_entry():
    """Updates the date of the last entry to whatever the user wants"""
    with open('usage.txt', 'r') as usage_file:
        lines = usage_file.readlines()
    lines[-1] = ''
    with open('usage.txt', 'w') as usage_file:
        usage_file.writelines(lines)


while True:
    with open('pipe.txt', 'r') as infile:
        message = infile.readline()
    if message == 'get count':
        count_display = str(count_usage())
        with open('pipe.txt', 'w') as outfile:
            outfile.write(f'This program has been ran {count_display} times.')
    elif message == 'log':
        log()
        with open("pipe.txt", "w") as file:
            pass
    elif message == 'delete last':
        delete_last_entry()
        with open("pipe.txt", "w") as file:
            pass
    else:
        continue
