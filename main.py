from random import randint
from flask import Flask, render_template
from data.db_session import global_init, create_session
from data.items import Items
from data.quests import Quests

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'


@app.route('/')
def main_page():
    session = create_session()
    item = session.query(Items).get(randint(1, session.query(Items).count()))
    quest = session.query(Quests).get(randint(1, session.query(Quests).count()))
    print(item.name)
    return render_template('main_page.html', item=item,quest=quest)


def main():
    global_init("db/endless_orange.sqlite")
    # session = create_session()
    # names = ['принтер', 'парашют', "мегафон", "самосвал", "корабль", "кровать", "смеситель", "что-то", "топор", "ванна",
    #          "шприц", "звонок", "стол", "саксофон", "ложка", "самокат", "коньки", "зонт", "пила", "коляска", "компас",
    #          "вертолет", "маракасы", "микрофон", "телескоп", "секундомер", "паровоз", "молоток", "рояль",
    #          "стиральная машина", "перчатки", "диван", "маска с трубкой", "бензоколонка", "настольная лампа",
    #          "шуруповерт", "светофор", "лопата", "смеситель", "консервная банка", "YouTube", "ракетка", "огнетушитель",
    #          "подкова", "солонка", "мухомор", "компьютерная мышь", "отвертка", "чашка-непроливайка", "сйеф", "пугало",
    #          "вилка", "галстук", "термометр", "камин", "подводная лодка", "аквариум", "шкаф", "магнитофон", "трактор"]
    # for i in range(len(names)):
    #     item = Items()
    #     item.name = names[i]
    #     item.filename = f'static/img/items/{i + 1}.svg'
    #     session.add(item)
    # session.commit()
    app.run(port=8080)


if __name__ == '__main__':
    main()
