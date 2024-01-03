"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""

EXPECTED_BAKE_TIME = 40


def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """

    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(number_of_layers):

    """Calculate the preparation time in minutes

    :param number_of_layers: int - number of lasagna layers.
    :return: int - preparation time in minutes based on the number of lasagna layers.

    Function that takes the amount of time it takes to prepare the lasagna depending on the number of layers the
    lasagna has.
    """

    return number_of_layers * 2


def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):

    """Calculate the elapsed preparation and bake time in minutes

    :param number_of_layers: int - number of lasagna layers.
    :param elapsed_bake_time: int - amount of time the lasagna has been in the oven.
    :return: int - the amount of time it has been since the preparation started.

    Function that takes in the variables number_of_layers and elapsed_bake_time and returns the amount of time
    that has elapsed since we started making the lasagna.
    """

    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
