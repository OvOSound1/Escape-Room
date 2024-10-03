import check_input
from combination_door import CombinationDoor
from basic_door import BasicDoor
from key_door import KeyDoor
from random import randint

def open_door(door):
  """
  Allows the player to attempt to unlock a door. Displays the door's description and menu options, prompts the user for an action, and displays the result. If the attempt fails, a clue is provided and the loop continues until the door is successfully unlocked.
  Args:
  door (object): The door the user will attempt to unlock.
  """
  print(door.examine_door())
  print(door.menu_options())
  user_input = check_input.get_int_range("", 1, door.get_menu_max())
  print(door.attempt(user_input))
  while door.is_unlocked() == False:
    print(door.clue() + "\n")
    print(door.menu_options())
    user_input = check_input.get_int_range("", 1, door.get_menu_max())
    print(door.attempt(user_input))

  print(door.success())

def main():
  print("Welcome to the Escape Room.")
  print("You must unlock 3 doors to escape...\n")
  # Creates a list of doors
  doors = [CombinationDoor(), BasicDoor(), KeyDoor()]

  # Iterates through the list and removes it if the player opens the door
  for i in range(len(doors)):
    if len(doors) == 0:
      num = 0
    else: 
      num = randint(0,len(doors)-1)
    open_door(doors[num])
    doors.pop(num)
    print("")

  print("You've Escaped!")

main()
