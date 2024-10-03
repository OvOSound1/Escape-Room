import door
from random import randint

class BasicDoor(door.Door):
  """
  Represents a basic door that can be pushed or pulled to open.

  ATTRIBUTES:
  _state: int; represents whether the door needs to be pushed (1) or pulled (2) to open.
  _input: int; stores the user's choice in attempting to open the door.
  """

  def __init__(self):
    """
    Initializes a BasicDoor instance with a random state (push or pull).
    """
    self._state = randint(1, 2)
    self._input = 0 

  def examine_door(self): 
    """
    Returns a string description of the basic door.

    Returns:
    A string describing the basic door.
    """
    return "You encounter a basic door. It can be pushed or pulled."

  def menu_options(self):
    """
    Returns a string of menu options for the door.

    Returns:
    A string containing menu options for the user to choose from to open the door.
    """
    return "1. Push\n2. Pull"

  def get_menu_max(self):
    """
    Returns the number of options in the menu.

    Returns:
    An integer representing the number of menu options.
    """
    return 2

  def attempt(self, option):
    """
    Processes the user's selection from the menu.

    Args:
    option (int): The user's choice representing whether to push or pull the door.

    Returns:
    A string describing the user's choice action.
    """
    self._input = option
    if option == 1:
      return "\nYou push the door.\n"
    else:
      return "\nYou pull the door.\n"

  def is_unlocked(self):
    """
    Checks whether the door is unlocked.

    Returns:
    A boolean indicating whether the door is unlocked (True) or locked (False).
    """
    return self._state == self._input

  def clue(self):
    """
    Provides a hint if the user's attempt is unsuccessful.

    Returns:
    A string hinting to the user to try the other way.
    """
    return "Try the other way."

  def success(self):
    """
    Provides a congratulatory message if the user successfully unlocks the door.

    Returns:
    A string containing a congratulatory message.
    """
    if self.is_unlocked():
      return "Congratulations, you opened the door!"
