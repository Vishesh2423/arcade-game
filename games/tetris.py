# Import all necessary values and functions. Please note that everything comes from the imports_and_settings file except for the randint() function from the random module and the games.shapes file we created.
from set_up.imports_and_settings import t, board_height, WORLD_BORDER, delay, get_time
import games.shapes
from random import randint

# This function clears the space INSIDE the game board using a y value parameter.
def clear_internal(y):
  # Print a bunch of spaces inside the game board.
  print(t.move_xy(2, y) + ((ext_length*2-4)*" ").center(ext_length*2-4))

# This function prints the game board used for this game (a bunch of white squares.) This function follows the same structure as the print_world() function in pong.py, with different values. Thus, refer to that for comments (need to be efficient and not repetitive)
def print_world():
  global ext_length, ext_height
  ext_length = 26
  ext_height = board_height-10
  with t.cbreak(), t.hidden_cursor():
    print(t.home + t.clear, end = "")
    for _ in range(ext_height):
      print(WORLD_BORDER + (" "*(ext_length*2-3) + WORLD_BORDER))

    print(ext_length*(WORLD_BORDER + " "))

# This function is the introduction to Tetris.
def introduction(name):
  with t.cbreak(), t.hidden_cursor():
    #  After moving the cursor to each intended line, print an greeting to the game and give instructions on how to play. Indicate how to begin playing.
    print(t.move_xy(2, 1) + f"Welcome to TETRIS, {name}".center(ext_length*2-4))
    print(t.move_xy(2, 3) + "Please use the LEFT and RIGHT arrow keys".center(ext_length*2-4))
    print(t.move_xy(2, 4) + "to move falling objects.".center(ext_length*2-4))
    print(t.move_xy(2, 6) + "Press R to rotate objects as they fall.".center(ext_length*2-4))
    print(t.move_xy(2, 8) + "Press Q to exit.".center(ext_length*2-4))
    print(t.move_xy(2, 10) + "Press any key to begin.".center(ext_length*2-4))

    # After waiting for any key to be pressed, clear all the instructions.
    t.inkey()
    clear_internal(1)
    clear_internal(3)
    clear_internal(4)
    clear_internal(6)
    clear_internal(8)
    clear_internal(10)

# This is the main function that is called from main.py and it calls all the other functions in this document. 
def play_tetris(name):
  with t.hidden_cursor():
    # Call two functions that are defined above to print the playing game board and the introduction.
    print_world()
    introduction(name)

    # Call the tetris() function to play the game. The value returned is the player's score.
    score = tetris()

    delay(0.5)

    # Print the world again to get rid of all the tetris blocks.
    print_world()

    # After receiving the score, let the user know what score they got.
    print(t.move_xy(2, 1) + f"🟠 Wow! You got a score of {score}, Vishesh!🟠".center(ext_length*2-4))

    # Let them know that they can wait to go back to the Arcade main menu. They do not get to directly play again because... who wants to play Tetris again?
    print(t.move_xy(2, 3) + "Please wait 5 seconds to go back".center(ext_length*2-4))
    print(t.move_xy(2, 4) + "to the arcade menu.".center(ext_length*2-4))
    delay(2)

    # Count down for them to return to the main page.
    print(t.move_xy(2, 6) + "You will go back to the arcade menu in...".center(ext_length*2-4))
    delay(1)
    print(t.move_xy(2, 8) + "3".center(ext_length*2-4))
    delay(1.25)
    print(t.move_xy(2, 8) + "2".center(ext_length*2-4))
    delay(1.25)
    print(t.move_xy(2, 8) + "1".center(ext_length*2-4))
    delay(1.5)

