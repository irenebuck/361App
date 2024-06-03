# This is Microservice A - Usage Tracker
# It logs the date the game is played into the usage.txt file and provides a count of the 
# number of times the player has played the game. 


import datetime
import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:8080")


def log():
    """Logs the date in MM/DD/YY format to the end of the usage.txt file"""
    now = datetime.datetime.now()
    day = now.strftime("%x")
    with open("usage.txt", "a") as file:
        file.write(day + '\n')


def count_usage():
    """Counts the number of unique log entries and prints them to the console."""
    with open("usage.txt", "r") as file:
        line_count = len(set(file.readlines()))
    return line_count


while True:
    message = socket.recv_string()
    if message == 'show count':
        count_display = str(count_usage())
        socket.send_string(count_display)
    elif message == 'log':
        log()
    else:
        continue


