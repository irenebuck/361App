# This is Microservice C - Time Preference
# The user enters how long of a delay they would like between the word appearing on the
# screen and the program saying the word aloud.

import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:8080")


def capture_seconds():
    """Asks user for number of seconds they want to delay seeing word to hearing it."""
    entry = input('How many seconds do you want the program to wait to say the word you see? \n '
                'Enter the number of seconds and hit enter. Seconds: ')
    if entry.isdigit():
        return entry
    else:
        entry = input("Please only enter the number of seconds, no letters or other characters.")
        capture_seconds()


while True:
    message = socket.recv_string()
    if message == 'get seconds':
        user_seconds= capture_seconds()
        socket.send_string(user_seconds)
    else:
        continue

