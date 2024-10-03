import door
from random import randint

class CombinationDoor(door.Door):
  """
  Represents a combination door where the user has to guess the correct number.

  ATTRIBUTES:
  _correct_value: int; randomly generated number between 1 and 10 as the correct combination
  _input: int; user's guessed value
  """

  def __init__(self):
    """
    Initializes a CombinationDoor instance with a random correct value.
    """
    self._correct_value = randint(1, 10)
    self._input = 0

  def examine_door(self): 
    """
    Provides a description of the combination door.

    Returns:
    A string describing the combination door.
    """
    return "You encounter a door with a combination lock, you can spin the dial to a number 1-10."

  def menu_options(self):
    """
    Provides a prompt for the user to enter their guess.

    Returns:
    A string indicating the range of possible combinations.
    """
    return "\nEnter a number 1-10: "

  def get_menu_max(self):
    """
    Returns the maximum possible value for the user's guess.

    Returns:
    An integer representing the maximum possible value.
    """
    return 10

  def attempt(self, option):
    """
    Records the user's guess attempt.

    Args:
    option (int): The number chosen by the user as their guess.

    Returns:
    A string describing the user's guess attempt.
    """
    self._input = option
    return f"\nYou turn the dial to... {str(self._input)}"

  def is_unlocked(self):
    """
    Checks whether the door is unlocked.

    Returns:
    A boolean indicating whether the door is unlocked (True) or locked (False).
    """
    return self._input == self._correct_value

  def clue(self):
    """
    Provides a hint based on whether the user's guess was too high or too low.

    Returns:
    A string hinting to the user whether their guess was too high or too low.
    """
    if self._input > self._correct_value:
      return "Try a lower number."
    else:
      return "Try a higher number."

  def success(self):
    """
    Provides a congratulatory message if the user successfully unlocks the door.

    Returns:
    A string containing a congratulatory message.
    """
    return "Congratulations! You opened the door!"
