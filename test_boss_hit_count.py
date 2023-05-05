from boss_hit_count import make_dictionary,\
    calc_bow_damage, calc_hits
from pytest import approx
import pytest



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


def test_make_dictionary():
    """Verify the make_dictionary funtion works properly.
    Modeled after the test_make_periodic_table from the
    test_chemestry_2.py"""

    # Create the dictionaries by calling the make_dictionary function
    # and store those dictionaries for testing
    weapons_dict    = make_dictionary("weapons.csv", WEAPON_NAME)
    arrows_dict     = make_dictionary("arrows.csv",  ARROW_NAME)
    bosses_dict     = make_dictionary("bosses.csv",  BOSS_NAME)

    # Verify that the make_dictionary function returns a dictionary
    # When promted to make the weapons dictionary
    assert isinstance(weapons_dict, dict), \
        "make_dictionary function must return a dictionary: " \
        f" expected a dictionary but found a {type(weapons_dict)}"

    # Verify that the make_dictionary function returns a dictionary
    # When promted to make the arrows dictionary
    assert isinstance(arrows_dict, dict), \
        "make_dictionary function must return a dictionary: " \
        f" expected a dictionary but found a {type(arrows_dict)}"

    # Verify that the make_dictionary function returns a dictionary
    # When promted to make the bosses dictionary
    assert isinstance(bosses_dict, dict), \
        "make_dictionary function must return a dictionary: " \
        f" expected a dictionary but found a {type(bosses_dict)}"


    # Check the weapons dictionary and make sure it returns the correct values
    check_weapon(weapons_dict, "stone axe", ['stone axe', 'Axes', '0', '0', '30', '0', '0', '0', '0']) 
    check_weapon(weapons_dict, "flint axe", ['flint axe', 'Axes', '0', '0', '35', '0', '0', '0', '0']) 
    check_weapon(weapons_dict, "bronze axe", ['bronze axe', 'Axes', '0', '0', '55', '0', '0', '0', '0'])
    check_weapon(weapons_dict, "iron axe", ['iron axe', 'Axes', '0', '0', '75', '0', '0', '0', '0'])
    check_weapon(weapons_dict, "blackmetal axe", ['blackmetal axe', 'Axes', '0', '0', '115', '0', '0', '0', '0'])
    check_weapon(weapons_dict, "battleaxe", ['battleaxe', 'Axes', '0', '0', '88', '0', '0', '0', '0'])
    check_weapon(weapons_dict, "crystal battleaxe", ['crystal battleaxe', 'Axes', '0', '0', '108', '0', '0', '0', '30'])
    check_weapon(weapons_dict, "crude bow", ['crude bow', 'Bows', '0', '31', '0', '0', '0', '0', '0'])
    check_weapon(weapons_dict, "finewood bow", ['finewood bow', 'Bows', '0', '41', '0', '0', '0', '0', '0'])
    check_weapon(weapons_dict, "huntsman bow", ['huntsman bow', 'Bows', '0', '51', '0', '0', '0', '0', '0'])
    check_weapon(weapons_dict, "draugr fang", ['draugr fang', 'Bows', '0', '56', '0', '0', '0', '20', '0'])
    check_weapon(weapons_dict, "club", ['club', 'Clubs', '30', '0', '0', '0', '0', '0', '0'])
    check_weapon(weapons_dict, "torch", ['torch', 'Clubs', '4', '0', '0', '0', '15', '0', '0'])
    check_weapon(weapons_dict, "bronze mace", ['bronze mace', 'Clubs', '53', '0', '0', '0', '0', '0', '0'])
    check_weapon(weapons_dict, "iron mace", ['iron mace', 'Clubs', '73', '0', '0', '0', '0', '0', '0'])
    check_weapon(weapons_dict, "frostner", ['frostner', 'Clubs', '35', '0', '0', '58', '0', '0', '20'])
    check_weapon(weapons_dict, "porcupine", ['porcupine', 'Clubs', '50', '63', '0', '0', '0', '0', '0'])
    check_weapon(weapons_dict, "stagbreaker", ['stagbreaker', 'Clubs', '38', '5', '0', '0', '0', '0', '0'])
    check_weapon(weapons_dict, "iron sledge", ['iron sledge', 'Clubs', '73', '0', '0', '0', '0', '0', '0'])
    check_weapon(weapons_dict, "bare fists", ['bare fists', 'Fists', '5', '0', '0', '0', '0', '0', '0'])
    check_weapon(weapons_dict, "flesh rippers", ['flesh rippers', 'Fists', '0', '0', '76', '0', '0', '0', '0'])
    check_weapon(weapons_dict, "flint knife", ['flint knife', 'Knives', '0', '8', '8', '0', '0', '0', '0'])
    check_weapon(weapons_dict, "copper knife", ['copper knife', 'Knives', '0', '15', '15', '0', '0', '0', '0'])
    check_weapon(weapons_dict, "abyssal razor", ['abyssal razor', 'Knives', '0', '23', '23', '0', '0', '0', '0'])
    check_weapon(weapons_dict, "silver knife", ['silver knife', 'Knives', '0', '28', '28', '0', '0', '0', '12'])
    check_weapon(weapons_dict, "blackmetal knife", ['blackmetal knife', 'Knives', '0', '37', '37', '0', '0', '0', '0'])
    check_weapon(weapons_dict, "antler pickaxe", ['antler pickaxe', 'Pickaxes', '0', '18', '0', '0', '0', '0', '0'])
    check_weapon(weapons_dict, "bronze pickaxe", ['bronze pickaxe', 'Pickaxes', '0', '40', '0', '0', '0', '0', '0'])
    check_weapon(weapons_dict, "iron pickaxe", ['iron pickaxe', 'Pickaxes', '0', '48', '0', '0', '0', '0', '0'])
    check_weapon(weapons_dict, "bronze atgeir", ['bronze atgeir', 'Polearms', '0', '63', '0', '0', '0', '0', '0'])
    check_weapon(weapons_dict, "iron atgeir", ['iron atgeir', 'Polearms', '0', '83', '0', '0', '0', '0', '0'])
    check_weapon(weapons_dict, "blackmetal atgeir", ['blackmetal atgeir', 'Polearms', '0', '123', '0', '0', '0', '0', '0'])
    check_weapon(weapons_dict, "flint spear", ['flint spear', 'Spears', '0', '38', '0', '0', '0', '0', '0'])
    check_weapon(weapons_dict, "bronze spear", ['bronze spear', 'Spears', '0', '53', '0', '0', '0', '0', '0'])
    check_weapon(weapons_dict, "abyssal harpoon", ['abyssal harpoon', 'Spears', '0', '10', '0', '0', '0', '0', '0'])
    check_weapon(weapons_dict, "ancient bark spear", ['ancient bark spear', 'Spears', '0', '73', '0', '0', '0', '0', '0'])
    check_weapon(weapons_dict, "fang spear", ['fang spear', 'Spears', '0', '93', '0', '0', '0', '0', '0'])
    check_weapon(weapons_dict, "bronze sword", ['bronze sword', 'Swords', '0', '0', '53', '0', '0', '0', '0'])
    check_weapon(weapons_dict, "iron sword", ['iron sword', 'Swords', '0', '0', '73', '0', '0', '0', '0'])
    check_weapon(weapons_dict, "silver sword", ['silver sword', 'Swords', '0', '0', '93', '0', '0', '0', '45'])
    check_weapon(weapons_dict, "blackmetal sword", ['blackmetal sword', 'Swords', '0', '0', '113', '0', '0', '0', '0'])

    # Check the arrows dictionary and make sure it returns the correct values
    check_arrow(arrows_dict, "wood", ['wood', '22', '0', '0', '0', '0']) 
    check_arrow(arrows_dict, "flinthead", ['flinthead', '27', '0', '0', '0', '0']) 
    check_arrow(arrows_dict, "bronsehead", ['bronsehead', '32', '0', '0', '0', '0'])
    check_arrow(arrows_dict, "ironhead", ['ironhead', '42', '0', '0', '0', '0'])
    check_arrow(arrows_dict, "obsidian", ['obsidian', '52', '0', '0', '0', '0'])
    check_arrow(arrows_dict, "needle", ['needle', '62', '0', '0', '0', '0'])
    check_arrow(arrows_dict, "fire", ['fire', '11', '0', '22', '0', '0'])
    check_arrow(arrows_dict, "poison", ['poison', '26', '0', '0', '20', '0'])
    check_arrow(arrows_dict, "silver", ['silver', '52', '0', '0', '0', '20'])
    check_arrow(arrows_dict, "frost", ['frost', '26', '52', '0', '0', '0'])

    # Check the arrows dictionary and make sure it returns the correct values
    check_boss(bosses_dict, "eikthyr", ['eikthyr', '500', '1.00', '1.00', '1.00', '1.00', '1.00', '1.00', '1.00']) 
    check_boss(bosses_dict, "elder", ['elder', '2500', '1.00', '1.00', '1.00', '1.00', '2.00', '0.00', '0.00']) 
    check_boss(bosses_dict, "bonemass", ['bonemass', '5000', '1.50', '0.25', '0.50', '1.50', '0.25', '0.00', '1.00'])
    check_boss(bosses_dict, "moder", ['moder', '7500', '1.00', '1.00', '1.00', '0.00', '1.50', '1.00', '0.00'])
    check_boss(bosses_dict, "yagluth", ['yagluth', '10000', '1.00', '0.25', '1.00', '1.00', '0.50', '0.00', '1.00'])

