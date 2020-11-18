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

    else:
        return True
