import os
import random
from flask import Flask, render_template, request, jsonify, make_response
from flask_restful import abort
from werkzeug.utils import redirect

from data.db_session import global_init, create_session
from data.items import Items
from data.quests import Quests
from forms.endless_orange_settings import EndlessOrangeSettingsForm
from forms.third_wheel_settings import ThirdWheelSettingsForm

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "secret_key_123")

global_init("db/endless_orange.sqlite")


@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """

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


@app.route("/settings", methods=["GET", "POST"])
def settings_page():
    third_wheel_settings = ThirdWheelSettingsForm()
    endless_orange_settings = EndlessOrangeSettingsForm()
    if request.method == "POST":
        # Сохраняем введенные настройки в куки и перенаправляем на страницу игры
        if request.form.get("mode", None) == "third-wheel" and third_wheel_settings.validate_on_submit():
            response = make_response(redirect("/play"))
            response.set_cookie("mode", third_wheel_settings.mode.data, max_age=86400*365)
            response.set_cookie("level", str(third_wheel_settings.level.data), max_age=86400*365)
            return response
        elif request.form.get("mode", None) == "endless-orange" and endless_orange_settings.validate_on_submit():
            response = make_response(redirect("/play"))
            response.set_cookie("mode", endless_orange_settings.mode.data, max_age=86400*365)
            response.set_cookie("time", str(endless_orange_settings.time.data), max_age=86400*365)
            response.set_cookie("rounds", str(endless_orange_settings.rounds.data), max_age=86400*365)
            response.set_cookie("question_type", endless_orange_settings.question_type.data, max_age=86400*365)
            response.set_cookie("communication_type", endless_orange_settings.communication_type.data, max_age=86400*365)
            return response
        else:
            return redirect("settings")

    params = {
        "third_wheel_settings": third_wheel_settings,
        "endless_orange_settings": endless_orange_settings,
        "cookies": request.cookies
    }

    return render_template("settings_page.html", **params)


@app.route("/play")
def play_page():
    session = create_session()
    mode = request.cookies.get("mode", "third-wheel")
    if mode == "third-wheel":
        try:
            items = list(map(lambda x: session.query(Items).get(x),
                             random.sample(range(1, session.query(Items).count()),
                                            int(request.cookies.get("level", 1)) + 1)))
        except ValueError:
            abort(400, "Level must be integer")
        return render_template("third_wheel.html", items=items)
    elif mode == "endless-orange":
        item = session.query(Items).get(random.randint(1, session.query(Items).count()))
        quest = session.query(Quests).get(random.randint(1, session.query(Quests).count()))
        return render_template("endless_orange.html", item=item, quest=quest)
    else:
        abort(400, "Unknown game mode")


# ---------- AJAX ----------

@app.route("/ajax/get-new-card", methods=["POST"])
def get_new_card():
    data = request.get_json()
    try:
        prev_item_id = int(data["previousItemId"])
        prev_quest_id = int(data["previousQuestId"])
    except ValueError:
        abort(400, "Id must be integer")
        return

    session = create_session()

    item_id = excluding_randint(1, session.query(Items).count(), prev_item_id)
    quest_id = excluding_randint(1, session.query(Quests).count(), prev_quest_id)

    item = session.query(Items).get(item_id)
    quest = session.query(Quests).get(quest_id)
    return jsonify({
        "item": item.to_dict(),
        "quest": quest.to_dict()
    })


@app.route("/ajax/get-n-items", methods=["POST"])
def get_n_items():
    data = request.get_json()
    try:
        prev_cards = list(map(int, data["cardsIDs"]))
        count = int(data["countCards"])
    except ValueError:
        abort(400, "Id and count must be integers")
        return

    session = create_session()

    items = list(map(lambda x: session.query(Items).get(x),
                     random.sample(set(range(1, session.query(Items).count())) ^ set(prev_cards), count)))

    return jsonify({
        "items": [item.to_dict() for item in items]
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
    app.run(port=8080, debug=True, host="192.168.1.77")


if __name__ == "__main__":
    main()
