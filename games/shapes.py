# Create a blank list.
x_values = []
# Start at 8, and count by 2's to 42 (inclusively). Append each number into the list. This is used to determine a random x position to drop the Tetris block.
for i in range(8, 43, 2):
  x_values.append(i)

# Create a list of all the possible colours for the blocks.
colour = tuple(("🟥","🟧","🟨","🟩","🟦","🟪","🟫"))

#---------------------------------------------------
# Each of the following functions draws a specific block.
# Please visit this link for a description of the blocks:
#      https://i.gzn.jp/img/2019/11/16/tetris-algorithm/tetmino.png

# Each function is named after the block that it draws. It takes two arguments, both of which are optional because they have a default x and y value. The default value would draw it in the top right corner. Each function has a 3D list. In this list, are four 2D lists. Each of the four 2D lists are an orientation of the shape. For example, the first 2D list in the Z_block function would be the shape rotated 0 degrees. The second 2D list would be the shape rotated 90 degrees, etc. Each of the coordinates are relative to the singular x and y coordinate being drawn. Thus, when the function is called, it calculates all the possible rotational positions of the shape in the 3D list. It returns that list of rotational coordinates.

def Z_block(x = 8, y = 0):
  shape = [
    [[x, y], [x+2, y], [x+2, y+1], [x+4, y+1]],
    [[x, y], [x, y+1], [x-2, y+1], [x-2, y+2]],
    [[x, y], [x-4, y-1], [x-2, y-1], [x-2, y]],
    [[x, y], [x+2, y-2], [x+2, y-1], [x, y-1]]
    ]
  return shape

def O_block(x = 8, y = 0):
  shape = [
    [[x, y], [x+2, y], [x+2, y+1], [x, y+1]],
    [[x, y], [x+2, y], [x+2, y+1], [x, y+1]],
    [[x, y], [x+2, y], [x+2, y+1], [x, y+1]],
    [[x, y], [x+2, y], [x+2, y+1], [x, y+1]],
    ]
  return shape # Note that the O block cannot be rotated.

def L_block(x = 8, y = 0):
  shape = [
    [[x, y], [x, y+1], [x+2, y], [x+4, y]],
    [[x, y], [x-2, y], [x, y+1], [x, y+2]],
    [[x, y], [x-4, y], [x-2, y], [x, y-1]],
    [[x, y], [x, y-2], [x, y-1], [x+2, y]]
    ]
  return shape

def I_block(x = 8, y = 0):
  shape = [
    [[x, y], [x-2, y], [x+2, y], [x+4, y]],
    [[x, y], [x, y-1], [x, y+1], [x, y+2]],
    [[x, y], [x+2, y], [x-2, y], [x-4, y]],
    [[x, y], [x, y+1], [x, y-1], [x, y-2]],
    ]
  return shape
  
def T_block(x = 8, y = 0):
  shape = [
    [[x, y], [x-2, y], [x+2, y], [x, y+1]],
    [[x, y], [x, y-1], [x, y+1], [x-2, y]],
    [[x, y], [x-2, y], [x+2, y], [x, y-1]],
    [[x, y], [x, y-1], [x, y+1], [x+2, y]],
    ]
  return shape

# This last function takes a number input. Based on the number, it calls the different functions and sends in the x and y values as arguments. This function is used to return the 3D list discussed above based on the shape that is needed. 
def get_shape(x = 8, y = 0, num = 0):
  if num == 1:
    return Z_block(x, y)
  elif num == 2:
    return O_block(x, y)
  elif num == 3:
    return L_block(x, y)
  elif num == 4:
    return I_block(x, y)
  elif num == 5:
    return T_block(x, y)