import random


hand_choices = ["Schere", "Papier", "Stein", "Echse", "Spock"]

def cp_pick_hand():
    return hand_choices[random.randrange(0,4)]


def check_user_win(user_hand, cp_hand):
    if hand_choices.index(user_hand) == hand_choices.index(cp_hand) -1 or hand_choices.index(user_hand) == hand_choices.index(cp_hand) +2:
        return "W"
    else:
        return False


if __name__ == "__main__":
    while(True):
        user = input("Gebe deinen Namen ein")
        user_hand = input("Wähle deinen Hand: Schere, Papier, Stein, Echse, Spock")
        cp_hand = cp_pick_hand()
        if user_hand == cp_hand:
            print("Der Computer hat:" + cp_hand + " gewählt")
            print("Unentschieden")
        if check_user_win(user_hand, cp_hand):
            print("Der Computer hat:" + cp_hand + " gewählt")
            print("Du hast gewonnen!")
        else:
            print("Der Computer hat " + cp_hand + " gewählt")
            print("Du hast leider verloren! :(")