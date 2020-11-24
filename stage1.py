from utils import say, askchoice, askword
import random


def stage1(player, questions):
    question_number = [i for i in range(1, 11)]
    for round in range(10):
        if player["hp"] == 0:
            say("Game Over!")
            return False
        say("This is level " + str(round + 1))
        if player["hp"] == 1:
            say("You have only 1 HP left")
            if "healing" in player["items"] and player["items"]["healing"] > 0:
                use = askword(["Y", "N"],
                              "You have healing potion in your item portal."
                              " Do you want to use healing potion to heal"
                              " your wond? (Y/N): ")
                if use == "Y":
                    player["items"]["healing"] -= 1
                    player["hp"] += 1
                    say("Congrats! Your HP has been increased!")
                else:
                    say("Try your best to survive! Good luck!!!")
        q = random.randint(0, 1)
        if q:
            random_question = random.choice(question_number)
            question_number.remove(random_question)
            question = questions[str(random_question)]
            solution = question["answer"]
            choices = question["choice"]
            say(question["question"])
            answer = askchoice(choices, "Select a choice(1-4): ")
            if choices[answer - 1] == solution:
                say("Correct! You can go to the next level")
            else:
                player["hp"] -= 1
                say("Wrong! Your HP is " + str(player["hp"]))
        else:
            say("You have to choose left/right")
            direction = random.choice(["left", "right"])
            select = askword(["left", "right"], "(left/right): ")
            if direction == select:
                items = ["healing", "sword", "spear", "dagger", "bowl"]
                player_get = random.choice(items)
                if player_get not in player["items"]:
                    player["items"][player_get] = 1
                else:
                    player["items"][player_get] += 1
                say(player["items"])
            else:
                say("You took the wrong turn, you can go to the next level")
    else:
        return True
