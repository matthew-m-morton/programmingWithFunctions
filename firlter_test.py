import csv

# import only system from os
from os import system, name
  
# import sleep to show output for some time period
from time import sleep
  

# Indexes for the weapons_dict
WEAPON_NAME = 0
WEAPON_TYPE = 1
WEAPON_BLUNT = 2
WEAPON_PEIRCE = 3
WEAPON_SLASH = 4
WEAPON_FROST = 5
WEAPON_FIRE = 6
WEAPON_POISON = 7
WEAPON_SPIRIT = 8


def main():
    weapons_dict = make_dict("weapons.csv", 0)
    
    weapon_type = input("Axes\nBows\nClubs\nFists\nKnives\n"\
        "Pickaxes\nPolearms\nSpears\nSwords\n"\
        "What type of weapon are you using?")
    clear()
    weapon_type_dict = {}

    for weapon in weapons_dict:
        if weapon_type.capitalize() == weapons_dict[weapon][WEAPON_TYPE]:
            key = weapons_dict[weapon][WEAPON_NAME]

            weapon_type_dict[key] = weapons_dict[weapon]
        else:
            pass


    print(weapon_type_dict)
    #weapon = (filter(lambda x: x[1] == 'Clubs', weapons_dict))
    #next(weapon)
    #print(weapon)



def damage():
        # Clear terminal to make things less cluttered
    clear()

    weapon_type_dict = sort_weapon_type(weapons_dict, weapon_type.capitalize(), WEAPON_TYPE)

    

    if weapon_type.capitalize() == "Bows":


        list_options(weapon_type_dict)
        bow_type = input("From the list above, What type of bow are you using? ")


        list_options(arrow_dict)
        arrow_type = input("From the list above, What type of arrow are you using? ")


        weapon_damage = calc_bow_damage(weapon_type_dict, arrow_dict, bow_type, arrow_type)


    else:
        list_options(weapon_type_dict)
        weapon = input("From the list above, What type of bow are you using? ")








def make_dict(filename, key_column_index):
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
    # to the opened file in a variable named csv_file.
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


# define our clear function
def clear():
  
    # for windows
    if name == 'nt':
        _ = system('cls')
  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

if __name__ == "__main__":
    main()