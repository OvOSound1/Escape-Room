import abc

class Door(abc.ABC):
  """
  An interface defining methods that different types of doors must implement.
  """

  @abc.abstractmethod
  def examine_door(self): 
    """
    Returns a string describing the door.

    Returns:
    A string describing the door.
    """
    pass

  @abc.abstractmethod
  def menu_options(self):
    """
    Returns a string representing the menu options for the door.

    Returns:
    A string containing menu options for the door.
    """
    pass

  @abc.abstractmethod
  def get_menu_max(self):
    """
    Returns the number of options available in the menu.

    Returns:
    An integer representing the number of menu options.
    """
    pass

  @abc.abstractmethod
  def attempt(self, option):
    """
    Processes the user's selection from the menu.

    Args:
    option (int): The user's selection from the menu.

    Returns:
    A string representing the outcome of the user's attempt.
    """
    pass

  @abc.abstractmethod
  def is_unlocked(self):
    """
    Checks whether the door is unlocked.

    Returns:
    A boolean value indicating whether the door is unlocked (True) or locked (False).
    """
    pass

  @abc.abstractmethod
  def clue(self):
    """
    Provides a hint if the user's attempt is unsuccessful.

    Returns:
    A string containing a hint for the user.
    """
    pass

  @abc.abstractmethod
  def success(self):
    """
    Provides a congratulatory message if the user successfully unlocks the door.

    Returns:
    A string containing a congratulatory message.
    """
    pass