def check_weapon(weapons_dict, weapon, expected):
    """Verify that the weapons dictionary contains the expected values.

    Parameters
        weapon: name of the weapon that is used as the dictionary key
        expected: a list that contains the expected values for weapon
    Return: nothing
    """

    # Verify that weapon is in the periodic table dictionary.
    assert weapon in weapons_dict, \
        f'"{weapon}" is missing from the periodic table dictionary.'
    actual = weapons_dict[weapon]

    # Verify that the weapons's name is correct.
    act_name = actual[WEAPON_NAME]
    exp_name = expected[WEAPON_NAME]
    assert act_name == exp_name, \
            f'wrong name for "{weapon}": ' \
            f'expected {exp_name} but found {act_name}'

    # Verify that the weapon's type is correct.
    act_type = actual[WEAPON_TYPE]
    exp_type = expected[WEAPON_TYPE]
    assert act_type == approx(exp_type), \
            f"wrong weapon type for {exp_name}: " \
            f"expected {exp_type} but found {act_type}"

    # Verify that the weapon's blunt damage is correct.
    act_blunt = actual[WEAPON_BLUNT]
    exp_blunt = expected[WEAPON_BLUNT]
    assert act_blunt == approx(exp_blunt), \
            f"wrong amount of blunt damage for {exp_name}: " \
            f"expected {exp_blunt} but found {act_blunt}"    

    # Verify that the weapon's peirce damage is correct.
    act_peirce = actual[WEAPON_PEIRCE]
    exp_peirce = expected[WEAPON_PEIRCE]
    assert act_peirce == approx(exp_peirce), \
            f"wrong amount of peirce damage for {exp_name}: " \
            f"expected {exp_peirce} but found {act_peirce}"

    # Verify that the weapon's slash damage is correct.
    act_slash = actual[WEAPON_SLASH]
    exp_slash = expected[WEAPON_SLASH]
    assert act_slash == approx(exp_slash), \
            f"wrong amount of slash damage for {exp_name}: " \
            f"expected {exp_slash} but found {act_slash}"

    # Verify that the weapon's frost damage is correct.
    act_frost = actual[WEAPON_FROST]
    exp_frost = expected[WEAPON_FROST]
    assert act_frost == approx(exp_frost), \
            f"wrong amount of frost damage for {exp_name}: " \
            f"expected {exp_frost} but found {act_frost}"

    # Verify that the weapon's fire damage is correct.
    act_fire = actual[WEAPON_FIRE]
    exp_fire = expected[WEAPON_FIRE]
    assert act_fire == approx(exp_fire), \
            f"wrong amount of fire damage for {exp_name}: " \
            f"expected {exp_fire} but found {act_fire}"

    # Verify that the weapon's poison damage is correct.
    act_poison = actual[WEAPON_POISON]
    exp_poison = expected[WEAPON_POISON]
    assert act_poison == approx(exp_poison), \
            f"wrong amount of poison damage for {exp_name}: " \
            f"expected {exp_poison} but found {act_poison}"

    # Verify that the weapon's spirit damage is correct.
    act_spirit = actual[WEAPON_SPIRIT]
    exp_spirit = expected[WEAPON_SPIRIT]
    assert act_spirit == approx(exp_spirit), \
            f"wrong amount of spirit damage for {exp_name}: " \
            f"expected {exp_spirit} but found {act_spirit}"

