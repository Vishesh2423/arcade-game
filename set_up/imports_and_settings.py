# Make the necessary imports from various libraries and modules. Please note that the "blessed" library is actually installed in the Packager files.
from blessed import Terminal
import time
from math import floor

# Initialize the terminal function, and name it "t" for short.
t = Terminal()

# Please note that the blessed module does a lot of the terminal work in terms of clearing the console and moving the cursor so that things can be printed.
# t.move_xy(x, y) is a really common command I use to move the cursor to a predetermined x and y location.

# Get the terminal height and width (sometimes, this doesn't work; it's moody.)
term_height, term_width = t.height, t.width

# Define the function "delay". This is the exact same as the time.sleep() function normally used, but I didn't want to type all that every time. Besides, "delay" is a more accurate word than "sleep" because who sleeps for 0.05 seconds? Exactly. No one.
def delay(length):
  time.sleep(length)

# Same reasoning as above. The phrase "get_time" is more readable and understandable, so I used that.
def get_time():
  return time.time()

# This function takes two number arguments and returns them rounded down to the nearest integer using the floor() function.
def round_down_xy(x, y):
    return int(floor(x)), int(floor(y))

# This is a modification to the print() function, as centerPrint just takes the string prints it centered in the terminal.
def centerPrint(string):
  print(string.center(term_width))

# This function determines what game the user wants to play.
def get_game(name):

  # Ask the user for their game preference.
  centerPrint(f"Please type the game that you would like to play, {name}.\n")

  # Establish a set for the three games in this Arcade.
  games = set(("PONG", "TETRIS", "SNAKE"))

  # Run this loop unti a valid game choice is provided.
  while True:

    # Take the user's input guess, and make it all uppercase and remove all black spaces.
    game = input().upper().replace(" ", "")

    # If their guess is valid (in the games set), this loop breaks
    if game in games:
      break
    # Else, we let them know their input wasn't valid, and that they should try again.
    else:
      print("")
      centerPrint(f"That's not a valid game, {name}. Please try again.")
      centerPrint("Make sure to use the game names above.\n")
    
  # By this point in the function, the user has entered a valid game input. Thus, the function returns it.
  return game

# This function prints the Arcade home page to the console.
def arcade_page():

  # Hide the cursor.
  with t.hidden_cursor():

    # Clear the console
    print(t.clear(), end = "")

    # Use the context manager to open the arcade_intro.txt file in READ mode.
    with open("set_up/arcade_intro.txt", "r") as file:

      # Create a blank list.
      data = []

      # For each line in the file, add the line as a string in the list established above.
      for line in file.readlines():
        data.append(line)
      
      # Print the first 9 lines centered in the terminal, removing their conventional "\n" command.
      for i in range(9):
        centerPrint(data[i].replace("\n", ""))
      
      # Print the rest of the lines in the data list aligned with the left of the terminal (as is normally)
      for i in range(9, 18):
        print(data[i].replace("\n", ""))

# Establish the standard board height for the arcade.
board_length = 80
board_height = 36

# Establish the border for all games.
WORLD_BORDER = '⬜'
