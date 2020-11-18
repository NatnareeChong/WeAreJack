import time


def say(message):
    time.sleep(0.5)
    print(message)


def askchoice(choices, message=""):
    for idx, choice in enumerate(choices):
        print(str(idx + 1) + ": " + choice)
    while True:
        answer = int(input(message))
        if answer >= 1 and answer <= 4:
            return answer
        else:
            print("Please select a correct choice(1-4)!")


def askword(choices, message=""):
    while True:
        answer = input(message)
        if answer in choices:
            return answer
        else:
            print("Please enter the correct format!" + "(" + "/".join(choices)
                     + ")")
