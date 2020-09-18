# need = [['Какие параметры предмета можно определить на ощупь?', True, False, True, False],
#             ['Для чего создан предмет, какая его главная функция?', False, True, False, True],
#             ['Какие параметры предмета можно увидеть?', True, False, True, False],
#             ['В какую технологическую систему эволюционирует предмет?', True, False, True, False],
#             ['Каким предмет будет в будущем?', True, False, True, False],
#             ['Каким предмет был в прошлом?', False, True, True, False],
#             ['Что является надсистемой предмета?', False, True, False, True],
#             ['Из каких подсистем состоит предмет?', False, True, False, True],
#             ['Из каких материалов состоит предмет? (Из каких материалов не может состоять предмет?)', False, True,
#              False, True], ['Что выполняет такаюже функцию?', False, True, False, True],
#             ['Что такое предмет наоборот?', True, False, True, False],
#             ['Что является или может быть антисистемой предмета?', False, True, True, False],
#             ['Какие технологические системы выполняют такую же функцию?', False, True, False, True],
#             ['Как изменится мир, если этот предмет исчезнет?', True, False, True, False],
#             ['К каким последствиям привело появление предмета?', True, False, True, False],
#             ['Чего боится предмет?', True, False, False, True],
#             ['Кто/что любоит/не любит предмет?', True, False, False, True],
#             ['Какие вопросы мог бы задавать предмет, будь он живой?', True, False, False, True],
#             ['На какие вопросы может ответить предмет?', True, False, False, True],
#             ['Любимое место предмета? Комфортные условия для предмета?', True, False, False, True],
#             ['Как можно применить предмет не по прямому назначению?', False, True, False, True],
#             ['Какие звуки может издавать предмет?', True, False, True, False],
#             ['Чем пахнет или может пахнуть предмет?', True, False, True, False],
#             ['Как изменится мир, если стоимость этого предмета увеличится в 1000 раз?', True, False, True, False],
#             ['Как изменится мир, если стоимость этого предмета уменьшится в 1000 раз?', True, False, True, False], [
#                 'Что можно будет сделать из этого предмета, если вы попадете на необитаемый остров и у вас будет огромное количество этого предмета?',
#                 True, False, True, False], ['  Что с помощью предмета не получится сделать?', True, False, True, False],
#             ['Какие причины способствовали появлению предмета?', False, True, True, False],
#             ['Предмет как (на что похож), но не (отличающийся признак)?', True, False, True, False],
#             ['Этот предмет ... (какой), но не ... (что такое же)', True, False, True, False],
#             ['Этот предмет ... (что делает), но не ... (что делает так же)', True, False, True, False],
#             ['Кто или что любит этот предмет?', True, False, False, True],
#             ['Чем питается предмет?', True, False, True, False],
#             ['Какие цели мог бы ставить перед собой предмет?', True, False, True, False],
#             ['Какие качества в предмете самые важные/не важные?', True, False, True, False],
#             ['Что можно описать цифрами в предмете?', False, True, True, False],
#             ['Что является рабочим органом, двигателем, трансмиссией и органом управления в предмете?', False, True,
#              True, False], ['При каких условиях предмет не сможет работать?', True, False, True, False],
#             ['Какие должны быть условия для идеальной работы предмета?', False, True, True, False]]
#     names = ['принтер', 'парашют', "мегафон", "самосвал", "корабль", "кровать", "смеситель", "что-то", "топор", "ванна",
#              "шприц", "звонок", "стол", "саксофон", "ложка", "самокат", "коньки", "зонт", "пила", "коляска", "компас",
#              "вертолет", "маракасы", "микрофон", "телескоп", "секундомер", "паровоз", "молоток", "рояль",
#              "стиральная машина", "перчатки", "диван", "маска с трубкой", "бензоколонка", "настольная лампа",
#              "шуруповерт", "светофор", "лопата", "смеситель", "консервная банка", "YouTube", "ракетка", "огнетушитель",
#              "подкова", "солонка", "мухомор", "компьютерная мышь", "отвертка", "чашка-непроливайка", "сйеф", "пугало",
#              "вилка", "галстук", "термометр", "камин", "подводная лодка", "аквариум", "шкаф", "магнитофон", "трактор"]
#     session = create_session()
#
#     for item in need:
#         quest = Quests()
#         quest.quest, quest.image, quest.erudition, quest.leader, quest.players = item[0], item[1], item[2], item[3], item[4]
#         session.add(quest)
#
#     for i in range(len(names)):
#         item = Items()
#         item.name = names[i]
#         item.filename = f'static/img/items/{i + 1}.svg'
#         session.add(item)
#
#     session.commit()