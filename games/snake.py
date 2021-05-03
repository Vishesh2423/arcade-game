# Import all necessary values and functions. Please note that everything comes from the imports_and_settings file.
from set_up.imports_and_settings import t, board_height, board_length, WORLD_BORDER, delay

# This function clears the space INSIDE the game board using a y value parameter.
def clear_internal(y):
  # Print a bunch of spaces inside the game board.
  print(t.move_xy(2, y) + ((ext_length*2-4)*" ").center(ext_length*2-4))


# This function prints the game board used for this game (a bunch of white squares.) This function follows the same structure as the print_world() function in pong.py, with different values. Thus, refer to that for comments (need to be efficient and not repetitive)
def print_world():
  global ext_length, ext_height
  ext_length = board_length//2-8
  ext_height = board_height-14
  with t.cbreak(), t.hidden_cursor():

    print(t.home + t.clear, end = "")
    print(ext_length*(WORLD_BORDER + " "))

    print(t.move_xy(0, 0))
    for _ in range(ext_height):
      print(WORLD_BORDER + (" "*(ext_length*2-3) + WORLD_BORDER))

    print(ext_length*(WORLD_BORDER + " "))


# This function takes an input of the snake's coordinates and the food's coordinates. Then, it iterates through each square in the snake and prints it to the console, and then prints the food and the head of the snake as well.
def print_players(snake, food):
  for square in snake:
    print(t.move_xy(square[0], square[1]) + BODY)
  print(t.move_xy(food[0], food[1]) + FOOD)
  print(t.move_xy(head_start[0], head_start[1]) + HEAD)


# This function is the introduction to the Snake Game.
def print_instructions(name):
  with t.cbreak(), t.hidden_cursor():
    #  After moving the cursor to each intended line, print an greeting to the game and give instructions on how to play and quit. Indicate how to begin playing.
    print(t.move_xy(2, 2) + "Welcome to the SNAKE GAME... with a twist.".center(ext_length*2-4))
    print(t.move_xy(2, 4) + f"YOU are the food {name}, and you must run.".center(ext_length*2-4))
    print(t.move_xy(2, 6) + "Please use the ARROW keys or WASD to move.".center(ext_length*2-4))
    print(t.move_xy(2, 8) + "Press Q to exit. Press any key to begin.".center(ext_length*2-4))

    # After waiting for any key to be pressed, clear all the instructions.
    t.inkey()
    clear_internal(2)
    clear_internal(4)
    clear_internal(6)
    clear_internal(8)


# This is the main function that is called from main.py and it calls all the other functions in this document. 
def play_snake(name):
  with t.cbreak(), t.hidden_cursor(): 
    # Clear the terminal and establish a LOT of global variables.
    print(t.home + t.clear, end = "")
    global BODY, HEAD, FOOD, head_start, DIRECTIONS, MOVEMENT_MAP, UP, RIGHT, LEFT, DOWN, M, N1, N2, MAX_SPEED, WASD_DICT

    # Establish initial blocks and positions
    BODY = "🟩"
    HEAD = "🟥"
    FOOD = "🥭"
    food = [44, 15]
    head_start = [22, 15]

    # Create the start positions for the snake with a 2D list
    snake = [
    [head_start[0], head_start[1]],
    [head_start[0]-2, head_start[1]],
    [head_start[0]-4, head_start[1]],
    [head_start[0]-6, head_start[1]],
    [head_start[0]-8, head_start[1]],
    [head_start[0]-10, head_start[1]]
    ]

    # Establish the direction keys and put them into a list
    UP = t.KEY_UP
    RIGHT = t.KEY_RIGHT
    LEFT = t.KEY_LEFT
    DOWN = t.KEY_DOWN
    DIRECTIONS = [LEFT, UP, RIGHT, DOWN]

    # Use a dictionary to map changes in x and y to each directional movement
    MOVEMENT_MAP = {
      LEFT: [-2, 0],
      UP: [0, -1],
      RIGHT: [2, 0],
      DOWN: [0, 1]
    }

    # Use a dictionary to map the WASD keys to a direction.
    WASD_DICT = {
      "w": UP,
      "a": LEFT,
      "s": DOWN,
      "d": RIGHT
    }

    MAX_SPEED = 6 # Max speed of snake
    M = 9 # The snake grows every M cycles
    N1 = 1 # The snake moves N1/N2 times.
    N2 = 2

    # Print the game board, the snake, the food, and the instructions.
    print_world()
    print_players(snake, food)
    print_instructions(name)

    # While the user is playing pong
    while True:
      # Play the pong game using the pong() function
      outcome, score = snake_game(snake, food)

      with t.hidden_cursor():
        delay(0.5)
        print_world()

        # Display the outcome of the game
        if outcome == "WIN":
          print(t.move_xy(2, 2) + f"🟢 Congratulations, {name}! You won with a score of {score}.🟢".center(ext_length*2-4))
        else:
          print(t.move_xy(2, 2) + f"🔴 Oh no, {name}! You lost with a score of {score}.🔴".center(ext_length*2-4))

        # Give them instructions on what to do next
        print(t.move_xy(2, 4) + "Press A to play again. Or, please wait".center(ext_length*2-4))
        print(t.move_xy(2, 5) + "to go back to the arcade menu.".center(ext_length*2-4))
      
      delay(1)

      with t.cbreak(), t.hidden_cursor():
        # Wait 5 seconds to see if the user wants to play again
        again = None
        again = t.inkey(timeout = 7)

        # If they do want to play again (they've indicated by pressing a key), then call the print_world() function to reset the board and let them know they can begin playing. Use continue to SKIP the rest of this while loop and play again.
        if again.upper() == "A":
          # Print the game board.
          print_world()
          print_players(snake, food)
          print(t.move_xy(2, 4) + "Press any key to begin.".center(ext_length*2-4))
          t.inkey()
          clear_internal(4)
          continue

        # If this point in the loop is reached, it means they did not want to play again. Thus, count down for them to go back to th Arcade menu and break the loop, terminating the function and returning to main.py
        print(t.move_xy(2, 7) + "You will go back to the arcade menu in...".center(ext_length*2-4))
        delay(1.25)
        print(t.move_xy(2, 9) + "3".center(ext_length*2-4))
        delay(1.25)
        print(t.move_xy(2, 9) + "2".center(ext_length*2-4))
        delay(1.25)
        print(t.move_xy(2, 9) + "1".center(ext_length*2-4))
        delay(1.5)
        break
    
