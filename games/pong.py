# Import all necessary values and functions. Please note that everything comes from the imports_and_settings file except for the randint() function from the random module.
from set_up.imports_and_settings import t, delay, board_length, board_height, round_down_xy, WORLD_BORDER
from random import randint

# Establish the square colours for the two pong paddles as global variables.
global PONG_PLAYER1, PONG_PLAYER2
PONG_PLAYER1 = '🟦'
PONG_PLAYER2 = '🟧'

# This function clears the space INSIDE the game board using a y value parameter.
def clear_internal(y):
  # Print a bunch of spaces inside the game board.
  print(t.move_xy(2, y) + ((ext_length*2-4)*" ").center(ext_length*2-4))


# This function prints the game board used for this game (a bunch of white squares.)
def print_world():

  # Establish global variables
  global ext_length, ext_height

  # The external length and height are numbers that represent the inclusive length and height of the game board in white squares.
  ext_length = board_length//2
  ext_height = board_height-10

  # t.cbreak() with the context manager lets us accept any keyboard input without the user pressing the ENTER key.
  with t.cbreak(), t.hidden_cursor():

    # Clear the screen and print the top border
    print(t.home + t.clear, end = "")
    print(ext_length*(WORLD_BORDER + " "))

    # For all the columns in the game board, print a square, then a specific number of spaces, and then another square. This creates the two vertical lines for the border.
    print(t.move_xy(0, 0))
    for _ in range(ext_height):
      print(WORLD_BORDER + (" "*(ext_length*2-3) + WORLD_BORDER))

    # Print the bottom border.
    print(ext_length*(WORLD_BORDER + " "))


# This function prints the two players in this game.
def print_players():
  global player1, player2

  # Using the middle of the game board, create a 2D list of coordinates for player1 and player2. Please note player2 refers to the computer. The mid variable is used in case the game board external height changes. In each player list, there are five coordinates (five smaller lists) that each contain x and y values respectively.
  mid = ext_height//2
  player1 = [[2, mid-2], [2, mid-1], [2, mid], [2, mid+1], [2, mid+2]]
  player2 = [[76, mid-2], [76, mid-1], [76, mid], [76, mid+1], [76, mid+2]]

  # Using for loops, go to each coordinate for each square in each player's position list and print the player's square (blue for player 1, orange for player 2).
  for square in player1:
      print(t.move_xy(square[0], square[1]) + PONG_PLAYER1)
  for square in player2:
      print(t.move_xy(square[0], square[1]) + PONG_PLAYER2)

# This function updates the location of player 1's paddle using a parameter of DIRECTION. The direction is either UP or DOWN.
def update_player1(direction):
  y_values = set()

  if direction:
    # Go to each square in player1's current position and replace it with a blank space.
    for square in player1:
      print(t.move_xy(square[0], square[1]) + " ")

    # For each square in player1's position, print it according to the direction.
    for square in player1:
      # If the direction is UP and the player is NOT at the roof, they move up one square.
      if direction == "UP" and player1[4][1] != 5:
        square[1] -= 1
      # If the direction is DOWN and the player is NOT at the bottom, they move one square down.
      elif direction == "DOWN" and player1[len(player1)-1][1] != ext_height:
        square[1] += 1

      # Print the new position of the square
      print(t.move_xy(square[0], square[1]) + PONG_PLAYER1)

      # Add this new position to the list of y values
      y_values.add(square[1])
  # Return that list of y_values
  return y_values


# This function updates the location of player 2's paddle. Note that this function does not need a parameter, as it automatically determines which direction to move.
def update_player2():

  # If the ball's y position is higher than the middle of the paddle, then the direction the computer needs to move is UP. Else, if the ball is lower than the middle of the paddle, then the direction the computer needs to move is DOWN. 
  direction = ""
  if ball_y < player2[2][1]:
    direction = "UP"
  elif ball_y > player2[2][1]:
    direction = "DOWN"
  
  y_values = set()

  # Go to each square in player1's current position and replace it with a blank space.
  for square in player2:
    print(t.move_xy(square[0], square[1]) + " ")

  # For each square in player1's position, print it according to the direction.
  for square in player2:
    # If the direction is UP and the player is NOT at the roof, they move up one square. Else, if the direction is DOWN and the player is NOT at the bottom, they move one square down.
    if direction == "UP" and player2[4][1] != 5:
      square[1] -= 1
    elif direction == "DOWN" and player2[len(player2)-1][1] != ext_height:
      square[1] += 1

    # Print the new position of the square
    print(t.move_xy(square[0], square[1]) + PONG_PLAYER2)

    # Add this new position to the list of y values
    y_values.add(square[1])
  # Return that list of y_values
  return y_values

