import sys
from random import randint
from pathlib import Path

MIN_GUESS_NUMBER = 1
MAX_GUESS_NUMBER = 100
DATA_DIR_NAME = ".data"
SCORES_FILE_NAME = "scores.txt"


def game_intro():
    print("Guess the Number!")


def read_guess() -> int:
    while True:
        try:
            guess_str = input(
                "Enter your guess (%d - %d): " % (MIN_GUESS_NUMBER, MAX_GUESS_NUMBER)
            )
            guess = int(guess_str)
            return guess
        except ValueError:
            continue
        except KeyboardInterrupt:
            print("\n")
            sys.exit()


def check_guess(guess: int, secret: int, attempts: int):
    if guess < secret:
        print("Too small!")
        return False
    elif guess > secret:
        print("Too big!")
        return False
    else:
        print("You win in %d attempts!\n" % attempts)
        return True


def greet_highscore():
    print("Highscore !!\n")


def read_scores():
    data_dir = Path(DATA_DIR_NAME)
    scores_file = data_dir / SCORES_FILE_NAME

    if not scores_file.is_file():
        yield 0

    with open(scores_file, "r") as file:
        for line in file:
            yield int(line)


def save_score(score: int):
    data_dir = Path(DATA_DIR_NAME)
    scores_file = data_dir / SCORES_FILE_NAME

    if not data_dir.exists():
        data_dir.mkdir(parents=True)

    with open(scores_file, "a") as scores:
        scores.write("%s\n" % score)


def is_least_attempts(current_attempts: int):
    for attempts in read_scores():
        if current_attempts >= attempts:
            return False
    return True


def main():
    secret = randint(MIN_GUESS_NUMBER, MAX_GUESS_NUMBER)
    attempts = 0

    game_intro()

    while True:
        attempts += 1
        guess = read_guess()
        is_guess_correct = check_guess(guess, secret, attempts)

        if not is_guess_correct:
            continue

        if is_least_attempts(attempts):
            greet_highscore()

        save_score(attempts)
        break


if __name__ == "__main__":
    main()
