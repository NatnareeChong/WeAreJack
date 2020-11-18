from utils import say, askchoice, askword
import random


def stage2(player, special_question, question_left):
    question_number = [i for i in range(1, 6)]
    for round in range(question_left):
        if player["hp"] == 0:
            say("Game Over!")
            return False
        say("This is giant level " + str(round + 1))
        if player["hp"] == 1:
            say("You have only 1 HP left")
            if "healing" in player["items"] and player["items"]["healing"] > 0:
                use = askword(["Y", "N"],
                              "Do you want to use healing potion(Y/N): ")
                if use == "Y":
                    player["items"]["healing"] -= 1
                    player["hp"] += 1
                    say("Congrats! Your HP has been increased!")
                else:
                    say("Good luck!!!")

    else:
        return True
