# This is Microservice C - Time Preference
# The user enters how long of a delay they would like between the word appearing on the
# screen and the program saying the word aloud.


def capture_seconds(user_speed):
    """
    :parameter last character of message sent through pipe
    Removes the last character of the message to determine the speed a user requested.
    :returns the speed in seconds
    """
    if user_speed == 'm':
        return '5'
    elif user_speed == 's':
        return '10'
    else:
        return '3'


while True:
    with open('pipe.txt', 'r') as infile:
        message = infile.readline()
    if 'get seconds' in message:
        choice = message[-1]
        response = capture_seconds(choice)
        with open('pipe.txt', 'w') as outfile:
            outfile.write(response)

