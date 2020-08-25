import random
from flask import Flask, render_template, request, jsonify
from flask_restful import abort

from data.db_session import global_init, create_session
from data.items import Items
from data.quests import Quests

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret_key"

@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """

    print(app.config["DEBUG"])
    if not app.config["DEBUG"]:
        return r

    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r


@app.route("/")
def main_page():
    return render_template("main_page.html")


@app.route("/play")
def play_page():
    session = create_session()
    item = session.query(Items).get(random.randint(1, session.query(Items).count()))
    quest = session.query(Quests).get(random.randint(1, session.query(Quests).count()))
    return render_template("play_page.html", item=item, quest=quest)


# ---------- AJAX ----------

@app.route("/ajax/get-new-card", methods=["POST"])
def get_new_card():
    data = request.get_json()
    try:
        prev_item_id = int(data["previousItemId"])
        prev_quest_id = int(data["previousQuestId"])
    except ValueError:
        abort(400, "Id must be integer")

    session = create_session()

    item_id = excluding_randint(1, session.query(Items).count(), prev_item_id)
    quest_id = excluding_randint(1, session.query(Quests).count(), prev_quest_id)

    item = session.query(Items).get(item_id)
    quest = session.query(Quests).get(quest_id)
    return jsonify({
        "item": item.to_dict(),
        "quest": quest.to_dict()
    })


def excluding_randint(start, end, exclusion):
    if exclusion == start:
        return random.randint(start + 1, end)
    elif exclusion == end:
        return random.randint(start, end - 1)
    try:
        return random.choice((random.randint(start, exclusion - 1),
                            random.randint(exclusion + 1, end)))
    except ValueError:
        return random.randint(start, end)


def main():
    global_init("db/endless_orange.sqlite")
    app.run(port=8080, debug=True, host="192.168.1.77")


if __name__ == "__main__":
    main()
