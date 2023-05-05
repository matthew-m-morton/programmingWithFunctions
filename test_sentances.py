from sentances import get_determiner, get_noun, get_verb, get_preposition, get_prepositional_phrase
import random
import pytest


def test_get_determiner():
    # 1. Test the single determiners.

    single_determiners = ["a", "one", "the"]

    # This loop will repeat the statements inside it 4 times.
    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a single determiner.
        word = get_determiner(1)

        # Verify that the word returned from get_determiner
        # is one of the words in the single_determiners list.
        assert word in single_determiners

    # 2. Test the plural determiners.

    plural_determiners = ["two", "some", "many", "the"]

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):

        # Get a random number between 2 and 10 inclusive.
        quantity = random.randint(2, 11)

        # Call the get_determiner function which
        # should return a plural determiner.
        word = get_determiner(quantity)

        # Verify that the word returned from get_determiner
        # is one of the words in the plural_determiners list.
        assert word in plural_determiners
    

def test_get_noun():
    # 1. Test the single nouns.

    single_nouns = ["bird", "boy", "car", "cat", "child",\
            "dog", "girl", "man", "rabbit", "woman"]

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):

        # Call the get_noun function which
        # should return a single noun.
        word = get_noun(1)

        # Verify that the word returned from get_noun
        # is one of the words in the single_nouns list.
        assert word in single_nouns

    # 2. Test the plural nouns.

    plural_nouns = ["birds", "boys", "cars", "cats", "children",\
            "dogs", "girls", "men", "rabbits", "women"]

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):

        # Get a random number between 2 and 10 inclusive.
        quantity = random.randint(2, 11)

        # Call the get_determiner function which
        # should return a plural determiner.
        word = get_noun(quantity)

        # Verify that the word returned from get_determiner
        # is one of the words in the plural_determiners list.
        assert word in plural_nouns
    

def test_get_verb():
    # 1. Test the past tense verbs.

    past_verb = ["drank", "ate", "grew", "laughed", "thought",\
            "ran", "slept", "talked", "walked", "wrote"]

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):

        # Call the get_verb function which
        # should return a past tense verb.
        word = get_verb(1, "past")

        # Verify that the word returned from get_verb
        # is one of the words in the past_verb list.
        assert word in past_verb


    # 2. Test the present tense singular verbs.

    present_singlular_verb = ["drinks", "eats", "grows", "laughs", "thinks",\
        "runs", "sleeps", "talks", "walks", "writes"]

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):

        # Call the get_verb function which
        # should return a present tense singular verb.
        word = get_verb(1, "present")

        # Verify that the word returned from get_verb
        # is one of the words in the present_singular_verb list.
        assert word in present_singlular_verb
    

    # 3. Test the present tense plural verbs.

    present_plural_verb = ["drink", "eat", "grow", "laugh", "think",\
            "run", "sleep", "talk", "walk", "write"]

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):

        # Get a random number between 2 and 10 inclusive.
        quantity = random.randint(2, 11)

        # Call the get_verb function which
        # should return a present tense plural verb.
        word = get_verb(quantity, "present")

        # Verify that the word returned from get_verb
        # is one of the words in the present_plural_verb list.
        assert word in present_plural_verb


    # 4. Test the future tense verbs.

    future_verb = ["will drink", "will eat", "will grow", "will laugh",\
            "will think", "will run", "will sleep", "will talk",\
            "will walk", "will write"]

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):

        # Call the get_verb function which
        # should return a future tense verb.
        word = get_verb(1, "future")

        # Verify that the word returned from get_verb
        # is one of the words in the future_verb list.
        assert word in future_verb


def test_get_preposition():
    # Test the prepositions.

    prepositions = ["about", "above", "across", "after", "along",\
            "around", "at", "before", "behind", "below",\
            "beyond", "by", "despite", "except", "for",\
            "from", "in", "into", "near", "of",\
            "off", "on", "onto", "out", "over",\
            "past", "to", "under", "with", "without"]

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):

        # Call the get_preposition function which
        # should return a preposition.
        word = get_preposition()

        # Verify that the word returned from get_preposition
        # is one of the words in the prepositions list.
        assert word in prepositions


def test_get_preposition_phrase():
    #1. Test the singular prepositional phrase
    
    #get sigular phrase and but the words into a list
    prep_phrase = get_prepositional_phrase(1)
    words = prep_phrase.split(' ')

    #for loop to test each of the words in the words list
    for i in range(len(words)):
        
        #test preposition part of the prepositional phrase
        if i == 0:
            prepositions = ["about", "above", "across", "after", "along",\
            "around", "at", "before", "behind", "below",\
            "beyond", "by", "despite", "except", "for",\
            "from", "in", "into", "near", "of",\
            "off", "on", "onto", "out", "over",\
            "past", "to", "under", "with", "without"]

            assert words[i] in prepositions

        #test the determiner part of the prepositional phrase
        elif i == 1:
            single_determiners = ["a", "one", "the"]

            assert words[i] in single_determiners

        #test the determiner part of the prepositional phrase
        elif i == 2:
            single_nouns = ["bird", "boy", "car", "cat", "child",\
            "dog", "girl", "man", "rabbit", "woman"]

            assert words[i] in single_nouns

    #2. Test the plural prepositional phrase
    
    #get plural phrase and but the words into a list
    prep_phrase = get_prepositional_phrase(2)
    words = prep_phrase.split(' ')

    #for loop to test each of the words in the words list
    for i in range(len(words)):
        
        #test preposition part of the prepositional phrase
        if i == 0:
            prepositions = ["about", "above", "across", "after", "along",\
            "around", "at", "before", "behind", "below",\
            "beyond", "by", "despite", "except", "for",\
            "from", "in", "into", "near", "of",\
            "off", "on", "onto", "out", "over",\
            "past", "to", "under", "with", "without"]

            assert words[i] in prepositions

        #test the determiner part of the prepositional phrase
        elif i == 1:
            plural_determiners = ["two", "some", "many", "the"]

            assert words[i] in plural_determiners

        #test the determiner part of the prepositional phrase
        elif i == 2:
            plural_nouns = ["birds", "boys", "cars", "cats", "children",\
            "dogs", "girls", "men", "rabbits", "women"]

            assert words[i] in plural_nouns


# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])