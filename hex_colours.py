"""
CP1404/CP5632 Practical
Colour in a dictionary
"""

COLOUR_TO_CODE = {"absolute zero": "#0048ba", "acid green": "#b0bf1a", "aliceblue": "#f0f8ff",
                   "alizarin crimson": "#e32636", "amaranth": "#e52b50", "amber": "#ffbf00",
                   "amethyst": "#9966cc", "antiquewhite": "#faebd7", "antiquewhite1": "#ffefdb",
                   "antiquewhite2": "#eedfcc"}
colour_name = input("Colour Name:").lower()
while colour_name != "":
    print(f"Code of {colour_name} is {COLOUR_TO_CODE.get(colour_name)}")
    colour_name = input("Colour Name:").lower()