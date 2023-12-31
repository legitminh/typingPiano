from typing import Any
from enum import Enum


class ExitException(Exception):
    """
    Error raised when the Player exits the screen
    """
    pass


class ScreenID(Enum):
    intro = 1
    menu = 2
    levelOptions = 3
    level = 4
    outro = 5
    option = 6


class Redirect:
    def __init__(self, redirect_screen: ScreenID, **kwargs) -> None:
        self.redirect_screen = redirect_screen
        self.params = kwargs
