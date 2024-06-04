import pyttsx3
import random
import time
import keyboard
import sys


def say_word(seconds, engine, word):
    """Reads the sight word aloud"""
    time.sleep(seconds)
    engine.say(word)
    engine.runAndWait()


def title():
    """Displays the program title at initial opening of program"""
    print("""

  _____  _           ___  _        _    _    __      __             _ 
 |_   _|| |_   ___  / __|(_) __ _ | |_ | |_  \ \    / /___  _ _  __| |
   | |  | ' \ / -_) \__ \| |/ _` || ' \|  _|  \ \/\/ // _ \| '_|/ _` |
   |_|  |_||_|\___| |___/|_|\__, ||_||_|\__|   \_/\_/ \___/|_|  \__,_|
             ___  _         |___/_                                    
            / __|| |_   __ _ | || | ___  _ _   __ _  ___              
           | (__ | ' \ / _` || || |/ -_)| ' \ / _` |/ -_)             
            \___||_||_|\__,_||_||_|\___||_||_|\__, |\___|             
                                              |___/                   
    """)


def opening_message():
    """Displays the reason the user may use the program"""
    print("Practice your 2nd Grade sight words!\n")


def display_options():
    print("COMMANDS:\n"
        "Enter   Hit the Enter key to start the Sight Word game! \n"
        "a       Type a then hit Enter to hear more about this program.\n"
        "c       Type c then hit Enter to check how many times this program has been used.\n"
        "t       Type t then hit Enter to take more time on each word before it is said aloud.\n"
        "q       Type q then hit Enter to exit the program. \n")


def warning():
    """Warns the user about the noise the program creates."""
    print ("WARNING : Check your volume setting.\n"
           "This program displays a word, then says the word aloud after 3 seconds.\n")


def clear_pipe():
    """Deletes everything from the pipe.txt file"""
    with open("pipe.txt", "w") as file:
        pass


def micro_A_usage_count():
    """Implements microservice A - tells the user the number of times the program has been used"""
    with open('pipe.txt', 'w') as outfile:
        outfile.write('get count')
    time.sleep(1)
    with open('pipe.txt', 'r') as infile:
        response = infile.readline()
        print(response)
    clear_pipe()


def micro_A_usage_log():
    """Implements microservice A - tells the user the number of times the program has been used"""
    with open('pipe.txt', 'w') as outfile:
        outfile.write('log')
    time.sleep(1)
    clear_pipe()


def micro_A_delete():
    """Implements microservice A - deletes the last entry in the usage.txt log"""
    with open('pipe.txt', 'w') as outfile:
        outfile.write('delete last')
    time.sleep(1)
    clear_pipe()


def micro_B_about():
    """Implements microservice B - gives information about why and how to use the program"""
    with open('pipe.txt', 'w') as outfile:
        outfile.write('about info')
    time.sleep(1)
    with open('pipe.txt', 'r') as infile:
        response = infile.read()
        print(response)
    clear_pipe()


def micro_C_time(speed):
    """
    Implements microservice C - gets user's choice of time between seeing and saying word in seconds
    Returns: integer - number of seconds
    """
    with open('pipe.txt', 'w') as outfile:
        outfile.write(f'get seconds {speed}')
    time.sleep(1)
    with open('pipe.txt', 'r') as infile:
        response = int(infile.readline())
    clear_pipe()
    return response


def micro_D_quit():
    """
    Implements microservice D - quits program and displays message
    """
    with open('pipe.txt', 'w') as outfile:
        outfile.write('get teacher message')
    time.sleep(1)
    with open('pipe.txt', 'r') as infile:
        response = infile.read()
        print(response)
    clear_pipe()
    sys.exit()


def break_loop(hit_q):
    """Uses a mutable list to change the hit_q flag and removes the credit in the
    usage.txt tracker so user doesn't get credit for last play/log removed"""
    hit_q[0] = True
    micro_A_delete()


def command_entered():
    """
    This function takes input from user about which feature of the program they want to use
    """
    entry = input('What do you want to do? ')
    if entry == 't':
        speed = input('Do you want to go slow, medium, or fast? Hit s for slow, m for medium, or f for fast.')
        response = micro_C_time(speed)
        one_game(response)
    elif entry == 'a':
        micro_B_about()
        command_entered()
    elif entry == 'c':
        micro_A_usage_count()
        command_entered()
    elif entry == '':
        one_game(3)
    elif entry == 'q':
        print("Goodbye!")
        sys.exit()
    else:
        command_entered()


def read_shuffle():
    """Opens, reads, and then shuffles the words in words.txt file"""
    with open("words.txt", "r") as infile:
        words = infile.readlines()
    random.shuffle(words)
    return words


def display_word(word_to_display, words_remaining):
    """
    :param word_to_display: word the user will see and hear read to them
    :param words_remaining:
    This function displays word and number of words remaining to finish the game.
    """
    print (f'\n'
           f'{word_to_display}\n'
           f'Words remaining: {words_remaining}'
           f'\n')


def one_game(seconds):
    """
    Parameter: number of seconds the user want to delay from seeing word to hearing it.
    This program plays through one game with either default 3-second delay or user's choice.
    Delay applies to time word appears on screen to when pyttsx3 module says it aloud.
    """
    micro_A_usage_log()
    engine = pyttsx3.init()
    count = 0
    words = read_shuffle()
    number_of_words = len(words)
    hit_q = [False]
    print('\nHit the q key to exit the game early.\n')
    keyboard.add_hotkey('q', break_loop, args=(hit_q,))
    while count < number_of_words and not hit_q[0]:
        remaining = number_of_words - count - 1
        display_word(words[count], remaining)
        say_word(seconds, engine, words[count])
        count += 1
    micro_D_quit()


if __name__ == "__main__":
    title()
    opening_message()
    warning()
    display_options()
    command_entered()
