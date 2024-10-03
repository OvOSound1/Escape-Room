import door
import random

class KeyDoor(door.Door):
    """
    Represents a locked door that requires the player to find the key to unlock it.

    ATTRIBUTES:
    _key_location: int; randomly assigned location of the key (1 to 3 inclusive)
    _input: int; user's choice for where they'll search for the key
    """

    def __init__(self):
        """
        Initializes a KeyDoor instance.
        """
        self._key_location = random.randint(1, 3)
        self._input = 0

    def examine_door(self):
        """
        Describes the locked door.

        Returns:
        A string describing the locked door.
        """
        return "You encounter a locked door. Search for the key nearby."

    def menu_options(self):
        """
        Provides menu options for searching for the locked door's key.

        Returns:
        A string representing options for searching for the key.
        """
        return "1. Rummage through the pile of old newspapers\n2. Check the top shelf of the bookcase\n3. Search behind the painting on the wall"

    def get_menu_max(self):
        """
        Returns the maximum number of menu options.

        Returns:
        An integer representing the number of menu options.
        """
        return 3

    def attempt(self, option):
        """
        Records the user's chosen option for searching and returns a description of their search location.

        Args:
        option (int): The number corresponding to the chosen search location.

        Returns:
        A string describing where the user searched.
        """
        self._input = option
        if option == 1:
            return "\nYou rummage through the pile of old newspapers."
        elif option == 2:
            return "\nYou carefully check the top shelf of the bookcase."
        elif option == 3:
            return "\nYou search behind the painting on the wall."

    def is_unlocked(self):
        """
        Checks if the door has been unlocked.

        Returns:
        A boolean indicating whether the door was unlocked.
        """
        return self._input == self._key_location

    def clue(self):
        """
        Provides a clue when the user fails to find the key.

        Returns:
        A hint to suggest the user to try again elsewhere.
        """
        return "The key isn't here. Keep searching."

    def success(self):
        """
        Provides a congratulatory message when the user unlocks the door.

        Returns:
        A message congratulating the user on finding the key and opening the door.
        """
        return "You found the key and opened the door!"