def check_arrow(arrows_dict, arrow, expected):
    """Verify that the arrows dictionary contains the expected values.

    Parameters
        arrow: name of the arrow that is used as the dictionary key
        expected: a list that contains the expected values for arrow
    Return: nothing
    """

    # Verify that arrow is in the periodic table dictionary.
    assert arrow in arrows_dict, \
        f'"{arrow}" is missing from the periodic table dictionary.'
    actual = arrows_dict[arrow]

    # Verify that the arrows's name is correct.
    act_name = actual[ARROW_NAME]
    exp_name = expected[ARROW_NAME]
    assert act_name == exp_name, \
            f'wrong name for "{arrow}": ' \
            f'expected {exp_name} but found {act_name}'

    # Verify that the arrow's peirce damage is correct.
    act_peirce = actual[ARROW_PIERCE]
    exp_peirce = expected[ARROW_PIERCE]
    assert act_peirce == approx(exp_peirce), \
            f"wrong amount of peirce damage for {exp_name}: " \
            f"expected {exp_peirce} but found {act_peirce}"

    # Verify that the arrow's frost damage is correct.
    act_frost = actual[ARROW_FROST]
    exp_frost = expected[ARROW_FROST]
    assert act_frost == approx(exp_frost), \
            f"wrong amount of frost damage for {exp_name}: " \
            f"expected {exp_frost} but found {act_frost}"

    # Verify that the arrow's fire damage is correct.
    act_fire = actual[ARROW_FIRE]
    exp_fire = expected[ARROW_FIRE]
    assert act_fire == approx(exp_fire), \
            f"wrong amount of fire damage for {exp_name}: " \
            f"expected {exp_fire} but found {act_fire}"

    # Verify that the arrow's poison damage is correct.
    act_poison = actual[ARROW_POISON]
    exp_poison = expected[ARROW_POISON]
    assert act_poison == approx(exp_poison), \
            f"wrong amount of poison damage for {exp_name}: " \
            f"expected {exp_poison} but found {act_poison}"

    # Verify that the arrow's spirit damage is correct.
    act_spirit = actual[ARROW_SPIRIT]
    exp_spirit = expected[ARROW_SPIRIT]
    assert act_spirit == approx(exp_spirit), \
            f"wrong amount of spirit damage for {exp_name}: " \
            f"expected {exp_spirit} but found {act_spirit}"

