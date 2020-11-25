from utils import say, askchoice, askword
import random


def stage2(player, special_question, question_left):
    question_number = [i for i in range(1, 6)]
    for round in range(question_left):
        if player["hp"] == 0:
            say("NOOO~~ Game Over! T_T You had failed to help Jack survived.")
            return False
        say("This is giant level " + str(round + 1))
        if player["hp"] == 1:
            say("You have only 1 HP left. Try your best to survived!")
            if "healing" in player["items"] and player["items"]["healing"] > 0:
                use = askword(["Y", "N"],
                              "Do you want to use healing potion(Y/N): ")
                if use == "Y":
                    player["items"]["healing"] -= 1
                    player["hp"] += 1
                    say("Congrats! Your HP has been increased!")
                else:
                    say("Good luck!!!")
        random_question = random.choice(question_number)
        question_number.remove(random_question)
        question = special_question[str(random_question)]
        solution = question["answer"]
        choices = question["choice"]
        say(question["question"] + "Choose the right answer to get closer"
            "to the treassure")
        answer = askchoice(choices, "Select a choice(1-4): ")
        if choices[answer - 1] == solution:
            say("Correct! You can go to the next level. Now you are another "
                "step closer to kill the giants!")
        else:
            player["hp"] -= 1
            say("Wrong! You are bleeding!! and Your HP is " + str(player["hp"])
                + "Try to move faster and don't get caught by the giants")
    else:
        return True