# This is the main function that plays the TETRIS game.
def tetris():
  # Establish some global variables, and set most of them as blank or 0.
  global current_shape, current_coordinates, history, max_y_set, max_y
  rotation = 0      # Rotation is how many times the shape has been rotated.
  current_coordinates = []
  current_shape = []
  history = []      # History is a record of the position of all past shapes.
  score = 0
  max_y_set = set()     # This is a record of the y values of all blocks (to find the highest block)
  bypass = True     # Bypass means the user is ready to receive a new shape
  max_y = 19      # The max y value is the point where the user cannot move the blocks.

  # The start interval is the current time, and the fall interval is 0.3 seconds. Fall is the 0.3 seconds from the current time.
  start_interval = get_time()
  fall_interval = 0.3
  fall = start_interval + fall_interval
  

  with t.cbreak(), t.hidden_cursor():
    # Repeat this loop until something terminates the function. This loop runs several times a second, as it updates the movement of the blocks.
    while True:
      # This checks if the user is ready to receive a new shape.
      if bypass == True:
        delay(0.5)

        # Since they are receiving a new shape, bypass because False and the rotation resets.
        bypass = False
        rotation = 0

        # If the highest block is at the top of the screen, the entire function terminates and returns the score because this means the game has ended.
        if max_y == 1:
          return score

        # This picks a random number to pick a random shape
        number = randint(1, 5)
        new_shape = []

        # This uses a random integer to pick a value from the x_values in games.shapes. This x_point is the starting x value of the block. This also picks a random colour for the shape.
        x_point = games.shapes.x_values[randint(0, len(games.shapes.x_values)-1)]
        colour = games.shapes.colour[randint(0, 6)]

        # This calls on the get_shape() function to get a 3D list of the shape based on the starting x value and intended shape.
        new_shape = games.shapes.get_shape(x = x_point, num = number)

        # Print the shape to the console
        for block in new_shape[0]:
          print(t.move_xy(block[0], block[1]) + colour)
        
        # Establish that the current shape is this new shape, and it's coordinates are the first rotational coordinates in the current shape
        # PLEASE NOTE THAT THIS MEANS:
        # The current shape variable is a 3D list, the coordinates variable is a 2D list, and the rotation is the index of coordinates in current_shape.
        current_shape = new_shape
        coordinates = current_shape[rotation]

        # Add to the score and print it at the bottom of the screen.
        score += len(new_shape[0])
        print(t.move_xy(0, 28))
        print(f"Score: {score}.")
      
      # Take an input from the keyboard but only wait 0.02 seconds to do so.
      key = t.inkey(timeout = 0.02)
      
      # If the key is R, then increase the rotation by 1. If the rotation is 4, then reset it to 0. If the key is Q, it means the user wants to quit the game and the function terminates and returns the score.
      if key.lower() == "r":
        rotation += 1
        if rotation == 4:
          rotation = 0
      elif key.lower() == "q":
        return score

      # Call on the update_shape function to find the updated shape based on what the user inputs. Send in ALL the variables we have because they're all important.
      values = update_shape(key, current_shape, rotation, coordinates, number, colour)

      # If a valid key was pressed, then get the values and establish them as the coordinates and current shape.
      if values:
        coordinates, current_shape = values
      
      # If the current time is greater than or equal to the time when a shape should fall:
      if get_time() >= fall:
        # Reset the start interval, get the new fall time, and get the most up to date pair of coordinates.
        start_interval = get_time()
        fall = start_interval + fall_interval
        coordinates = current_shape[rotation]

        move = True
        # Check to make sure that if the shape was to fall, it would NOT go past the bottom of the game board. Also, make sure that it would not collide with any of the previous shapes.
        for coordinate in coordinates:
          if coordinate[1] + 1 >= ext_height or [coordinate[0], coordinate[1]+1] in history:
            move = False

        # If the move is valid, then delete the current block by printing spaces, add one to the y value in each coordinate pair, and then the shape in its new position in the appropriate colour.
        if move:
          for coordinate in coordinates:
            print(t.move_xy(coordinate[0], coordinate[1]) + " ")
            coordinate[1] += 1
          for coordinate in coordinates:
            print(t.move_xy(coordinate[0], coordinate[1]) + colour)

        # If the move is not valid, then that means the the shape is in its final position.
        elif not move:
          # Add each coordinate pair to the history list to indicate a block is there, and add each y value in the set of y values.
          for coordinate in coordinates:
            history.append(coordinate)
            max_y_set.add(coordinate[1])
          # The maximum y value becomes the max in the set of y values, and since the shape has stopped moving, it's time to drop another shape. Thus, we make bypass True.
          max_y = min(max_y_set)
          bypass = True


