import random as r


def int_check(msg):
    try:
        user_input = int(input(msg))
    except ValueError:
        return int_check("Wrong format! Try again.\n")
    return user_input


def numbers():
    operators = "+", "-", "*"
    task = f"{r.randint(2, 9)} {r.choice(operators)} {r.randint(2, 9)}"
    return int_check(f"{task}\n") == eval(task)


def squares():
    number = r.randint(11, 29)
    return int_check(f"{number}\n") == number ** 2


def record(name, score, level, description):
    with open("results.txt", "a") as results:
        results.write(f"{name}: {score}/5 in level {level} ({description}).\n")
    return print('The results are saved in "results.txt".')


def main():
    description = {1: "simple operations with numbers 2-9", 2: "integral squares of 11-29"}
    options = {1: "numbers()", 2: "squares()"}
    print("Which level do you want? Enter a number:")
    level = input(f"1 - {description[1]}\n2 - {description[2]}\n")
    score = 0

    if level.isdecimal() and int(level) in options:
        level = int(level)
    else:
        print("Incorrect format.")
        return main()

    for _ in range(5):
        if eval(options[level]):
            score += 1
            print("Right!")
        else:
            print("Wrong!")

    print(f"Your mark is {score}/5. Would you like to save the result? Enter yes or no.\n")
    if input().lower() in ("yes", "y"):
        return record(input("What is your name?\n"), score, level, description[level])


main()
