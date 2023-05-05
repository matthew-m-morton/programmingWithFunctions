def main():


    questions = ['I feel that I am a person of worth, at least on an equal plane with others.',\
        'I feel that I have a number of good qualities.','All in all, I am inclined to feel that I am a failure.',\
        'I am able to do things as well as most other people.','I feel I do not have much to be proud of.',\
        'take a positive attitude toward myself.','On the whole, I am satisfied with myself.',\
        'I wish I could have more respect for myself.',\
        'I certainly feel useless at times.','At times I think I am no good at all.']


    print("""
    This program is an implementation of the Rosenberg
    Self-Esteem Scale. This program will show you ten
    statements that you could possibly apply to yourself.
    Please rate how much you agree with each of the
    statements by responding with one of these four letters:
    
    D means you strongly disagree with the statement.
    d means you disagree with the statement.
    a means you agree with the statement.
    A means you strongly agree with the statement.""")

    user_rating = determine_rating(questions)
    print(f"Your score is {user_rating}")
    print("A score below 15 may indicate problematic low self-esteem.")

def determine_rating(list):
    score = 0
    for i in range(len(list)):
        print(list[i])
       
        if i == 0 or i == 1 or i == 3 or i == 5 or i == 6:
            rating = rating_positive()
        else:
            rating = rating_negative()
        score += rating
    return score


def rating_positive():
    opinion = input("Enter D, d, a, or A: ")
    if opinion == "D":
        return 0
    elif opinion == "d":
        return 1
    elif opinion == "a":
        return 2
    elif opinion == "A":
        return 3

def rating_negative():
    opinion = input("Enter D, d, a, or A: ")
    if opinion == "D":
        return 3
    elif opinion == "d":
        return 2
    elif opinion == "a":
        return 1
    elif opinion == "A":
        return 0

main()