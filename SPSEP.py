import json
import secrets
from flask import Flask, render_template, redirect
from flask_restful import Resource, Api

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)
hand_choices = ["Schere", "Papier", "Stein", "Echse", "Spock"]
api = Api(app)

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



def read_userpicks():
    with open("userpicks.txt", "r") as f:
        return json.loads(f.read())

def write_userpicks(userpicks):
    with open("userpicks.txt", "w") as f:
        f.write(json.dumps(userpicks))


def check_user_win(user_hand, cp_hand):
    if hand_choices.index(user_hand) == hand_choices.index(cp_hand) -1 or hand_choices.index(user_hand) == hand_choices.index(cp_hand) + 2 % 5:
        return True
    else:
        return False
@app.route("/stats")
def home():
    return render_template('stats.html',userpicks = read_userpicks())

@app.route("/")
def play():
    userpicks = read_userpicks()
    user = input("Gebe deine Name ein:")
    rounds = 0
    while(True):
        user_hand = input("Wähle deinen Hand: Schere, Papier, Stein, Echse, Spock oder 'quit'")
        if user_hand == "quit":
            return redirect("/stats", code=302)
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
        write_userpicks(userpicks)


class GetStats(Resource):
    def get(self):
        return read_userpicks()

api.add_resource(GetStats, "/getstats")

if __name__ == "__main__":
    app.run()