def check_boss(bosses_dict, boss, expected):
    """Verify that the bosses dictionary contains the expected values.

    Parameters
        boss: name of the boss that is used as the dictionary key
        expected: a list that contains the expected values for boss
    Return: nothing
    """

    # Verify that boss is in the periodic table dictionary.
    assert boss in bosses_dict, \
        f'"{boss}" is missing from the periodic table dictionary.'
    actual = bosses_dict[boss]

    # Verify that the bosss's name is correct.
    act_name = actual[BOSS_NAME]
    exp_name = expected[BOSS_NAME]
    assert act_name == exp_name, \
            f'wrong name for "{boss}": ' \
            f'expected {exp_name} but found {act_name}'

    # Verify that the boss's hp is correct.
    act_hp = actual[BOSS_HP]
    exp_hp = expected[BOSS_HP]
    assert act_hp == approx(exp_hp), \
            f"wrong boss hp for {exp_name}: " \
            f"expected {exp_hp} but found {act_hp}"

    # Verify that the boss's blunt resistance is correct.
    act_blunt = actual[BOSS_BLUNT_RESIST]
    exp_blunt = expected[BOSS_BLUNT_RESIST]
    assert act_blunt == approx(exp_blunt), \
            f"wrong amount of blunt resistance for {exp_name}: " \
            f"expected {exp_blunt} but found {act_blunt}"    

    # Verify that the boss's peirce resistance is correct.
    act_peirce = actual[BOSS_PIERCE_RESIST]
    exp_peirce = expected[BOSS_PIERCE_RESIST]
    assert act_peirce == approx(exp_peirce), \
            f"wrong amount of peirce resistance for {exp_name}: " \
            f"expected {exp_peirce} but found {act_peirce}"

    # Verify that the boss's slash resistance is correct.
    act_slash = actual[BOSS_SLASH_RESIST]
    exp_slash = expected[BOSS_SLASH_RESIST]
    assert act_slash == approx(exp_slash), \
            f"wrong amount of slash resistance for {exp_name}: " \
            f"expected {exp_slash} but found {act_slash}"

    # Verify that the boss's frost resistance is correct.
    act_frost = actual[BOSS_FROST_RESIST]
    exp_frost = expected[BOSS_FROST_RESIST]
    assert act_frost == approx(exp_frost), \
            f"wrong amount of frost resistance for {exp_name}: " \
            f"expected {exp_frost} but found {act_frost}"

    # Verify that the boss's fire resistance is correct.
    act_fire = actual[BOSS_FIRE_RESIST]
    exp_fire = expected[BOSS_FIRE_RESIST]
    assert act_fire == approx(exp_fire), \
            f"wrong amount of fire resistance for {exp_name}: " \
            f"expected {exp_fire} but found {act_fire}"

    # Verify that the boss's poison resistance is correct.
    act_poison = actual[BOSS_POISON_RESIST]
    exp_poison = expected[BOSS_POISON_RESIST]
    assert act_poison == approx(exp_poison), \
            f"wrong amount of poison resistance for {exp_name}: " \
            f"expected {exp_poison} but found {act_poison}"

    # Verify that the boss's spirit resistance is correct.
    act_spirit = actual[BOSS_SPIRIT_RESIST]
    exp_spirit = expected[BOSS_SPIRIT_RESIST]
    assert act_spirit == approx(exp_spirit), \
            f"wrong amount of spirit resistance for {exp_name}: " \
            f"expected {exp_spirit} but found {act_spirit}"

