###############################################################################
#     ____                          __     _                          _____
#    / __ \  __  __  ___    _____  / /_   (_)  ____    ____          |__  /
#   / / / / / / / / / _ \  / ___/ / __/  / /  / __ \  / __ \          /_ <
#  / /_/ / / /_/ / /  __/ (__  ) / /_   / /  / /_/ / / / / /        ___/ /
#  \___\_\ \__,_/  \___/ /____/  \__/  /_/   \____/ /_/ /_/        /____/
#
#  Question 3
###############################################################################
#
# Instructions:
# Make a Python class for a magical oven that can combine ingredients at
# different temperatures to craft special materials.
#
# The oven class should have the methods:
# - add(item) to add an oven to be combined
# - freeze() to freeze the ingredients
# - boil() to boil the ingredients
# - wait() to combine the ingredients with no change in temperature
# - get_output() to get the result
#
# You will need to change the `make_oven()` function to return a new instance
# of your oven.
#
# The `alchemy_combine()` function will use your oven. You can see the expected
# formulas and their outputs in the test file, `question3_test.py`.

# This function should return an oven instance!
def make_oven():
    return oven()


def alchemy_combine(oven, ingredients, temperature):

    for item in ingredients:
        oven.add(item)

    if temperature < 0:
        oven.freeze()
    elif temperature >= 100:
        oven.boil()
    else:
        oven.wait()

    return oven.get_output()


class oven():
    '''
    This is a magical oven that can combine ingredients at different
    temperatures to craft special materials.
    ----------------------------------------
    Methods:
    - add(item) to add an oven to be combined
    - freeze() to freeze the ingredients
    - boil() to boil the ingredients
    - wait() to combine the ingredients with no change in temperature
    - get_output() to get the result
    ----------------------------------------
    variables:
    - ingredients: tuple of ingredients
    - temperature: temperature of the oven
    - result: dictionary of ingredients and their results
    '''
    def __init__(self):
        self.ingredients = ()
        self.temperature = 0
        self.result = {
            ("lead", "mercury"): "gold",
            ("water", "air"): "snow",
            ("cheese", "dough", "tomato"): "pizza"
        }

    def add(self, item):
        '''This function adds an ingredient to the oven'''
        self.ingredients += (item,)

    def freeze(self):
        '''This function freezes the oven'''
        self.temperature = 0

    def boil(self):
        '''This function boils the oven'''
        self.temperature = 100

    def wait(self):
        '''This function waits the oven'''
        pass

    def get_output(self):
        '''This function returns the result of the oven'''
        return self.result.get(self.ingredients, "unknown")