# This function takes the key pressed, the current shape, the rotation number, the coordinates of the shape, the number of which shape it is, and the colour of the shape as an argument.
def update_shape(key, current_shape, rotation, coordinates, number, colour):
  move = ""

  # If the user wants to ROTATE:
  if key.lower() == "r":
    # The current x and y coordinates are taken from the list.
    x, y = coordinates[0]

    # A new shape and new set of coordinates is generated using the methods outlined above. The rotation has already been increased by one, so the new coordinates are the POTENTIALLY rotated coordinates.
    new_shape = games.shapes.get_shape(x, y, number)
    new_coordinates = new_shape[rotation]

    move = True

    # Check if each coordinate in the new shape would be valid. This means that if they are lower than the max y value, or at the very edge of the game board, then the move is False.
    for coordinate in new_coordinates:
      if coordinate[1] >= max_y+3 or coordinate[0] <= 2 or coordinate[0] >= 48:
        move = False

    # If the move is NOT false:
    if move:
      # Go to each coordinate in the current coordinates and print a space to get rid of the shape
      for coordinate in coordinates:
        print(t.move_xy(coordinate[0], coordinate[1]) + " ")
      # Then, go the each coordinate in the new set of coordinates and print the shape in the intended colour.
      for coordinate in new_coordinates:
        print(t.move_xy(coordinate[0], coordinate[1]) + colour)
      # Return the new coordinates and the new shape.
      return (new_coordinates, new_shape)
    # If the move was false, then just return the current coordinates and shape.
    return (coordinates, current_shape)

  elif key.is_sequence:
    # If the key is the RIGHT arrow:
    if int(key.code) == 261:
      # Get the coordinates based on the rotation
      coordinates = current_shape[rotation]
      move = True
      
      # Check if the move is valid
      for coordinate in coordinates:
        if coordinate[1] >= max_y+3 or coordinate[0] == 48:
          move = False

      # If the move is valid, the go to each current coordinate, delete it by printing a space, add 2 to the x value in the coordinate pair, and then use another for loop to print each block in the new coordinate 2D list. 
      if move:
        for coordinate in coordinates:
          print(t.move_xy(coordinate[0], coordinate[1]) + " ")
          coordinate[0] += 2
        for coordinate in coordinates:
          print(t.move_xy(coordinate[0], coordinate[1]) + colour)

      # Return the new coordinates and shape.
      return(coordinates, current_shape)

    # If the key is the LEFT arrow:
    elif int(key.code) == 260:
      # Get the coordinates based on the rotation
      coordinates = current_shape[rotation]
      move = True

      # Check if the move is valid
      for coordinate in coordinates:
        if coordinate[1] >= max_y+3 or coordinate[0] == 2:
          move = False

      # If the move is valid, the go to each current coordinate, delete it by printing a space, subtract 2 from the x value in the coordinate pair, and then use another for loop to print each block in the new coordinate 2D list. 
      if move:
        for coordinate in coordinates:
          print(t.move_xy(coordinate[0], coordinate[1]) + " ")
          coordinate[0] -= 2
        for coordinate in coordinates:
          print(t.move_xy(coordinate[0], coordinate[1]) + colour)

      # Return the new coordinates and shape.
      return (coordinates, current_shape)
  
  # If the key pressed is not R, LEFT ARROW, OR RIGHT ARROW, then just return the function.
  else:
    return (coordinates, current_shape)