from random import randint
from flask import Flask, render_template
from data.db_session import global_init, create_session
from data.items import Items
from data.quests import Quests

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret_key"


@app.route("/")
def main_page():
    return render_template("main_page.html")


@app.route("/play")
def play_page():
    session = create_session()
    item = session.query(Items).get(randint(1, session.query(Items).count()))
    quest = session.query(Quests).get(randint(1, session.query(Quests).count()))
    return render_template("play_page.html", item=item, quest=quest)


def main():
    global_init("db/endless_orange.sqlite")
    app.run(port=8080, debug=True)


if __name__ == "__main__":
    main()
