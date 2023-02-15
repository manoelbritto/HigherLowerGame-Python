import art
from game_data import data
import random as rd

start_score = 0


def select_question(position):
    """function that return the question"""
    question = data[position]['name'] + ", " + data[position]['description'] + ", " + data[position]['country']
    return question


def get_score(position):
    """function that return score position on from the list"""
    score = data[position]['follower_count']
    return score


def track_score(value):
    """function that track the game score"""
    global start_score
    start_score += value
    if start_score > 0:
        print(f"You were right, your score is {start_score}")


def game():
    start_game = 0
    continue_game = True
    print(art.logo)
    while continue_game:
        track_score(start_game)
        question_first = rd.randint(0, 49)
        question_second = rd.randint(0, 49)
        while question_first == question_second:
            question_first = rd.randint(0, 49)
        print(f"Option A: {select_question(question_first)}")
        score_first = get_score(question_first)
        print(score_first)
        print(art.vs)
        print(f"Option B: {select_question(question_second)}")
        score_second = get_score(question_second)
        print (score_second)

        option = input("What is your option A or B? ").lower()

        if option == 'a':
            if score_first > score_second:
                start_game = 1
            else:
                print(f"You lose \nYour score was {track_score(start_game)}")
                continue_game = False
        else:
            if score_first < score_second:
                start_game = 1
            else:
                print(f"You lose \nYour score was {track_score(start_game)}")

                continue_game = False


game()
