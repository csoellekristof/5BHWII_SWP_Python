import json


hand_choices = ["Schere", "Papier", "Stein", "Echse", "Spock"]


def cp_pick_hand(user, userpicks, rounds):

    if user not in userpicks:
        user = "User"

    choices = sorted(userpicks[user], key=userpicks[user].get, reverse=True)
    choices.remove("Gewonnen")
    print(choices)
    most_likely = choices[rounds % 5]


    indexof_mostlikely = hand_choices.index(most_likely)
    beats_1 = hand_choices[indexof_mostlikely - 1]
    beats_2 = hand_choices[(indexof_mostlikely + 2) % 5]
    if (userpicks[user][beats_1] < userpicks[user][beats_2]):
        return beats_1
    else:
        return beats_2

def check_user_win(user_hand, cp_hand):
    if hand_choices.index(user_hand) == hand_choices.index(cp_hand) -1 or hand_choices.index(user_hand) == hand_choices.index(cp_hand) + 2 % 5:
        return True
    else:
        return False

def getUserPicks():
    return requests.get("http://127.0.0.1:5000/getstats").json()

def uploadUserPicks(userpicks, user):
    url = "http://127.0.0.1:5000/putstats"
    senddata = {"user": user, "stats": json.dumps(userpicks[user])}
    return requests.put(url, senddata)

def play():
    userpicks = getUserPicks()
    user = input("Gebe deine Name ein:")
    rounds = 0
    while(True):
        user_hand = input("Wähle deinen Hand: Schere, Papier, Stein, Echse, Spock oder 'quit'")
        if user_hand == "quit":
            exit(0)
        cp_hand = cp_pick_hand(user, userpicks,rounds)
        if user in userpicks.keys():
            userpicks[user][user_hand] = userpicks[user][user_hand] + 1

        else:
            userpicks[user] = {"Gewonnen": 0, "Schere":0, "Papier":0, "Stein":0, "Echse":0, "Spock":0}
            userpicks[user][user_hand] = 1

        userpicks["User"][user_hand] = userpicks["User"][user_hand] + 1

        if user_hand == cp_hand:
            print("Der Computer hat:" + cp_hand + " gewählt")
            print("Unentschieden")
        elif check_user_win(user_hand, cp_hand):
            userpicks[user]["Gewonnen"] += 1
            userpicks["User"]["Gewonnen"] += 1
            print("Der Computer hat:" + cp_hand + " gewählt")
            print("Du hast gewonnen!")
        else:
            print("Der Computer hat " + cp_hand + " gewählt")
            print("Du hast leider verloren! :(")

        rounds += 1
        uploadUserPicks(userpicks, user)



if __name__ == "__main__":
    play()

