import random


def main():
    Quantities = [1, 2]
    Tenses = ["past", "present", "future"]

    for quantity in range(len(Quantities)):
        for tense in range(len(Tenses)):

            determiner = get_determiner(Quantities[quantity])
            
            noun = get_noun(Quantities[quantity])
            
            verb = get_verb(Quantities[quantity], Tenses[tense])

            prepositional_phrase = get_prepositional_phrase(Quantities[quantity])

            print(f"{determiner.capitalize()} {noun} {verb} {prepositional_phrase}.")


def get_determiner(quantity):
    """Return a randomly chosen determiner. A determiner is
    a word like "the", "a", "one", "two", "some", "many".
    If quantity == 1, this function will return either "a",
    "one", or "the". Otherwise this function will return
    either "two", "some", "many", or "the".

    Parameter
        quantity: an integer.
            If quantity == 1, this function will return
            a determiner for a single noun. Otherwise this
            function will return a determiner for a plural noun.
    Return: a randomly chosen determiner.
    """
    if quantity == 1:
        words = ["a", "one", "the"]
    else:
        words = ["two", "some", "many", "the"]

    # Randomly choose and return a determiner.
    word = random.choice(words)
    return word


def get_noun(quantity):
    """Return a randomly chosen noun.
    If quantity == 1, this function will
    return one of these ten single nouns:
        "bird", "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman"
    Otherwise, this function will return one of
    these ten plural nouns:
        "birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"

    Parameter
        quantity: an integer that determines if
            the returned noun is single or plural.
    Return: a randomly chosen noun.
    """
    if quantity == 1:
        words = ["bird", "boy", "car", "cat", "child",\
            "dog", "girl", "man", "rabbit", "woman"]
    else:
        words = ["birds", "boys", "cars", "cats", "children",\
            "dogs", "girls", "men", "rabbits", "women"]

    # Randomly choose and return a noun.
    word = random.choice(words)
    return word


def get_verb(quantity, tense):
    """Return a randomly chosen verb. If tense is "past",
    this function will return one of these ten verbs:
        "drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"
    If tense is "present" and quantity is 1, this
    function will return one of these ten verbs:
        "drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"
    If tense is "present" and quantity is NOT 1,
    this function will return one of these ten verbs:
        "drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"
    If tense is "future", this function will return one of
    these ten verbs:
        "will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"
    Parameters
        quantity: an integer that determines if the
            returned verb is single or plural.
        tense: a string that determines the verb conjugation,
            either "past", "present" or "future".
    Return: a randomly chosen verb.
    """   

    #past tense verbs
    if tense == "past":
        words = ["drank", "ate", "grew", "laughed", "thought",\
            "ran", "slept", "talked", "walked", "wrote"]
    
    #present tense singular verbs
    elif tense == "present" and quantity == 1:
        words = ["drinks", "eats", "grows", "laughs", "thinks",\
        "runs", "sleeps", "talks", "walks", "writes"]

    #present tense plural verbs
    elif tense == "present":
        words = ["drink", "eat", "grow", "laugh", "think",\
            "run", "sleep", "talk", "walk", "write"]

    #future tense verbs
    else:
        words = ["will drink", "will eat", "will grow", "will laugh",\
            "will think", "will run", "will sleep", "will talk",\
            "will walk", "will write"]

    # Randomly choose and return a verb.
    word = random.choice(words)
    return word


def get_preposition():
    """Return a randomly chosen preposition
    from this list of prepositions:
        "about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"

    Return: a randomly chosen preposition.
    """
    #list of all the prepositions
    words = ["about", "above", "across", "after", "along",\
            "around", "at", "before", "behind", "below",\
            "beyond", "by", "despite", "except", "for",\
            "from", "in", "into", "near", "of",\
            "off", "on", "onto", "out", "over",\
            "past", "to", "under", "with", "without"]

    #randomly choose and return a preposition
    word = random.choice(words)
    return word


def get_prepositional_phrase(quantity):
    """Build and return a prepositional phrase composed of three
    words: a preposition, a determiner, and a noun by calling the
    get_preposition, get_determiner, and get_noun functions.

    Parameter
        quantity: an integer that determines if the determiner
            and noun in the prepositional phrase returned from
            this function are single or pluaral.
    Return: a prepositional phrase.
    """
    #retieve the words needed for the prepositional phrase
    preposition = get_preposition()
    determiner = get_determiner(quantity)
    noun = get_noun(quantity)

    #compose the words into phrase and into a string
    prepositional_phrase = f"{preposition} {determiner} {noun}"

    #return the phrase for the main program
    return prepositional_phrase

main()    