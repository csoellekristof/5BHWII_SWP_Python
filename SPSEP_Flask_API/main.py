import json
import secrets
import requests
from flask import Flask, render_template, redirect, request
from flask_restful import Resource, Api

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)
api = Api(app)

def read_userpicks():
    with open("userpicks.txt", "r") as f:
        return json.loads(f.read())

def write_userpicks(userpicks):
    with open("userpicks.txt", "w") as f:
        f.write(json.dumps(userpicks))

@app.route("/")
def home():
    userpicks = read_userpicks()
    return render_template("stats.html",userpicks = userpicks)


class GetStats(Resource):
    def get(self):
        return read_userpicks()

class PutStats(Resource):
    def put(self):
        user = request.form["user"]
        userpicks = read_userpicks()
        userpicks[user] = json.loads(request.form["stats"])
        write_userpicks(userpicks)
        return

api.add_resource(GetStats, "/getstats")
api.add_resource(PutStats, "/putstats")

if __name__ == '__main__':
    app.run()
