import os

INPUT_FILE = os.path.join(os.path.dirname(__file__), "input_example_1.txt")

with open(INPUT_FILE) as f:
    input_text = f.read()

translocate = {
   (-1, 0): { # North
      "|": (-1, 0),
      "F": (-1, 1),
      "7": (-1, -1),
   },
   (0, 1): { # East
      "-": (0, 1),
      "J": (-1, 1),
      "7": (1, 1),
   },
   (1, 0): { # South
      "|": (1, 0),
      "L": (1, 1),
      "J": (1, -1),
   },
   (0, -1): { # West
      "-": (0, -1),
      "L": (-1, -1),
      "F": (1, -1),
   },
}
lines = input_text.split("\n")
matrix = [[c for c in line] for line in lines]

def find_start_position():
   for i in range(len(matrix)):
      line = matrix[i]
      for j in range(len(line)):
         point = matrix[i][j]
         if point == "S":
            return i, j
   raise Exception("No starting point found")

current_position = find_start_position()
travelled = 0
while True:
   checks = [(-1, 0), (0, 1), (1, 0), (0, -1)]
   for check in checks:
      try:
         next_pipe = matrix[current_position[0] + check[0]][current_position[1] + check[1]]
      except IndexError:
         continue
      if (shift := translocate[check].get(next_pipe)):
         travelled += 1 if next_pipe in ("-", "|") else 2
         current_position = current_position[0] + shift[0], current_position[1] + shift[1]
         break
   current_pipe = matrix[current_position[0]][current_position[1]]
   if current_pipe == "S":
      break
print(travelled / 2)