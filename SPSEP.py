import random
import json

hand_choices = ["Schere", "Papier", "Stein", "Echse", "Spock"]

def cp_pick_hand():
    return hand_choices[random.randrange(0,4)]

def read_userpicks():
    with open("userpicks.txt", "r") as f:
        return json.loads(f.read())

def write_userpicks(userpicks):
    with open("userpicks.txt", "w") as f:
        f.write(json.dumps(userpicks))


def check_user_win(user_hand, cp_hand):
    if hand_choices.index(user_hand) == hand_choices.index(cp_hand) -1 or hand_choices.index(user_hand) == hand_choices.index(cp_hand) +2:
        return True
    else:
        return False


if __name__ == "__main__":
    userpicks = read_userpicks()
    user = input("Gebe deine Name ein:")
    while(True):
        user_hand = input("Wähle deinen Hand: Schere, Papier, Stein, Echse, Spock")
        cp_hand = cp_pick_hand()
        if user in userpicks.keys():
            userpicks[user][user_hand] = userpicks[user][user_hand] + 1
        else:
            userpicks[user] = {"Gewonnen": 0, "Schere":0, "Papier":0, "Stein":0, "Echse":0, "Spock":0}
            userpicks[user][user_hand] = 1

        if user_hand == cp_hand:
            print("Der Computer hat:" + cp_hand + " gewählt")
            print("Unentschieden")
        elif check_user_win(user_hand, cp_hand):
            userpicks[user]["Gewonnen"] += 1
            print("Der Computer hat:" + cp_hand + " gewählt")
            print("Du hast gewonnen!")
        else:
            print("Der Computer hat " + cp_hand + " gewählt")
            print("Du hast leider verloren! :(")

        write_userpicks(userpicks)