# This is the main snake game function
def snake_game(first_snake, first_food):

  # Establish a bunch of variables, including the speed for the snake
  global turn, speed, snake, dead
  snake = first_snake
  food = first_food
  turn = 0
  speed = 3
  dead = False

  # This loop repeats itself until the game ends.
  with t.cbreak(), t.hidden_cursor():
    while True:
      # Take an input at a predetermined timeout speed
      key = t.inkey(timeout = 1/speed)

      # If the user presses Q, then terminate the function.
      if key.isalpha():
        if key.lower() == "q":
          dead = True
          break

      # Call the get_snake_move() function to get the snake's next move, the position of it's head after the move, and updated food and head values.
      next_move, future_head, food, head = get_snake_move(snake, food)

      # If the snake doesn't have a next move, then there's a problem.
      if not next_move:
        break
      
      # Add one to the turn to indicate the loop has run once
      turn += 1

      # If the snake is allowed to move, calculate the move and print the new head and snake accordingly
      if turn%N2 < N1:
        snake = [next_move] + snake
        print(t.move_xy(head[0], head[1]) + BODY)
        if turn % M != 0:
          speed = min(speed * 1.05, MAX_SPEED)
          tail = snake.pop()
          print(t.move_xy(tail[0], tail[1]) + " ")
        print(t.move_xy(next_move[0], next_move[1]) + HEAD)

      # Call the move_food function, send in ALL the important variables, and get dead and food as return values.
      dead, food = move_food(key, next_move, head, food, snake, dead)

      # Calculate and print the score
      score = int(turn/2)
      print(t.move_xy(0, ext_height+2) + f"Score: {score}.")
      print(f"Snake Size = {len(snake)}.")
      
      # If the snake is dead, break out of the loop
      if dead:
        break

    # If the snake is dead, return whether the user won or lost and their score.
    if dead:
      return ("LOSE", score)
    else:
      return ("WIN", score)
          
# This function gets the snake's next move.
def get_snake_move(snake, food):
  head = snake[0]
  x_difference = food[0] - head[0]
  y_difference = food[1] - head[1]

  # Determine the preferred move for the snake (in the direction of the food) using the differences in x and y
  preferred_move = None
  if abs(x_difference) > abs(y_difference):
    if x_difference >= 0:
      preferred_move = RIGHT
    else:
      preferred_move = LEFT
  else:
    if y_difference <= 0:
      preferred_move = UP
    else:
      preferred_move = DOWN
  
  # Create a list of preferred_moves, with the actual preferred move as the first item and the other directions as the other elements.
  preferred_moves = [preferred_move] + DIRECTIONS

  next_move = None
  
  # Check if the preferred move is valid, and cycle through the other possible moves if it is not. When the final next_move is found, print it to the console.
  for move in preferred_moves:
    # Get the appropriate movement shift
    movement_shift = MOVEMENT_MAP[move]
    # Find the future location of the head of the snake
    future_head = head.copy()
    future_head[0] += movement_shift[0]
    future_head[1] += movement_shift[1]
    # If the future head is in the world border, continue to the next preferred_moves element
    if future_head[0] == 0 or future_head[0] == (ext_length-1)*2 or future_head[1] == 0 or future_head[1] == ext_height+1:
      continue
    # If the future head is in the snake:
    elif future_head in snake:
      # If the future head is the current tail and the snake is NOT going to grow this turn, then it is safe to say that the future_head is valid
      if future_head == snake[-1] and turn%M != 0:
        next_move = future_head
        break
      # Otherwise, the move isn't valid.
      else:
        continue
    else:
      next_move = future_head
      break
  # Return the values
  return next_move, future_head, food, head


# This function finds the moves for the food
def move_food(key, next_move, head, food, snake, dead):

  future_food = food.copy()

  # Calculate the direction in which the food is moving based on the key that was pressed
  if key.code in DIRECTIONS or key.lower() in WASD_DICT:
    food_move = None
    if key in WASD_DICT:
      food_move = WASD_DICT[key.lower()]
    else:
      food_move = key.code
    # Move the food using the movement map and find the future_location
    food_shift = MOVEMENT_MAP[food_move]
    future_food[0] += food_shift[0]
    future_food[1] += food_shift[1]

  # Make sure the food is not dead because of this move. If it is dead, then dead is True.
  if future_food == next_move:
    print(t.move_xy(future_food[0], future_food[1]) + HEAD)
    print(t.move_xy(head[0], head[1]) + BODY)
    dead = True
  elif food in snake:
    dead = True
  
  # If the food is not dead, check a bunch of conditions to ensure that the move for the food is valid (to ensure it stays within the borders and doesn't violate any rules. If it is valid, then print it to the console.)
  if not dead:
    if future_food not in snake and future_food[0] != 0 and future_food[0] != (ext_length-1)*2 and future_food[1] != 0 and future_food[1] != ext_height+1:
      print(t.move_xy(food[0], food[1]) + " ")
      food = future_food
      print(t.move_xy(food[0], food[1]) + FOOD)
  # Return these values
  return dead, food