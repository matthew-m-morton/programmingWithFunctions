"""This program is designed so players of the video game "Valheim"
can calculate how many hits it will take to kill a chosen boss with
their chosen weapon. Then based on how many hits, advice will be given 
to help in the battle."""

# Import the system so that the terminal commands can be entered
# specifically so that the terminal can be cleared periodically.
# It is also built into python so no need to look for it.
from os import system, name

# Import csv so that csv files can be read.
import csv


# Indexes for the weapons_dict and type_weapons_dict
WEAPON_NAME = 0
WEAPON_TYPE = 1
WEAPON_BLUNT = 2
WEAPON_PEIRCE = 3
WEAPON_SLASH = 4
WEAPON_FROST = 5
WEAPON_FIRE = 6
WEAPON_POISON = 7
WEAPON_SPIRIT = 8

# Indexes for the arrow_dict
ARROW_NAME = 0
ARROW_PIERCE = 1
ARROW_FROST = 2
ARROW_FIRE = 3
ARROW_POISON = 4
ARROW_SPIRIT = 5

# Indexes for boss_dictionary
BOSS_NAME = 0
BOSS_HP = 1
BOSS_BLUNT_RESIST = 2
BOSS_PIERCE_RESIST = 3
BOSS_SLASH_RESIST = 4
BOSS_FROST_RESIST = 5
BOSS_FIRE_RESIST = 6
BOSS_POISON_RESIST = 7
BOSS_SPIRIT_RESIST = 8


def main():
    """The main function that uses other functions to calculate how many 
    hits it takes to kill a specific boss with the chosen weapon."""

    # Clear terminal to make things less cluttered
    clear()

    # Make dictionaries for weapons, arrow types and Bosses 
    weapons_dict    = make_dictionary("weapons.csv", WEAPON_NAME)
    arrow_dict      = make_dictionary("arrows.csv",  ARROW_NAME)
    boss_dict       = make_dictionary("bosses.csv",  BOSS_NAME)

    # Ask for type of weapon after giving a list of options
    weapon_type = ask_weapon_type()

    # Clear terminal to make things less cluttered
    clear()

    # Utilizes the calc_damage function to create a variable that is the  list of 
    # damage values for use in the calc_hits function and the final_print function
    weapon_damage = calc_damage(weapons_dict, arrow_dict, weapon_type.capitalize())

    # Clear terminal to make things less cluttered
    clear()

    # Utilizes the boss_select function to create a variable
    # that is the list of boss stats for the selected boss
    # for use in the calc_hits function and the final_print function
    boss = boss_select(boss_dict)

    # Clear terminal to make things less cluttered
    clear()

    # Utilizes the calc_hits function to create a variable that represents
    # how many hits are required to kill the given boss with the given specific
    # weapon. It exists for use in the final_print function
    total_hits = calc_hits(weapon_damage, boss)

    # Runs the Final_print function that takes the total_hits, boss, and weapon_damage
    # variables and prints information related to to the variables. 
    final_print(total_hits, boss, weapon_damage)

def ask_weapon_type():
    # Program made to ask the first question. 
    # Speciffically made to reduce the size of the main function
    type = input("Axes\nBows\nClubs\nFists\nKnives\n"\
        "Pickaxes\nPolearms\nSpears\nSwords\n"\
        "From the list above, What type of weapon will you be using? ")
    return type
   
def sort_weapon_type(dictionary, type, TYPE_INDEX):
    #create new shorter dictionary
    new_dictionary = {}

    # For loop that goes through the given dictionary
    for item in dictionary:

        # If statement that tests the given dictionary and if the type variable
        # matches the type field then the dictionary entry is copied to the new 
        # dictionary
        if type == dictionary[item][TYPE_INDEX]:
            key = dictionary[item][0]

            new_dictionary[key] = dictionary[item]
        
        else:
            pass


    return new_dictionary

def calc_bow_damage(bows_dict, arrow_dict, bow, arrow):
    """Retrieve values from the bows dictionary and arrows dictionary. Using those 
    values creates a list for the combined damage values and returns that list"""

    blunt   = int(bows_dict[bow][WEAPON_BLUNT]) 
    peirce  = int(bows_dict[bow][WEAPON_PEIRCE]) + int(arrow_dict[arrow][ARROW_PIERCE])
    slash   = int(bows_dict[bow][WEAPON_SLASH])
    frost   = int(bows_dict[bow][WEAPON_FROST])  + int(arrow_dict[arrow][ARROW_FROST])
    fire    = int(bows_dict[bow][WEAPON_FIRE])   + int(arrow_dict[arrow][ARROW_FIRE])
    poison  = int(bows_dict[bow][WEAPON_POISON]) + int(arrow_dict[arrow][ARROW_POISON])
    spirit  = int(bows_dict[bow][WEAPON_SPIRIT]) + int(arrow_dict[arrow][ARROW_SPIRIT])

    temp_list = [f"{bow} with {arrow} arrows","Bows", blunt, peirce, slash, frost, fire, poison, spirit ]
    return temp_list

