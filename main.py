from flask import Flask, render_template

from data.db_session import global_init, create_session
from data.items import Items

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'


@app.route('/')
def main_page():
    session = create_session()
    item = session.query(Items).first()
    print(item.filename)
    return render_template('main_page.html',item=item)


def main():
    global_init("db/endless_orange.sqlite")
    app.run(port=8080)


if __name__ == '__main__':
    main()