def test_calc_bow_damage():
    weapons_dict    = make_dictionary("weapons.csv", WEAPON_NAME)
    arrows_dict     = make_dictionary("arrows.csv",  ARROW_NAME)

    # Verify that the make_dictionary function returns a dictionary
    # When promted to make the weapons dictionary
    assert isinstance(weapons_dict, dict), \
        "make_dictionary function must return a dictionary: " \
        f" expected a dictionary but found a {type(weapons_dict)}"

    # Verify that the make_dictionary function returns a dictionary
    # When promted to make the arrows dictionary
    assert isinstance(arrows_dict, dict), \
        "make_dictionary function must return a dictionary: " \
        f" expected a dictionary but found a {type(arrows_dict)}"

    # Various assertions to test the addition of damage values when 
    # utilizing the calc_bow_damage function
    assert calc_bow_damage(weapons_dict, arrows_dict, 'finewood bow', 'silver') \
        == ['finewood bow with silver arrows','Bows', 0, 93, 0, 0, 0, 0, 20]
    assert calc_bow_damage(weapons_dict, arrows_dict, 'crude bow', 'frost') \
        == ['crude bow with frost arrows','Bows', 0, 57, 0, 52, 0, 0, 0]
    assert calc_bow_damage(weapons_dict, arrows_dict, 'huntsman bow', 'obsidian') \
        == ['huntsman bow with obsidian arrows','Bows', 0, 103, 0, 0, 0, 0, 0]
    assert calc_bow_damage(weapons_dict, arrows_dict, 'draugr fang', 'fire') \
        == ['draugr fang with fire arrows','Bows', 0, 67, 0, 0, 22, 20, 0]

def test_calc_hits():
    # assertions made to test the calc_hits function
    assert calc_hits(['club', 'Clubs', '30', '0', '0', '0', '0', '0', '0'],\
            ['eikthyr', '500', '1.00', '1.00', '1.00', '1.00', '1.00', '1.00', '1.00'])\
            == approx(16.66667)
    assert calc_hits(['draugr fang and fire arrows', 'Bows', '0', '67', '0', '0', '22', '20', '0'],\
            ['elder', '2500', '1.00', '1.00', '1.00', '1.00', '2.00', '0.00', '0.00'])\
            == approx(22.52252)
    assert calc_hits(['blackmetal sword', 'Swords', '0', '0', '113', '0', '0', '0', '0'],\
            ['bonemass', '5000', '1.50', '0.25', '0.50', '1.50', '0.25', '0.00', '1.00'])\
            == approx(88.4956)

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])
