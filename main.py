#Super Subroutine
def color(color, word):
  if color == "red":
    print("\033[31m", word, sep="", end="")
  elif color == "green":
    print("\033[32m", word, sep="", end="")
  elif color == "blue":
    print("\033[34m", word, sep="", end="")
  else:
    print("\033[0m", word, sep="", end="")

print("Super Subroutine")
print("With my ", end="")
color("red", "new program ")
color("reset", "I can just call red ")
color("red", "and ")
color("reset", "that word will appear in the color I set it to. ")
color("reset", "With no ")
color("green", "weird gaps.")
color("reset", "Epic.")