# This is the main function that is called from main.py and it calls all the other functions in this document. 
def play_pong(name):
  with t.cbreak(), t.hidden_cursor():
    # Call two functions that are defined above to print the playing game board and the players.
    print_world()
    print_players()
    
    # Moving the cursor, print an greeting to the game and give instructions on how to play. Indicate how to begin playing.
    print(t.move_xy(2, 2) + f"Welcome to PONG, {name}.".center(ext_length*2-4))
    print(t.move_xy(2, 4) + "Please use the UP and DOWN arrow keys to move, and press Q to quit.".center(ext_length*2-4))
    print(t.move_xy(2, 6) + "Press any key to begin.".center(ext_length*2-4))

    # Use the inkey() function to wait until a key is pressed on the keyboard. Then, clear the introduction and instructions.
    t.inkey()
    clear_internal(2)
    clear_internal(4)
    clear_internal(6)

    # Repeat this loop until the user wants to stop playing PONG.
    while True:
      with t.cbreak(), t.hidden_cursor():
        # Call the pong() function to play the game. The outcome is either WIN or LOSE.
        outcome = pong()

        # Let the user know whether they've won or lost.
        if outcome == "WIN":
          print(t.move_xy(4, 2) + f"🟢 Congratulations, {name}! You won! Press any key to play again.🟢".center(ext_length*2-6))
        else:
          print(t.move_xy(4, 2) + f"🔴 Oh no! You lost, {name}! Press A to play again.🔴".center(ext_length*2-6))

        # Let them know how to go back to the Arcade Menu.
        print(t.move_xy(10, 4) + "Or, please wait to go back to the Arcade menu.".center(ext_length*2-12))
      
      delay(1)

      with t.cbreak(), t.hidden_cursor():
        # Wait 5 seconds to see if the user wants to play again.
        again = None
        again = t.inkey(timeout = 7)

        # If they do want to play again (they've indicated by pressing a key), then call the print_world() and print_players() function to reset the board and let them know they can begin playing. Use continue to SKIP the rest of this while loop and play again.
        if again.upper() == "A":
          # Call two functions that are defined above to print the playing game board and the players.
          print_world()
          print_players()
          print(t.move_xy(2, 6) + "Press any key to begin.".center(ext_length*2-4))
          t.inkey()
          print_world()
          print_players()
          continue

        # If this point in the loop is reached, it means they did not want to play again. Thus, count down for them to go back to th Arcade menu and break the loop, terminating the function and returning to main.py
        print(t.move_xy(10, 6) + "You will go back to the arcade menu in...".center(ext_length*2-12))
        delay(1.25)
        print(t.move_xy(2, 8) + "3".center(ext_length*2-4))
        delay(1.25)
        print(t.move_xy(2, 8) + "2".center(ext_length*2-4))
        delay(1.25)
        print(t.move_xy(2, 8) + "1".center(ext_length*2-4))
        delay(1.5)
        break

# This is the main function that plays the PONG game.
def pong():
  # Establish some global variables, and pick a random position for the ball's starting location using randint from the random module.
  global ball_x, ball_y, x_factor, y_factor, player1_y_values
  ball_x, ball_y = randint(10, 60), randint(10, ext_height-10)
  x_factor, y_factor = 1, 1

  # Move the cursor to the ball's initial location.
  print(t.move_xy(ball_x, ball_y))

  # Repeat this loop until something terminates the function. This loop runs several times a second, as it updates the movement of player1, player2, and the ball itself.
  while True:
    global old_position
    move = ""

    # Take an input from the keyboard but only wait 0.02 seconds to do so.
    key = t.inkey(timeout = 0.02)

    # If the key that was pressed was the letter Q, then the user wants to quit. Thus, return that they lost.
    if key.lower() == "q":
      return "LOSE"
    
    # If the key is a sequence (a non-alphanumeric key), then figure out whether it is the UP arrow key or the DOWN arrow key. Identify the player's "move" accordingly.
    if key.is_sequence:
      if int(key.code) == 259:
        move = "UP"
      elif int(key.code) == 258:
        move = "DOWN"
    
    # Call the update_player1 function and get the paddle's y values.
    player1_y_values = update_player1(move)

    # If the player doesn't move, it doesn't have new y values. Thus, we just take it's old position as it's current position.
    if player1_y_values:
      old_position = player1_y_values

    # If the ball is a certain distance from the computer's paddle, only THEN does it begin calculating when to move. This allows us to change how fast it reacts to the ball, and by increasing this value, it gets easier for the computer to lose because it doesn't get enough time to react to the ball.
    if ball_x > 58:
      # Call the update_player2 function and establish it's new y values.
      player2_y_values = update_player2()
      
      # If the ball is in the column next to the paddle AND the ball's y value is in the paddle's y values, then the ball can "bounce" by switching directions. If the ball is past the paddle on the x axis, it means the computer has lost and the player has won. In this case, terminate the function and return WIN.
      if ball_x == 75 and ball_y in player2_y_values:
        x_factor *= -1
      elif ball_x == 77:
        return "WIN"

    # Go to the ball's current position and print a space to clear it.
    remove_ball = t.move_xy(*round_down_xy(ball_x, ball_y)) + ' '

    # If the ball is next to the player's paddle and it in the same y value range as the paddle, then make the ball bounce. Otherwise, if the ball is past the paddle on the x axis, return that the player LOST.
    if ball_x == 4 and (ball_y in old_position or ball_y+1 in old_position or ball_y-1 in old_position):
        x_factor *= -1
    elif ball_x == 2:
      return "LOSE"

    # If the ball hits the top or bottom of the game board, it bounces.
    if ball_y >= ext_height or ball_y <= 1:
        y_factor *= -1

    # Get the new ball x and y values.
    ball_x, ball_y = ball_x + x_factor, ball_y + y_factor

    # Go to the ball's new position and print it.
    add_ball = t.move_xy(*round_down_xy(ball_x, ball_y)) + 'O'

    # Combine the ball's movement change and print it.
    print(remove_ball + add_ball, end='', flush=True)
    delay(0.05)