def calc_damage(weapons_dict, arrow_dict, weapon_type):

    # creates a new shorter dictionary.
    weapon_type_dict = sort_weapon_type(weapons_dict, weapon_type, WEAPON_TYPE)


    # If statement used to separate the bows from the other weapons.
    # This is done because the bow damage has to be added to the arrow damage.
    if weapon_type == "Bows":

        list_options(weapon_type_dict)
        bow_type = input("From the list above, What type of bow are you using? ")

        # Clear terminal to make things less cluttered
        clear()        
    
        # Lists the options for arrows and asks user to choose an arrow type from the list
        list_options(arrow_dict)
        arrow_type = input("From the list above, What type of arrow are you using? ")

        # Calculates the weapon damage using the calc_bow_damage function 
        weapon_damage = calc_bow_damage(weapon_type_dict, arrow_dict, bow_type.lower(), arrow_type.lower())

    else:
        # Lists the options from the weapon_type_dict and then procedes to ask
        # the user which weapon fron the list they are using
        list_options(weapon_type_dict)
        weapon = input("From the list above, Which weapon are you using? ")

        # Assigns the weapon_damage variable to the dictionary value 
        # corrisponding to the key that matches the chosen weapon  
        weapon_damage = weapon_type_dict[weapon.lower()]

    return weapon_damage

def boss_select(boss_dict):
    """This function's purpose is to list the bosses using the list options function.
    Then ask the user for which boss they are going to fight and then return the value
    of the corrisponding key from the dictionary."""

    list_options(boss_dict)
    boss_name = input("From the list above, which Boss are you planning to fight? ")
    boss = boss_dict[boss_name]

    return boss

def calc_hits(weapon_damage,boss):
    """The purpose of this function is to take the two lists for the boss and the weapon
    and calculate how many hits it takes to kill the boss.
    
    This is done by taking the weapon damage of each damage type and multipling it by the 
    bosses corrisponding damage resistance. Then you add all  of those values up to get
    the total damage per hit. Then you take the bosses HP and divide it by the damage per 
    hit.
    
    Finally it returns the number of hits needed to kill the boss."""
    
    blunt   = int(weapon_damage[WEAPON_BLUNT])   * float(boss[BOSS_BLUNT_RESIST])
    peirce  = int(weapon_damage[WEAPON_PEIRCE])  * float(boss[BOSS_PIERCE_RESIST])
    slash   = int(weapon_damage[WEAPON_SLASH])   * float(boss[BOSS_SLASH_RESIST])
    frost   = int(weapon_damage[WEAPON_FROST])   * float(boss[BOSS_FROST_RESIST])
    fire    = int(weapon_damage[WEAPON_FIRE])    * float(boss[BOSS_FIRE_RESIST])
    poison  = int(weapon_damage[WEAPON_POISON])  * float(boss[BOSS_POISON_RESIST])
    spirit  = int(weapon_damage[WEAPON_SPIRIT])  * float(boss[BOSS_SPIRIT_RESIST])
    damage_per_hit = blunt + peirce + slash + frost + fire + poison + spirit

    hits = float(boss[BOSS_HP]) / float(damage_per_hit)

    return hits

def final_print(total_hits, boss, weapon_damage):
    """ Print results of calculations followed by advice for player 
        based on number of hits required to defeat the boss.""" 
    
    # Spacing to make things look nice
    print("\n")

    # Main print based on results of calculations 
    print(f"It will take {total_hits:.01f} hits to kill {boss[BOSS_NAME]} with a {weapon_damage[WEAPON_NAME]}\n")

    # If statement giving advice based on how many hits are required to kill boss
    if total_hits < 10:
        print("that should be super easy maybe try it with your eyes closed")
    
    elif total_hits >= 10 and total_hits < 25:
        print(f"{boss[BOSS_NAME]} is probably shaking in his boots.")

    elif total_hits >= 25 and total_hits < 30:
        print(f"You've got this in the bag.")

    elif total_hits >= 30 and total_hits < 40:    
        print("Shouldn't be terrible just look for good openings.")

    elif total_hits >= 50 and total_hits < 60:
        print(f"Might be a longer fight. Make sure to keep an eye on your food")

    elif total_hits >= 60 and total_hits < 80:
        print(f"Manageable. Having friends help can make the fight go faster."\
            "\nWatch your food. Don't get greedy, back off and heal if you need.")

    elif total_hits >= 80 and total_hits < 110:
        print(f"Help from friends is advised, Watch your food."\
            "\nDon't get greedy. Back off and heal if you need."\
            "\nGood Luck.")

    elif total_hits >= 110 and total_hits < 150:
        print(f"This is going to be a very long battle. Make sure you have plenty of food."\
            "\nHaving friends help is highly recommended. "\
            "\n\nMaybe look for a weapon better suited for this boss.")

    else:
        print("This fight is not advised. You should probably choose a different weapon.")

    # Spacing to make things look nice
    print("\n\n")

def make_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    # This function has been adapted from 
    # example 5 from the 09 prepare section

    # Create an empty dictionary that will
    # store the data from the CSV file.
    dictionary = {}

    # Open the CSV file for reading and store a reference
    # to the opened file in a type named csv_file.
    with open(filename, "rt") as csv_file:

        # Use the csv module to create a reader object
        # that will read from the opened CSV file.
        reader = csv.reader(csv_file)

        # The first row of the CSV file contains column
        # headings and not data, so this statement skips
        # the first row of the CSV file.
        next(reader)

        # Read the rows in the CSV file one row at a time.
        # The reader object returns each row as a list.
        for row_list in reader:

            # From the current row, retrieve the data
            # from the column that contains the key.
            key = row_list[key_column_index]

            # Store the data from the current row
            # into the dictionary.
            dictionary[key] = row_list

    # Return the dictionary.
    return dictionary

def list_options(dictionary):
    """Runs through the dictionary and prints the dictionary key"""

    for item in dictionary:
        print(item)

def clear():
    """Made to clear the teminal to reduce the chance of confusion.
    learned at geeksforgeeks.org"""
    # For windows
    if name == 'nt':
        _ = system('cls')
  
    # For mac and linux
    else:
        _ = system('clear')

if __name__ == "__main__":
    main()